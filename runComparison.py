#!/usr/bin/env python

# Importamos las clases de ROOT: 
from ROOT import *

import tdrstyle
import math 

# CMS Style (carga variables estilo para los plots)
tdrstyle.setTDRStyle()

# Tipo de archivo
label="HMuMu"

# Cargamos el archivo root: 
f = TFile( 'gitfiles/file'+label+'.root')

# Cargamos el tree indicando el directorio y el nombre del tree:
tree = f.Get("dumpGenInfo/Ntuple")

# Cuantos sucesos hay en el tree?
entries=tree.GetEntries()
print "El tree tiene %d sucesos" %entries


# Rellenamos los histogramas con "Draw"
tree.Draw("pt>>allPt(100,0,100)")   # este comando rellena un histograma con el contenido de la rama del tree "pt"
allPt.SetTitle("Pt de todas  las particulas") # le ponemos un titulo al histograma
allPt.SetName("allPT")

# Otra forma de hacer esto (y en este caso pintando muchos histogramas):
muonPt=TH1F("muonPT","Pt del Muon", 100,0, 100)
muonMother=TH1F("muonMother","Muon Mother", 53,-26, 26)
muonPtTauDecay=TH1F("muonPTTauDecay","Pt del Muon, Tau Decay", 100,0, 100)
muonPtOther=TH1F("muonPTOther","Pt del Muon, Other", 100,0, 100)

tauPt=TH1F("tauPT","Pt del Tau", 100,0, 100)
tauMother=TH1F("tauMother","Tau Mother", 53,-26, 26)
tauDecay=TH1F("tauDecay","Tau Decay", 15,-0.5, 14.5)
tauPtVisible=TH1F("tauPTVisible","Pt del Tau Visible", 100,0, 100)

electronPt=TH1F("electronPT","Pt del Electron", 100,0, 100)
electronMother=TH1F("electronMother","Electron Mother", 53,-26, 26)
electronPtTauDecay=TH1F("electronPTTauDecay","Pt del Electron, Tau Decay", 100,0, 100)
electronPtOther=TH1F("electronPTOther","Pt del Electron, Other", 100,0, 100)

higgsPt=TH1F("higgsPT","Pt del Higgs", 100,0, 100)


