#!/usr/bin/env python

# Importamos las clases de ROOT: 
from ROOT import *

import sys
import tdrstyle
import math 

# CMS Style (carga variables estilo para los plots)
tdrstyle.setTDRStyle()

# Tipo de archivo
label=sys.argv[1] 

# Cargamos el archivo root: 
f = TFile( 'file'+label+'.root')

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
muonPt=TH1F("muonPT","", 100,0, 100)
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

InvariantMassDiMuon=TH1F("InvariantMassDiMuon","Invariant Mass 2 Muons",200,0,200)
InvariantMassMuonTau=TH1F("InvariantMassMuonTau","Invariant Mass Muon Tau",200,0,200)
InvariantMassMuonElectron=TH1F("InvariantMassMuonElectron","Invariant Mass Muon Electron",200,0,200)
InvariantMassMuonTauVisible=TH1F("InvariantMassMuonTauVisible","Invariant Mass Muon TauVisible",200,0,200)

CollinearMassDiMuon=TH1F("CollinearMassDiMuon","Collinear Mass 2 Muons",200,0,200)
CollinearMassMuonTau=TH1F("CollinearMassMuonTau","Collinear Mass Muon Tau",200,0,200)
CollinearMassMuonElectron=TH1F("CollinearMassMuonElectron","Collinear Mass MuonElectron",200,0,200)

MM_MuonLead=TH1F("MM_MuonLead","", 100,0, 100)
MM_MuonSubLead=TH1F("MM_MuonSubLead","", 100,0, 100)
ME_MuonLead=TH1F("ME_MuonLead","", 100,0, 100)
ME_ElectronLead=TH1F("ME_ElectronLead","", 100,0, 100)

MM_METEt=TH1F("MM_METEt","", 100,0, 100)
ME_METEt=TH1F("ME_METEt","", 100,0, 100)

MM_deltaPhiMu1Met=TH1F("MM_deltaPhiMu1Met","", 100,0,6)
MM_deltaPhiMu2Met=TH1F("MM_deltaPhiMu2Met","", 100,0,6)
MM_deltaPhiMu1Mu2=TH1F("MM_deltaPhiMu1Mu2","", 100,0,6)
MM_deltaEtaMu1Mu2=TH1F("MM_deltaEtaMu1Mu2","", 100,0,6)

ME_deltaPhiMuMet=TH1F("ME_deltaPhiMuMet","", 100,0,6)
ME_deltaPhiEleMet=TH1F("ME_deltaPhiEleMet","", 100,0,6)
ME_deltaPhiMuEle=TH1F("ME_deltaPhiMuEle","", 100,0,6)
ME_deltaEtaMuEle=TH1F("ME_deltaEtaMuEle","", 100,0,6)

M_PI=3.14159265358979323846264338328

def normDPhi(dphi):
        if dphi>M_PI:
		dphi = dphi-2.0*M_PI    
	elif dphi<=-M_PI:	
		dphi = dphi+2.0*M_PI
	return abs(dphi)


import math 

