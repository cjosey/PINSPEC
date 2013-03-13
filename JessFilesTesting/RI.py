#Resonance Integral
import matplotlib.pyplot as plt
import os
import numpy
import math
#from scipy.integrate import simps

#Read in array for fictitious XS at 300
cur_dir = os.getcwd()+'/U-238-capture300.txt'
res300=open(cur_dir, 'r').readlines()
En300=numpy.array([])
barns300=numpy.array([])
invEn300=numpy.array([])
for line in res300:
	En300t, barns300t=line.split('  ', 1)
        En300t=float(En300t)
	barns300t=float(barns300t)
	invEn300t=1/En300t
        En300=numpy.append(En300,En300t)
        barns300=numpy.append(barns300,barns300t)
	invEn300=numpy.append(invEn300, invEn300t)
print "read in fake XS ok"

#Read in array for ENDF7 XS at 300
cur_p = os.getcwd()+'/U-238-captureRealEndF7.txt'
Endf300=open(cur_p, 'r').readlines()
EndfE300=numpy.array([])
barnsEndF300=numpy.array([])
invEndfE300=numpy.array([])
for line in Endf300:
	EndfE300t, barnsEndF300t=line.split(',', 1)
	EndfE300t=float(EndfE300t)
	barnsEndF300t=float(barnsEndF300t)
        invEndfE300t=1/EndfE300t
        EndfE300=numpy.append(EndfE300,EndfE300t)
	barnsEndF300=numpy.append(barnsEndF300,barnsEndF300t)
	invEndfE300=numpy.append(invEndfE300,invEndfE300t)
print "read in ENDF7 XS ok"

#Plot values on top of each other
fig=plt.figure()
plt.loglog(En300,barns300)
plt.loglog(EndfE300,barnsEndF300)
plt.legend(["Fake U238 XS, 300","ENDFBVII U238 XS, 300"])
plt.grid()
plt.title('U238 Cross Section Comparison')
plt.xlabel('XS [barns]')
plt.ylabel('E [eV]')
plt.savefig("XS_Comparison_300.png")

#Resonance Integral Boundaries, can be passed in
RIb=numpy.array([[0.01,0.1],[0.1,1.0],[6,10],[1,6],[10,25],[25,50],[50,100],[0.5,10000]], dtype=float)

#Make loop for RI calculation for Fake U238
prod=numpy.zeros_like(barns300)
prodr=numpy.zeros_like(barnsEndF300)
RIfake=numpy.zeros(len(RIb), dtype=float)
RIreal=numpy.zeros(len(RIb), dtype=float)

for i in range(len(RIb-1)):
	#Retrieve bounds
	Elow=RIb[i,0]
	Eupp=RIb[i,1]
	
	#Find index matching boundary in Energy vectors
	indlow=numpy.flatnonzero(En300>=Elow) 
	indlo=numpy.array([indlow[0]], dtype=int)
	indupp=numpy.flatnonzero(En300>=Eupp)
	indup=numpy.array([indupp[0]], dtype=int)
	indlowr=numpy.flatnonzero(EndfE300>=Elow) 
	indlor=numpy.array([indlowr[0]], dtype=int)
	induppr=numpy.flatnonzero(EndfE300>=Eupp)
	indupr=numpy.array([induppr[0]], dtype=int)

	#create vector to integrate, in	tegrate
	prod=(barns300*invEn300)
	prodr=(barnsEndF300*invEndfE300)
	#en vector=En300
	RIfake[i]=numpy.trapz(prod[indlo:indup],En300[indlo:indup])
	RIreal[i]=numpy.trapz(prodr[indlor:indupr],EndfE300[indlor:indupr])
print "Resonance Integral Bounds:"
print RIb
print "Fake U238 Resonance Integrals"
print str(RIfake)
print "Real U238 Resonance Integrals integrated from ENDF7 XS"
print str(RIreal)
	
