# ExampleAnalysisExercise
Example analysis exercise, based on HMuTau generator studies

# Generator level exercise

# Event trees structure
Available small trees of signal and background samples relevant for the Higgs to Muon Tau analysis.  The trees contain slimmed generator level information based on HEPMC. 

The information skim is as follow: 
- All events are saved, but not all the generator level particles produced in each event are kept.
- For each event, the particle variables are saved in a vector [particle 1, particle 2, particle 3,....]
    pt--> [pt particle 1, pt particle 2, pt particle 3, pt particle 4, ... ] 
    eta -> [eta particle 1, eta particle 2, eta particle 3, eta particle 4, ... ] 
    (etc)
- Particles saved: Electrons (pdgID=11), Muons (pdgID=13), Taus (pdgID=15), Neutrinos (pdgID=12,14,16), Higgs (pdgID=25), Z boson (pdgID=23), W boson (pdgID=24)
- Pythia8 status:  
    - Electrons, Muons, and Neutrinos are saved only the final state (pythia status=1),  removing intermediate particles 
    - Taus are saved just before decay (status=2), and the decay information is kept in a "decay" flag that encodes the tau decay (posible values of the flag: 0=1pi+,0pi0 1=1pi+,1pi0  2=1pi+,2pi0 3=3pi+,0pi0 4=3pi+,1pi0 5=other hadronic decay; 11=electron decay, 13=muon decay) 
    - Bosons are saved in the first state in which they appear (typically pythia values 21-29)
- Quantities saved per particle: pt, eta, phi, mass, pdgID, status, motherPdgID, motherStatus, numberOfDaughters, decay (for taus only), ptvisible (also only for taus, in development)
- Event variables: event number, generator level weight for aMC@NLO


# First exercises: plot muon pt from a HiggsToMuTau tree 
Run 
python ExampleMuons.py 

--> Two different ways to draw histograms from the information in a tree: tree->Draw, and a loop over the particles are compared
--> The result of the program is double: a canvas is plotted (all particles vs muons), and a root file containing the plots is produced 

Exercise 0: get this program to run and inspect the results :)

Exercise 1: plot different muon variables out of the ones available 
Exercise 2: plot also taus and electrons 
Exercise 3: what is the origin of the muons in the event? distinguish muons that are decayed from a tau and muons that aren't: are they similar? 
Exercise 4: what is the origin of the electrons in the event? distinguish electrons that are decayed from a tau and electrons that aren't: are they similar? 
Exercise 5: compare muons, taus and electrons : what can you say about the process you are studying? 

 
    
 
