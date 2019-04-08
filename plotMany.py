#!/usr/bin/env python

# Importamos las clases de ROOT: 
from ROOT import *

import sys
import tdrstyle
import math 

# CMS Style (carga plotnames estilo para los plots)
tdrstyle.setTDRStyle()

lumi=1

# Tipo de archivo

plotname=sys.argv[1]

#plotname='InvariantMassDiMuon'
#plotname='InvariantMassMuonElectron'
#plotname='MM_METEt'

hmutaulabel='HMuTau'
scalehiggs_mutau=48.58/100000*0.01
colorhiggs_mutau=kBlack
fHMuTau = TFile.Open('histosHMuTau.root', 'read')

zlllabel='ZLL'
scale_zll=2075.14*3/100000
color_zll=kBlue
fZLL = TFile.Open('histosZLL.root', 'read')

htautaulabel='HTauTau'
scalehiggs_tautau=48.58/100000*0.06
colorhiggs_tautau=kRed
fHTauTau = TFile.Open('histosHTauTau.root', 'read')

hmumulabel='HMuMu'
scalehiggs_mumu=48.58/100000*2e-4
colorhiggs_mumu=kMagenta
fHMuMu = TFile.Open('histosHMuMu.root', 'read')

tt2l2nulabel='TT2L2Nu'
scale_tt2l2nu=831.76/100000*0.32*0.32
color_tt2l2nu=kGreen+2
fTT2L2Nu = TFile.Open('histosTT2L2Nu.root', 'read')



def plotSample(f,name,label,scale,color):
    # Cargamos el archivo root:
    histo=f.Get(plotname)

    histo.SetName('histo'+label)
    histo.SetLineColor(color)
    histo.SetLineWidth(2)
    histo.SetYTitle("Sucesos / GeV")
    histo.Scale(scale)
    print histo.Integral()

    return histo

def plot2(name):
	histo=TH1F(name,name,200,0,200)
	histo.FillRandom("gaus")
	return histo

histoHMuTau=plotSample(fHMuTau,plotname,hmutaulabel,scalehiggs_mutau*lumi,colorhiggs_mutau)
histoZLL=plotSample(fZLL,plotname,zlllabel,scale_zll*lumi,color_zll)
histoHTauTau=plotSample(fHTauTau,plotname,htautaulabel,scalehiggs_tautau*lumi,colorhiggs_tautau)
histoHMuMu=plotSample(fHMuMu,plotname,hmumulabel,scalehiggs_mumu*lumi,colorhiggs_mumu)
histoTT2L2Nu=plotSample(fTT2L2Nu,plotname,tt2l2nulabel,scale_tt2l2nu*lumi,color_tt2l2nu)



#out=TFile("savetest.root","RECREATE")
#histoHMuTau.Write()


#histoZLL=plotSample(plotname,'ZLL',6000/100000,kBlue)

# Definimos un "lienzo" para pintar los histogramas
canvas=TCanvas("canvas","Canvas Masa Invariante",800,600)  # (nombre, titulo, dimensionx, dimensiony)
canvas.Divide(1,2)
canvas.cd(1) 
canvas.cd(1).SetLogy()
histoZLL.Draw("hist")
histoHMuTau.Draw("hist,sames")
histoHTauTau.Draw("hist,sames")
histoHMuMu.Draw("hist,sames")
histoTT2L2Nu.Draw("hist,sames")
#Leyenda del histograma. Necesario cuando tienes mas de una grafica.
legend=TLegend(0.5,0.7,0.90,0.90) # (posInicio_x, posInicio_y, posFin_x, posFin_y)
legend.AddEntry(histoHMuTau,"h #mu #tau","l")
legend.AddEntry(histoHTauTau,"h #tau #tau","l")
legend.AddEntry(histoHMuMu,"h #mu #mu","l")
legend.AddEntry(histoTT2L2Nu,"t#bar{t}  ","l")
legend.AddEntry(histoZLL,"Z#rightarrow ll","l")
legend.Draw()
 

canvas.cd(2) 
histoZLL.DrawNormalized("hist")
histoHMuTau.DrawNormalized("hist,sames")
histoHTauTau.DrawNormalized("hist,sames")
histoHMuMu.DrawNormalized("hist,sames")
histoTT2L2Nu.DrawNormalized("hist,sames")

canvas.SaveAs("plot_"+plotname+".png")