for event in tree: # loop sobre los sucesos del tree 
	muon_1_pt=0
	muon_2_pt=0
	tau_pt=0
	electron_pt=0
	tau_decay=0
	tau_mother=0
	muonindex_1 = 0
	muonindex_2 = 0
	tauindex = 0
	electronindex = 0
	nmuons=0 
	ntaus=0 
	nhadtaus=0
	nelectrons=0

        met_px=0
	met_py=0 

        for i in range(0,event.pt.size()): # loop sobre las particulas en este suceso
		if  ( abs(event.pdgId.at(i)) ==12 or  abs(event.pdgId.at(i)) ==14 or abs(event.pdgId.at(i)) ==16):
			met_px=met_px+event.pt.at(i)*math.cos(event.phi.at(i))
	                met_py=met_py+event.pt.at(i)*math.sin(event.phi.at(i))


		if event.pt.at(i) <10 :
			continue 
 
		if ( abs(event.pdgId.at(i)) ==13 ): # las condiciones que quieras, sobre el elemento "i" de cada rama
			nmuons+=1
	                muonPt.Fill(event.pt.at(i))
			muonMother.Fill(event.motherPdgId.at(i))
			if (abs(event.motherPdgId.at(i))==15):
				muonPtTauDecay.Fill(event.pt.at(i))
			else:
				muonPtOther.Fill(event.pt.at(i))
			if(event.pt.at(i)>muon_1_pt):
				muon_2_pt=muon_1_pt
				muon_1_pt=event.pt.at(i)
				muonindex_2 = muonindex_1
				muonindex_1 = i 
			else:
				if (event.pt.at(i)>muon_2_pt):
					muon_2_pt=event.pt.at(i)
					muon_2_eta=event.eta.at(i)
					muonindex_2= i
                if ( abs(event.pdgId.at(i)) ==15 ): 
			ntaus+=1
                        tauPt.Fill(event.pt.at(i))
                        tauDecay.Fill(event.decay.at(i))
                        tauPtVisible.Fill(event.ptvisible.at(i))
			tauindex=i
			if event.decay.at(i)!=13 and event.decay.at(i)!=11:
				nhadtaus+=1
			if(event.pt.at(i)>tau_pt):
				tau_pt=event.pt.at(i)
				tau_decay=event.decay.at(i)
				tau_mother=event.motherPdgId.at(i)
			#if (ntaus>1) :
			#	print "WHY? - %d - %4.2f %4.2f %4d - %4.2f %4.2f %4d "%(ntaus,tau_pt,tau_decay,tau_mother,event.pt.at(i),event.decay.at(i),event.motherPdgId.at(i))
                if ( abs(event.pdgId.at(i)) ==11 ): 
			nelectrons+=1
                        electronPt.Fill(event.pt.at(i))
                        electronMother.Fill(event.motherPdgId.at(i))
			electronindex=i
                        if (abs(event.motherPdgId.at(i))==15):
                                electronPtTauDecay.Fill(event.pt.at(i))
                        else:
                                electronPtOther.Fill(event.pt.at(i))
			if(event.pt.at(i)>electron_pt):
                                electron_pt=event.pt.at(i)
                if ( abs(event.pdgId.at(i)) ==25 ): 
                        higgsPt.Fill(event.pt.at(i))

#	print "%d %4d %4d " %(nmuons, nhadtaus, nelectrons)

	met_et=math.sqrt(met_px*met_px+met_py*met_py) 
        met_phi=0
	if met_px>0:
		met_phi=math.atan(met_py/met_px)	

#	if met_et < 20: 
#		continue
#	if muon_1_pt < 40:
#		continue 


	if (nmuons>=1):
	        muon_1_px=event.pt.at(muonindex_1)*math.cos(event.phi.at(muonindex_1))
        	muon_1_py=event.pt.at(muonindex_1)*math.sin(event.phi.at(muonindex_1))
        	muon_1_pz=event.pt.at(muonindex_1)*math.sinh(event.eta.at(muonindex_1))

		muon_1_eta=event.eta.at(muonindex_1)
        	muon_1_phi=event.phi.at(muonindex_1)

		if (nmuons ==2): 
	        	muon_2_px=event.pt.at(muonindex_2)*math.cos(event.phi.at(muonindex_2))
        		muon_2_py=event.pt.at(muonindex_2)*math.sin(event.phi.at(muonindex_2))
        		muon_2_pz=event.pt.at(muonindex_2)*math.sinh(event.eta.at(muonindex_2))
	        	muon_2_eta=event.eta.at(muonindex_2)
        		muon_2_phi=event.phi.at(muonindex_2)

			p = math.sqrt( (muon_1_px+muon_2_px)*(muon_1_px+muon_2_px) +(muon_1_py+muon_2_py)*(muon_1_py+muon_2_py) + (muon_1_pz+muon_2_pz)*(muon_1_pz+muon_2_pz))  
			energy_1 = math.sqrt(muon_1_px*muon_1_px + muon_1_py*muon_1_py+ muon_1_pz*muon_1_pz)
        		energy_2 = math.sqrt(muon_2_px*muon_2_px + muon_2_py*muon_2_py+ muon_2_pz*muon_2_pz)
			mass = math.sqrt( (energy_1+energy_2)*(energy_1+energy_2) - p*p)