for event in tree: # loop sobre los sucesos del tree 
	muon_1_pt=0
	muon_2_pt=0
	tau_pt=0
	electron_pt=0
	tau_decay=0
	muon_1_px=0
        muon_2_px=0
        muon_1_py=0
        muon_2_py=0
        muon_1_pz=0
        muon_2_pz=0
        for i in range(0,event.pt.size()): # loop sobre las particulas en este suceso
		if ( abs(event.pdgId.at(i)) ==13 ): # las condiciones que quieras, sobre el elemento "i" de cada rama
	                muonPt.Fill(event.pt.at(i))
			muonMother.Fill(event.motherPdgId.at(i))
			if (abs(event.motherPdgId.at(i))==15):
				muonPtTauDecay.Fill(event.pt.at(i))
			else:
				muonPtOther.Fill(event.pt.at(i))
			if(event.pt.at(i)>muon_1_pt):
				muon_2_pt=muon_1_pt
				muon_1_pt=event.pt.at(i)
                                muon_2_px=muon_1_px
                                muon_1_px=event.pt.at(i)*math.cos(event.phi.at(i))
                                muon_2_py=muon_1_py
                                muon_1_py=event.pt.at(i)*math.sin(event.phi.at(i))
                                muon_2_pz=muon_1_pz
                                muon_1_pz=event.pt.at(i)*math.sinh(event.eta.at(i))
			else:
				if (event.pt.at(i)>muon_2_pt):
					muon_2_pt=event.pt.at(i)
                                        muon_2_px=event.pt.at(i)*math.cos(event.phi.at(i))
                                        muon_2_py=event.pt.at(i)*math.sin(event.phi.at(i))
                                        muon_2_pz=event.pt.at(i)*math.sinh(event.eta.at(i))

                if ( abs(event.pdgId.at(i)) ==15 ): 
                        tauPt.Fill(event.pt.at(i))
                        tauDecay.Fill(event.decay.at(i))
                        tauPtVisible.Fill(event.ptvisible.at(i))
			if(event.pt.at(i)>tau_pt):
				tau_pt=event.pt.at(i)
				tau_decay=event.decay.at(i)
                if ( abs(event.pdgId.at(i)) ==11 ): 
                        electronPt.Fill(event.pt.at(i))
                        electronMother.Fill(event.motherPdgId.at(i))
                        if (abs(event.motherPdgId.at(i))==15):
                                electronPtTauDecay.Fill(event.pt.at(i))
                        else:
                                electronPtOther.Fill(event.pt.at(i))
			if(event.pt.at(i)>electron_pt):
                                electron_pt=event.pt.at(i)
                if ( abs(event.pdgId.at(i)) ==25 ): 
                        higgsPt.Fill(event.pt.at(i))

	p = math.sqrt( (muon_1_px+muon_2_px)*(muon_1_px+muon_2_px) +(muon_1_py+muon_2_py)*(muon_1_py+muon_2_py) + (muon_1_pz+muon_2_pz)*(muon_1_pz+muon_2_pz))  
	energy_1 = math.sqrt(muon_1_px*muon_1_px + muon_1_py*muon_1_py+ muon_1_pz*muon_1_pz)
        energy_2 = math.sqrt(muon_2_px*muon_2_px + muon_2_py*muon_2_py+ muon_2_pz*muon_2_pz)
	mass = math.sqrt( (energy_1+energy_2)*(energy_1+energy_2) - p*p)
	#print "Muon1 : %4.2f  %4.2f  %4.2f  ,  %4.2f  %4.2f  %4.2f  , %4.2f %4.2f" %(muon_1_px,muon_1_py,muon_1_pz,muon_2_px,muon_2_py,muon_2_pz, p, mass) 

	#print "Muon %4.2f Tau %4.2f TauDecay %d  Muon 2 %4.2f Electron %4.2f \n" %(muon_1_pt,tau_pt,tau_decay,muon_2_pt,electron_pt) 

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

tauPt.SetLineColor(kGreen+2)
tauPt.SetLineWidth(2)
tauPt.SetXTitle("Generator Particle Pt [GeV]")
tauPt.SetYTitle("Sucesos / GeV")

electronPt.SetLineColor(kBlack)
electronPt.SetLineWidth(2)
electronPt.SetXTitle("Generator Particle Pt [GeV]")
electronPt.SetYTitle("Sucesos / GeV")

# Pinta los histogramas
allPt.Draw("hist") 
muonPt.Draw("hist,sames")
tauPt.Draw("hist,sames")
electronPt.Draw("hist,sames")

#Leyenda del histograma. Necesario cuando tienes mas de una grafica.
legend=TLegend(0.5,0.7,0.90,0.90) # (posInicio_x, posInicio_y, posFin_x, posFin_y)
legend.AddEntry(allPt, "Particulas Generadas","l")
legend.AddEntry(muonPt,"Muones","l")
legend.AddEntry(tauPt,"Taus","l")
legend.AddEntry(electronPt,"Electrones","l")

legend.Draw()

# Guarda el canvas:
canvasMuPt.SaveAs("canvasMuPt.png")

#Archivo con histogramas y canvas para estudiarlo luego:
out = TFile('histos'+label+'.root',"RECREATE")
out.cd()
tauPt.Write()
tauDecay.Write()
muonPt.Write()
allPt.Write()
muonMother.Write()
muonPtTauDecay.Write()
muonPtOther.Write()
electronMother.Write()
electronPtTauDecay.Write()
electronPtOther.Write()
electronPt.Write()
higgsPt.Write()
tauPtVisible.Write()
canvasMuPt.Write()

