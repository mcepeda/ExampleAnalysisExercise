#!/usr/bin/env python

# Importamos las clases de ROOT: 
from ROOT import *

# Cargamos el archivo root:
f = TFile( 'fileHMuTau.root')

# Cargamos el tree indicando el directorio y el nombre del tree:
tree = f.Get("dumpGenInfo/Ntuple")

# Cuantos sucesos hay en el tree?
entries=tree.GetEntries()
print "El tree tiene %d sucesos" %entries

# Rellenamos los histogramas con "Draw"
tree.Draw("pt>>allPt(100,0,100)")   # este comando rellena un histograma con el contenido de la rama del tree "pt"
allPt.SetTitle("Pt de todas  las particulas") # le ponemos un titulo al histograma
allPt.SetName("allPT")

# ponemos una condicion: solo rellenamos particulas que cumplan "pdgID==13" (codigo MC que significa muon)
tree.Draw("pt>> muonPt(100,0,100)","abs(pdgId)==13") 
muonPt.SetTitle("Pt de todas  las particulas")
muonPt.SetName("allPT")

# Otra forma de hacer esto:
#primero definimos el histograma
muonPtV2=TH1F("muonPTV2","Pt del Muon, Segundo Modo", 100,0, 100)

for event in tree: # loop sobre los sucesos del tree 
        for i in range(0,event.pt.size()): # loop sobre las particulas en este suceso
		if ( abs(event.pdgId.at(i)) ==13 ): # las condiciones que quieras, sobre el elemento "i" de cada rama
	                muonPtV2.Fill(event.pt.at(i))

# Definimos un "lienzo" para pintar los histogramas
canvasMuPt=TCanvas("canvas","Momento de los Muones",800,600)  # (nombre, titulo, dimensionx, dimensiony)
canvasMuPt.cd() # carga el histograma 

#Estilo del Plot (Color, Etiquetas de los ejes, etc)
allPt.SetLineColor(kRed)
allPt.SetLineWidth(2)
allPt.SetXTitle("Generator Particle Pt [GeV]")
allPt.SetYTitle("Sucesos / GeV")

muonPt.SetLineColor(kBlue)
muonPt.SetLineWidth(2)
muonPt.SetXTitle("Generator Particle Pt [GeV]")
muonPt.SetYTitle("Sucesos / GeV")

muonPtV2.SetLineColor(kCyan)
muonPtV2.SetLineStyle(kDashed)
muonPtV2.SetLineWidth(2)
muonPtV2.SetXTitle("Generator Particle Pt [GeV]")
muonPtV2.SetYTitle("Sucesos / GeV")

# Pinta los histogramas
allPt.Draw("hist") 
muonPt.Draw("hist,sames")
muonPtV2.Draw("hist,sames")

#Leyenda del histograma. Necesario cuando tienes mas de una grafica.
legend=TLegend(0.5,0.7,0.90,0.90) # (posInicio_x, posInicio_y, posFin_x, posFin_y)
legend.AddEntry(allPt, "Particulas Generadas","l")  # nombre, titulo, opcion de la linea
legend.AddEntry(muonPt,"Muones","l")
legend.AddEntry(muonPtV2,"Muones (loop)","l")

legend.Draw()

# Guarda el canvas:
canvasMuPt.SaveAs("canvasMuPt.png")

#Archivo con histogramas y canvas para estudiarlo luego:
out = TFile('histos.root',"RECREATE")
out.cd()
muonPt.Write()
allPt.Write()