#			if normDPhi(met_phi-event.phi.at(muonindex_2))>1.5:
#				continue 

			InvariantMassDiMuon.Fill(mass)	
			MM_MuonLead.Fill(event.pt.at(muonindex_1))
                        MM_MuonSubLead.Fill(event.pt.at(muonindex_2))
			MM_METEt.Fill(met_et)
			MM_deltaPhiMu1Met.Fill(normDPhi(met_phi-event.phi.at(muonindex_1)))
                        MM_deltaPhiMu2Met.Fill(normDPhi(met_phi-event.phi.at(muonindex_2)))
                        MM_deltaPhiMu1Mu2.Fill(normDPhi(event.phi.at(muonindex_1)-event.phi.at(muonindex_2)))
                        MM_deltaEtaMu1Mu2.Fill(abs(event.eta.at(muonindex_1)-event.eta.at(muonindex_2)))

			# coll mass ?
                        ptnu = abs(met_et*math.cos(normDPhi(met_phi -event.phi.at(muonindex_2))))
			taufraction=event.pt.at(muonindex_2)/ ( event.pt.at(muonindex_2)+ptnu)
			CollinearMassDiMuon.Fill(mass/math.sqrt(taufraction)) 

		elif (nhadtaus==1) :
                        tau_eta=event.eta.at(tauindex)
                        tau_phi=event.phi.at(tauindex)
			tau_pt_visible=event.ptvisible.at(tauindex)

			mass=math.sqrt(2*muon_1_pt*tau_pt*(math.cosh(muon_1_eta-tau_eta)-math.cos( muon_1_phi - tau_phi)))
                        mass2=math.sqrt(2*muon_1_pt*tau_pt_visible*(math.cosh(muon_1_eta-tau_eta)-math.cos(muon_1_phi - tau_phi)))
					
                        InvariantMassMuonTau.Fill(mass)
                        InvariantMassMuonTauVisible.Fill(mass2)

                        # coll mass ?
			if tau_pt_visible>0 :
                                ptnu = abs(met_et*math.cos(normDPhi(met_phi-tau_phi)))
                                taufraction=tau_pt_visible /  (tau_pt_visible+ptnu)
        	                CollinearMassMuonTau.Fill(mass2/math.sqrt(taufraction))
			else :
				CollinearMassMuonTau.Fill(0)


		elif (nelectrons==1):
#			print tau_decay
                        electron_eta=event.eta.at(electronindex)
                        electron_phi=event.phi.at(electronindex)
                        mass=math.sqrt(2*muon_1_pt*electron_pt*(math.cosh(muon_1_eta-electron_eta)-math.cos(muon_1_phi - electron_phi)))

#			if normDPhi(met_phi-event.phi.at(electronindex))> 1.5:
#				continue 

                        InvariantMassMuonElectron.Fill(mass)
                        ME_MuonLead.Fill(muon_1_pt)
                        ME_ElectronLead.Fill(electron_pt)
                        ME_METEt.Fill(met_et)
                        ME_deltaPhiMuMet.Fill(normDPhi(met_phi-event.phi.at(muonindex_1)))
                        ME_deltaPhiEleMet.Fill(normDPhi(met_phi-event.phi.at(electronindex)))
                        ME_deltaPhiMuEle.Fill(normDPhi(event.phi.at(muonindex_1)-event.phi.at(electronindex)))
                        ME_deltaEtaMuEle.Fill(abs(event.eta.at(muonindex_1)-event.eta.at(electronindex)))
                        # coll mass ?
                        ptnu = abs(met_et*math.cos(normDPhi(met_phi-electron_phi)))
                        taufraction=electron_pt/ ( electron_pt +ptnu)
                        CollinearMassMuonElectron.Fill(mass/math.sqrt(taufraction))




	#mass2=math.sqrt(2*muon_1_pt*muon_2_pt*(math.cosh(muon_1_eta -muon_2_eta)-math.cos( muon_1_phi - muon_2_phi)))
	#print "%4.2f %4.2f" %(mass,mass2)

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
InvariantMassDiMuon.Write()
InvariantMassMuonElectron.Write()
InvariantMassMuonTau.Write()
InvariantMassMuonTauVisible.Write()


MM_MuonLead.Write()
MM_MuonSubLead.Write()
MM_METEt.Write()
MM_deltaPhiMu1Met.Write()
MM_deltaPhiMu2Met.Write()
MM_deltaPhiMu1Mu2.Write()
MM_deltaEtaMu1Mu2.Write()

ME_MuonLead.Write()
ME_ElectronLead.Write()
ME_METEt.Write()
ME_deltaPhiMuMet.Write()
ME_deltaPhiEleMet.Write()
ME_deltaPhiMuEle.Write()
ME_deltaEtaMuEle.Write()

CollinearMassDiMuon.Write()
CollinearMassMuonTau.Write()
CollinearMassMuonElectron.Write()


