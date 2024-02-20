import numpy as np
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
import functions_xDLVO as fn
import pandas as pd
import openpyxl
import Compare as cm

'''CHECKBOX'''

# Geometry
list_geometry = ['SS', 'SP']  # SS sphere-sphere, SP sphere-plate
geometry = list_geometry[0]
if geometry == 'SS':
    SS = 1
    SP = 0
else:
    SP = 1
    SS = 0

# Coated systems
list_coated = [0, 1]
cbCOATED = list_coated[0]
list_cb = [0, 1]  # 0 False, 1 True
cb1 = list_cb[0]  # coated colloid - coated collector
cb2 = list_cb[0]  # colloid - coated collector
cb3 = list_cb[0]  # coated colloid - collector
VDWmode = 0
if cbCOATED == 1:
    if cb1 == 1:
        VDWmode = 1  # 1 coated colloid - coated collector
    elif cb2 == 1:
        VDWmode = 2  # 2 colloid - coated collector
    elif cb3 == 1:
        VDWmode = 3  # 3 coated colloid - collector

# Roughness
list_roughness = [0, 1, 2, 3]  # Rmode0 = Smooth Rmode1 = Rough Colloid Rmode=2 Rough Collector Rmode=3 Rough Colloid and Collector
Rmode = list_roughness[0]

# Hamaker constant calculated from fundamentals
list_cbA132 = [0, 1]  # checkbox list of hamaker from fundamentals
cbA132 = list_cbA132[0]  # checkbox hamaker from fundamentals

# Acid-Base energy at minimum separation distance calculated from fundamentals
list_cbgammaAB = [0, 1]  # checkbox list of Acid-Base energy at minimum separation distance from fundamentals
cbgammaAB = list_cbgammaAB[0]  # checkbox Acid-Base energy at minimum separation distance from fundamentals

# Work of adhesion calculated from fundamentals
list_cbW132 = [0, 1]  # checkbox list of Work of adhesion from fundamentals
cbW132 = list_cbW132[0]  # checkbox Work of adhesion from fundamentals

# Contact Radius calculated from fundamentals
list_cbacont = [0, 1]  # checkbox list of Contact Radius from fundamentals
cbacont = list_cbacont[0]  # checkbox Contact Radius from fundamentals

# xDLVO PROFILES
list_cbHET = [0, 1]  # checkbox list over heterodomain radii (m) for ZOI areal fractions (AFRACT)
cbHET = list_cbHET[0]  # checkbox over heterodomain radii (m) for ZOI areal fractions (AFRACT)

list_cbHETUSER = [0, 1]  # checkbox list over user-specified heterodomain radii (m)
cbHETUSER = list_cbHETUSER[1]  # checkbox over user-specified heterodomain radii (m)

'''DATA'''
## vdW parameters
# initialize vdw fundamentals
ve = 'N/A'
e1 = 'N/A'
n1 = 'N/A'
e2 = 'N/A'
n2 = 'N/A'
e3 = 'N/A'
n3 = 'N/A'
A132calc = 'N/A'
## initialize vdw coated system parameters
#coating thickness and Fluid Hamaker constant
T1 = 'N/A'
T2 = 'N/A'
A33 = 'N/A'
#combined Hamaker
A12 = 'N/A'
A12p = 'N/A'
A13 = 'N/A'
A1p2 = 'N/A'
A1p2p = 'N/A'
A1p3 = 'N/A'
A23 = 'N/A'
A2p3 = 'N/A'
#combined Hamaker calculated flag
A12c = 0
A12pc = 0
A13c = 0
A1p2c = 0
A1p2pc = 0
A1p3c = 0
A23c = 0
A2p3c = 0
# single materials Hamaker
A11 = 'N/A'
A1p1p = 'N/A'
A22 = 'N/A'
A2p2p = 'N/A'
# hamaker constributions
s1A1p2p = 'N/A'
s1A12p = 'N/A'
s1A1p2 = 'N/A'
s1A12 = 'N/A'
s2A12p = 'N/A'
s2A12 = 'N/A'
s3A1p2 = 'N/A'
s3A12 = 'N/A'
## initialize acid-base energy fundamentals
g1pos = 'N/A'
g1neg = 'N/A'
g2pos = 'N/A'
g2neg = 'N/A'
g3pos = 'N/A'
g3neg = 'N/A'
gammaABcalc = 'N/A'
## initialize work of adhesion fundamentals
g1LW = 'N/A'
g2LW = 'N/A'
g3LW = 'N/A'
INDgammaAB = 'N/A'
W132calc = 'N/A'
## initialize contact radius for steric interaction fundamentals
E1 = 'N/A'
E2 = 'N/A'
v1 = 'N/A'
v2 = 'N/A'
INDW132 = 'N/A'
Kint = 'N/A'
acontCALC = 'N/A'

# Main parameters
T = 293.15  # temperature(K)
IS = 6.0  # Ionic strength (IS) (mol/m3)
a1 = 2.2e-6  # Colloid radius (a1) (m)
a2 = 2.55e-4  # Collector radius (a2) (m)
zetac = -0.070  # Colloid zeta potential (z1) (V)
zetap = -0.065  # Collector zeta potential (z2) (V)
z = 1  # Valence of the symmetric electrolyte (z) (-)
epsilonR = 80.0  # Relative permittivity of water (epsilonR) (-)
lambdavdW = 1.0e-7  # vdW characterisitic wavelength (lambdaVDW) (m)
sigmaC = 3.0e-10  # Born collision diameter (sigmac) (m)

# Extended DLVO parameter
lambdaAB = 6.0e-10  # Lewis acid-base decay length (lambdaAB) (m)
lambdaSTE = 4.1e-10  # Steric decay length (lambdaSTE) (m)
gammaSTE = 1.7e-2  # Steric energy at minimum separation distance (gammaSTE) (J/m2)
aasp = 0.0  # Asperity height above mean surface (aasp) (m)
acont = 5.0e-8  # Contact Radius (acont) (m)
if Rmode > 0:
    aasp = 1.0e-08  # Asperity height above mean surface (aasp) (m)

# Hamaker constant parameter
if cbA132 == 1:
    ve = 2.04e15  # Main electronic absorption frequency (ve) (s-1)
    e1 = 2.55  # Colloid dielectric constant (e1) (-)
    n1 = 1.557  # Colloid refractive index (n1) (-)
    e2 = 3.8  # Collector dielectric constant (e2) (-)
    n2 = 1.448  # Collector refractive index (n2) (-)
    e3 = 80  # Fluid dielectric constant (e3) (-)
    n3 = 1.333  # Fluid refractive index (n3) (-)
A132 = 7.17e-21  # Hamaker constant (ve  equivalent)  (J)

# Acid-base surface energy components
if cbgammaAB == 1:
    g1pos = 0.0  # Colloid electron acceptor (g1pos) (J/m2)
    g1neg = 1.10e-3  # Colloid electron donor (g1neg) (J/m2)
    g2pos = 1.00e-4  # Colloid electron acceptor (g2pos) (J/m2)
    g2neg = 37.50e-3  # Colloid electron donor (g2neg) (J/m2)
    g3pos = 25.50e-3  # Colloid electron acceptor (g3pos) (J/m2)
    g3neg = 25.50e-3  # Colloid electron donor (g2neg) (J/m2)
gammaAB = -0.0270305  # Acid-Base energy at minimum separation distance (gammaAB) (J/m2)

# Work of adhesion (for contact area)
if cbW132 == 1:
    g1LW = 42.00e-3  # Colloid van der Waals free energy (g1LW) (J/m2)
    g2LW = 27.30e-3  # Collector van der Waals free energy (g2LW) (J/m2)
    g3LW = 21.80e-3  # Fluid van der Waals free energy (g3LW) (J/m2)
    INDgammaAB = -0.0270305  # Acid-base energy at minimum separation distance (J/m2)

# Contact Radius (for steric interaction)
if cbacont == 1:
    E1 = 3.0e9  # Colloid Young's modulus (E1) (N/m2)
    E2 = 7.3e10  # Collector Young's modulus (E2) (N/m2)
    v1 = 0.33  # Colloid Poison's ratio (v1) (-)
    v2 = 0.22  # Collector Poison's ratio (v2) (-))
W132 = -0.028448  # Work of adhesion (W132) (J/m2))

# COATED SYSTEM
if cbCOATED == 1:
    # Coating thickness and Fluid Hamaker constant
    T1 = 2.30e-9  # Colloid coated thickness (m)
    T2 = 1.0e-7  # Collector coated thickness (m)
    A33 = 3.70e-20  # Fluid Hamaker Constant (A33) (J)

    # Hamaker constant contributions
    if VDWmode == 1:
        s1A1p2p = 3.7e-20  # colloid coating - collector coating
        s1A12p = 0  # colloid - collector coating
        s1A1p2 = 0  # colloid coating - collector
        s1A12 = 0  # colloid - collector
    if VDWmode == 2:
        s2A12p = 3.7e-20  # colloid - collector coating
        s2A12 = 3.7e-20  # colloid - collector
    if VDWmode == 3:
        s3A1p2 = 3.7e-20  # colloid coating - collector
        s3A12 = 0  # colloid - collector

    # Hamaker constants - Single material values
    A11 = 6.50e-20  # Colloid Hamaker constant (A11) (J)
    A1p1p = 7.00e-20  # Colloid coating Hamaker constant (A1p1p) (J)
    A22 = 6.30e-20  # Collector Hamaker constant (A22) (J))
    A2p2p = 1.51e-19  # Collector coating Hamaker constant (A2p2p) (J)

    # Combined Hamaker constant - Coated system
    A12 = (A11**0.5)*(A22**0.5)  # Colloid - Collector (A12) (J)
    A12p = (A11**0.5)*(A2p2p**0.5)  # Colloid - Collector Coating (A12p) (J)
    A13 = (A11**0.5)*(A33**0.5)  # Colloid - Fluid (A13) (J)
    A1p2 = (A1p1p**0.5)*(A22**0.5)  # Colloid Coating - Collector  (A1p2) (J)
    A1p2p = (A1p1p**0.5)*(A2p2p**0.5)  # Colloid Coating - Collector Coating (A1p2p) (J)
    A1p3 = (A1p1p**0.5)*(A33**0.5)  # Colloid Coating - Fluid  (A1p3) (J)
    A23 = (A22**0.5)*(A33**0.5)  # Collector - Fluid  (A23) (J)
    A2p3 = (A2p2p**0.5)*(A33**0.5)  # Collector Coating - Fluid  (A2p3) (J)

#xDLVO profiles
zetahet = None
if cbHETUSER == 1:
    rhet1USER = 3.3e-08  # heterodomain radii (m) for 0.25 ZOI
    rhet2USER = 6.6e-08  # heterodomain radii (m) for 0.5 ZOI
    rhet3USER = 1.32e-07  # heterodomain radii (m) for 0.75 ZOI
    rhet4USER = 2.64e-07  # heterodomain radii (m) for 1 ZOI
    zetahet = 0.051  # Heterodomain zeta potential (zhet) (V)
if cbHET == 1:
    zetahet = 0.051  # Heterodomain zeta potential (zhet) (V)

'''CALCULATE PROFILES'''

# define constants
kb =1.3806485E-23  # Boltzmann constant J/K
kt = kb*T  # (J)
hp = 6.62607004E-34  # Planck constant J.s
e_charge = 1.602176621e-19  # elementary charge (C)
Na = 6.02214086e+23  # avogadro number (-)
epsilon0 = 8.85418781762e-12  # Vacuum permitivity (C2/(N.m2))
epsilonW = epsilon0*epsilonR  # Water permitivity (C2/(N.m2))

# Number of interactions per asperity
# Ranges from 1-4 for opposed and complimentary packed asperities, respectively.
# Recommended value is 2.5
Nco = 2.5

# Minimum separation distance, generally accepted to be 1.58 amstrongs (in vacuum Israelachvili)
# ho = 1.58e-10

# Calculated parameters
# Inverse Debye lenght
k = 1/(epsilonW*kb*T/2/Na/z**2/e_charge**2/IS)**0.5 #inverse Debye lenght

# Radius of zone of influence (rZOI) for EDL
rZOI = 2*(a1*k**-1)**0.5
# set rZOI field value
# set(handles.rZOI,'Enable','on')
# set(handles.rZOI,'String',num2str(rZOI))

# Radius of zone of influence (rZOIAB) for Acid-base
rZOIAB = 2*(a1*lambdaAB)**0.5

rhetv = np.zeros(4)
afvector = np.zeros(4)

if cbHET == 1:
    # Calculate rhetvector corresponding to 0.25 0.5 0.75 and 1.0 ZOI
    afvector = np.array([0.25, 0.5,  0.75,  1.0])  # ZOI area fractional vector
    rhetv = (afvector*rZOI**2)**0.5  # heterodomain radii vector
    rhet1 = rhetv[0]  # heterodomain radii (m) for 0.25 ZOI
    rhet2 = rhetv[1]  # heterodomain radii (m) for 0.5 ZOI
    rhet3 = rhetv[2]  # heterodomain radii (m) for 0.75 ZOI
    rhet4 = rhetv[3]  # heterodomain radii (m) for 1.0 ZOI

if cbHETUSER == 1:
    # obtain rhetvector corresponding to user specified rhets
    rhetv[0] = rhet1USER  # heterodomain radii vector
    rhetv[1] = rhet2USER  # heterodomain radii vector
    rhetv[2] = rhet3USER  # heterodomain radii vector
    rhetv[3] = rhet4USER  # heterodomain radii vector
    # hetdomain area vector
    ahetv = rhetv**2*np.pi  # hetdomain area vector
    afvector = ahetv/(rZOI**2*np.pi) # ZOI area fractional vector
    afvector[afvector>1]=1  # bound fractional area to maximum coverage
if Rmode > 0:
    # Set number of asperities in zone of influence EDL and vdw
    asplim = 0.5*(np.pi**0.5)*rZOI
    if (aasp>=asplim):
        n = 1  # number of asperities in ZOI EDL and VDW
    else:
        n = rZOI**2/(aasp**2)*(np.pi/4)  # number of asperities in ZOI EDL and VDW

    # Calculate number of asperities in zone of influence for AB
    asplimAB = 0.5*(np.pi**0.5)*rZOIAB
    if (aasp>=asplimAB):
        nAB = 1  # number of asperities in ZOI ABL
    else:
        nAB = (rZOIAB**2)/(aasp**2)*(np.pi/4)  # number of asperities in ZOI ABL

# Smooth surface coverage for EDL
if Rmode>0 and aasp>0.0:
    theta = 1.0-np.pi/4
else:
    theta = 1.0

# Radius of steric hydration contact
aSte = (acont**2+2*lambdaSTE*(a1+(a1**2-acont**2)**0.5))**0.5 #radius of steric hydration contact

'''DISTANCE VECTOR '''
step_factor = 0.01
hmax = 1.0e-6
hmin = 1.0e-10
h = [hmin]
i = 0
while h[i] < hmax:
     new_distance = h[i] * (1 + step_factor)
     h.append(new_distance)
     i += 1
H = np.array(h)

# Separation distance for offset smooth surface (Rmode > 0)
if Rmode == 1 or Rmode == 2:
    Hoff = aasp  # complimentary offset surface distance
    H2 = H + Hoff
if Rmode == 3:
    Hoff = 0.5*(2*aasp + np.sqrt(3)*aasp)  # complimentary offset surface distance
    H2 = H + Hoff


'''MAIN PARAMETERS CALCULATED FROM FUNDAMENTAL'''
#Hamaker constant calculated from fundamentals
if cbA132 == 1:
    cA132 = fn.fcalcA132(ve, e1, n1, e2, n2, e3, n3, T, kb, hp) #Hamaker constant (A132) (J)
    A132calc = cA132
#Acid-Base energy at minimum separation distance from fundamentals
if cbgammaAB == 1:
    cgammaAB = fn.fcalcgammaAB(g1pos, g1neg, g2pos, g2neg, g3pos, g3neg) #(gammaAB) (J/m2)
    gammaABcalc = cgammaAB
#Work of adhesion from fundamentals
if cbW132 == 1:
    cW132 = fn.fcalcW132(g1LW, g2LW, g3LW, gammaAB) #(W132) (J/m2)
    W132calc = cW132
#Contact Radius from fundamentals
if cbacont == 1:
    cacont = fn.fcalcacont(E1, v1, E2, v2, W132, a1) #(acont) (m)
    acontCALC = cacont

'''CALCULATION OF INTERACTIONS'''

#set corresponding combined Hamaker constant aproximated from coating contributions
if cbCOATED == 1:
    if VDWmode == 1:
        aproxA132 = s1A1p2p
    if VDWmode == 2:
        aproxA132 = s2A12p
    if VDWmode == 3:
        aproxA132 = s3A1p2

# Sphere - sphere geometry
if SS == 1:
     # Interactions independent of coating and rpughness (assumed)
     # Hamaker calculation
     if cbCOATED == 1:
          A132c = aproxA132  # Hamaker depending of VDWmode
     if cbCOATED == 0:
         if cbA132 == 1:  # checkbox for Hamaker calculated from fundamentals
             A132c = cA132  # Hamaker calculated from fundamentals
         else:
             A132c = A132  # Default Hamaker
     # Born interaction
     E_Born = fn.EBorn_SS(H, A132c, sigmaC, a1)
     F_Born = fn.F_Born_SS(H, A132c, sigmaC, a1)
     # Steric interaction
     E_Ste = fn.E_Ste_SS(H, lambdaSTE, gammaSTE, aSte)
     F_Ste = fn.F_Ste_SS(H, lambdaSTE, gammaSTE, aSte)
     # Smooth surface
     if Rmode == 0:
     # Van der Waals interactions
         if cbCOATED ==1: # coated systems
              if VDWmode == 1:  # coated colloid - coated collector
                   E_vDW = fn.E_vdW_SS_coated_systems(H, a1, a2, lambdavdW, T1, T2, s1A1p2p, s1A12p, s1A1p2, s1A12, VDWmode)
                   F_vDW = fn.F_vdW_SS_coated_systems(H, a1, a2, lambdavdW, T1, T2, s1A1p2p, s1A12p, s1A1p2, s1A12, VDWmode)
              if VDWmode == 2:  # colloid - coated collector
                   E_vDW = fn.E_vdW_SS_coated_systems(H, a1, a2, lambdavdW, T1, T2, 0.0, s2A12p, 0.0 , s2A12, VDWmode)
                   F_vDW = fn.F_vdW_SS_coated_systems(H, a1, a2, lambdavdW, T1, T2, 0.0, s2A12p, 0.0 , s2A12, VDWmode)
              if VDWmode == 3:  # coated colloid - collector
                   E_vDW = fn.E_vdW_SS_coated_systems(H, a1, a2, lambdavdW, T1, T2, 0.0, 0.0, s3A1p2, s3A12, VDWmode)
                   F_vDW = fn.F_vdW_SS_coated_systems(H, a1, a2, lambdavdW, T1, T2, 0.0, 0.0, s3A1p2, s3A12, VDWmode)
         else: # not coated smooth
             E_vDW = fn.E_vdW_SS_colloid_plate(H, A132, a1, a2, lambdavdW)
             F_vDW = fn.F_vdW_SS_colloid_plate(H, A132, a1, a2, lambdavdW)
         # EDL smooth
         E_EDL = fn.E_EDL_SS_colloid_plate(H, 1.0, epsilonW, k, kb, T, z, zetac, e_charge, zetap, a1, a2)
         F_EDL = fn.F_EDL_SS_colloid_plate(H, 1.0, epsilonW, k, kb, T, z, zetac, e_charge, zetap, a1, a2)
         if cbHET == 1 or cbHETUSER == 1:
             E_EDL_HET = fn.E_EDL_SS_colloid_plate(H, 1.0, epsilonW, k, kb, T, z, zetap, e_charge, zetahet, a1, a2)
             F_EDL_HET = fn.F_EDL_SS_colloid_plate(H, 1.0, epsilonW, k, kb, T, z, zetap, e_charge, zetahet, a1, a2)
         # ABL smooth
         ho = fn.calculation_ho(E_vDW, E_Born, A132, H)  # ho calculation for ABL interaction
         E_ABL = fn.E_AB_SS_colloid_plate(H,lambdaAB, a1, gammaAB, ho, a2)
         F_ABL = fn.F_AB_SS_colloid_collector(H, lambdaAB, a1, gammaAB, ho, a2)

     else: # Rmode1 = Rough Colloid rmode=2 Rough Collector Rmode=3 Rough Colloid and Collector
         # VdW rough
         E_vDW = (fn.E_vdW_SS_colloid_plate(H2, A132, a1, a2, lambdavdW)
                 + fn.E_vdW_SS_RMODE(n, H, A132, aasp, a2, lambdavdW, a1, Rmode, Nco))
         F_vDW = (fn.F_vdW_SS_colloid_plate(H2,A132, a1, a2, lambdavdW)
                 + fn.F_vdW_SS_RMODE(n, H, a2, A132, aasp, lambdavdW, a1, Rmode, Nco))
         # EDL rough
         E_EDL = (theta*fn.E_EDL_SS_colloid_plate(H2, 1.0, epsilonW, k, kb, T, z, zetap, e_charge, zetac, a1, a2)
                  + fn.E_EDL_SS_RMODE(H, a2, epsilonW, k, kb, T, z, zetap, e_charge, zetac, aasp, a1, Rmode, n, Nco))
         F_EDL = (theta*fn.F_EDL_SS_colloid_plate(H2, 1.0, epsilonW, k, kb, T, z, zetap, e_charge, zetac, a1, a2)
                  + fn.F_EDL_SS_RMODE(H, a2, epsilonW, k, kb, T, z, zetap, e_charge, zetac, aasp, a1, Rmode, n, Nco))
         if cbHET == 1 or cbHETUSER == 1:
             E_EDL_HET = (theta*fn.E_EDL_SS_colloid_plate(H2, 1.0, epsilonW, k, kb, T, z, zetap, e_charge, zetahet, a1, a2)
                          +fn.E_EDL_SS_RMODE(H, a2, epsilonW, k, kb, T, z, zetap, e_charge, zetac, aasp, a1, Rmode, n, Nco))
             F_EDL_HET = (theta*fn.F_EDL_SS_colloid_plate(H2, 1.0, epsilonW, k, kb, T, z, zetap, e_charge, zetahet, a1, a2)
                         + fn.F_EDL_SS_RMODE(H, a2, epsilonW, k, kb, T, z, zetap, e_charge, zetac, aasp, a1, Rmode, n, Nco))
         # AB rough
         ho = fn.calculation_ho(E_vDW, E_Born, A132, H)
         E_ABL = fn.E_AB_SS_RMODE(H, lambdaAB, aasp, nAB, gammaAB, ho, Rmode, a1, a2, Nco)
         F_ABL = fn.F_AB_SS_RMODE(H, lambdaAB, aasp, nAB, gammaAB, ho, Rmode, a1, a2, Nco)

# Sphere - plate geometry
if SP == 1:
     # Interactions independent of coating
     # Hamaker calculation
     if cbCOATED == 1:
         A132c = aproxA132  # Hamaker depending of VDWmode
     if cbCOATED == 0:
         if cbA132 == 1:  # checkbox for Hamaker calculated from fundamentals
             A132c = cA132  # Hamaker calculated from fundamentals
         else:
             A132c = A132  # Default Hamaker
     # Born interaction
     E_Born = fn.E_Born_SP_colloid_plate(H, A132c, sigmaC, a1)
     F_Born = fn.F_Born_SP_colloid_plate(H, A132c, sigmaC, a1)
     # Steric interaction
     E_Ste = fn.E_Ste_SP_colloid_plate(H, lambdaSTE, gammaSTE, aSte)
     F_Ste = fn.F_Ste_SP_colloid_plate(H, lambdaSTE, gammaSTE, aSte)
     # Smooth interaction
     if Rmode == 0:
         # Van der Waals interactions
         if cbCOATED == 1:
             if VDWmode == 1:  # coated colloid - coated collector
                 E_vDW = fn.E_vdW_SP_coated_systems(H, a1, lambdavdW, T1, T2, s1A1p2p, s1A12p, s1A1p2, s1A12, VDWmode)
                 F_vDW = fn.F_vdW_SP_coated_systems(H, a1, lambdavdW, T1, T2, s1A1p2p, s1A12p, s1A1p2, s1A12, VDWmode)
             elif VDWmode == 2:   # colloid - coated collector
                 E_vDW =  fn.E_vdW_SP_coated_systems(H, a1, lambdavdW, T1, T2, 0.0, s2A12p, 0.0 , s2A12, VDWmode)
                 F_vDW =  fn.F_vdW_SP_coated_systems(H, a1, lambdavdW, T1, T2, 0.0, s2A12p, 0.0 , s2A12, VDWmode)
             elif VDWmode == 3:  # coated colloid - collector
                 E_vDW =  fn.E_vdW_SP_coated_systems(H, a1, lambdavdW, T1, T2, 0.0, 0.0, s3A1p2, s3A12, VDWmode)
                 F_vDW =  fn.F_vdW_SP_coated_systems(H, a1, lambdavdW, T1, T2, 0.0, 0.0, s3A1p2, s3A12, VDWmode)
         else: # not coated smooth
             E_vDW = fn.E_vdW_SP_Colloid_Plate(H, A132, a1, lambdavdW)
             F_vDW = fn.F_vdW_SP_colloid_plate(H, A132, a1, lambdavdW)
         # EDL smooth
         E_EDL = fn.E_EDL_SP_colloid_plate(H, theta, epsilonW, k, kb, T, z, zetac, e_charge, zetap, a1)
         F_EDL = fn.F_EDL_SP_colloid_plate(H, theta, epsilonW, k, kb, T, z, zetac, e_charge, zetap, a1)
         if cbHET == 1 or cbHETUSER == 1:
             E_EDL_HET = fn.E_EDL_SP_colloid_plate(H, 1.0, epsilonW, k, kb, T, z, zetap, e_charge, zetahet, a1, a2)
             F_EDL_HET = fn.F_EDL_SP_colloid_plate(H, 1.0, epsilonW, k, kb, T, z, zetap, e_charge, zetahet, a1, a2)
         # ABL smooth
         ho = fn.calculation_ho(E_vDW, E_Born, A132, H)  # ho calculation for ABL interaction
         E_ABL = fn.E_AB_SP_colloid_plate(H, lambdaAB, a1, gammaAB, ho)
         F_ABL = fn.F_AB_SP_colloid_plate(H, lambdaAB, a1, gammaAB, ho)

     else: # Rmode1 = Rough Colloid rmode=2 Rough Collector Rmode=3 Rough Colloid and Collector
         #VdW rough
         E_vDW = (fn.E_vdW_SP_Colloid_Plate(H2, A132, a1, lambdavdW)
                 + fn.E_vdW_SP_RMODE(H, n, A132, aasp, a1, lambdavdW, Rmode, Nco))
         F_vDW = (fn.F_vdW_SP_colloid_plate(H2, A132, a1, lambdavdW)
                 + fn.F_vdW_SP_RMODE(H, n, A132, aasp, a1, lambdavdW, Rmode, Nco))
         # EDL rough
         E_EDL = (theta*fn.E_EDL_SP_colloid_plate(H2, 1, epsilonW, k, kb, T, z, zetap, e_charge, zetac, a1)
                  + fn.E_EDL_SP_RMODE(H, n, epsilonW, k, kb, T, z, zetap, e_charge, zetac, aasp, a1, Rmode, Nco))
         F_EDL = (theta*fn.F_EDL_SP_colloid_plate(H2, 1, epsilonW, k, kb, T, z, zetap, e_charge, zetac, a1)
                  + fn.F_EDL_SP_RMODE(H, n, epsilonW, k, kb, T, z, zetap, e_charge, zetac, aasp, a1, Rmode, Nco))
         if cbHET == 1 or cbHETUSER == 1:
             E_EDL_HET = (theta*fn.E_EDL_SP_colloid_plate(H2, 1.0, epsilonW, k, kb, T, z, zetap, e_charge, zetahet, a1, a2)
                          +fn.E_EDL_SP_RMODE(H, a2, epsilonW, k, kb, T, z, zetap, e_charge, zetac, aasp, a1, Rmode, n, Nco))
             F_EDL_HET = (theta*fn.F_EDL_SP_colloid_plate(H2, 1.0, epsilonW, k, kb, T, z, zetap, e_charge, zetahet, a1, a2)
                          +fn.F_EDL_SP_RMODE(H, a2, epsilonW, k, kb, T, z, zetap, e_charge, zetac, aasp, a1, Rmode, n, Nco))
         # ABL rough
         ho = fn.calculation_ho(E_vDW, E_Born, A132, H)  # ho calculation for ABL interaction
         E_ABL = fn.E_AB_SP_RMODE(H, lambdaAB, aasp, nAB, gammaAB, ho, Rmode, a1, Nco)
         F_ABL = fn.F_AB_SP_RMODE(H, lambdaAB, aasp, nAB, gammaAB, ho, Rmode, a1, Nco)


# remove insignificant values (<abs(10e-30))
tol = 1e-30
# Energy
E_vDW[abs(E_vDW) < tol] = 0
E_EDL[abs(E_EDL) < tol] = 0
E_ABL[abs(E_ABL) < tol] = 0
E_Born[abs(E_Born) < tol] = 0
E_Ste[abs(E_Ste) < tol] = 0
if cbHET == 1 or cbHETUSER == 1:
    E_EDL_HET[abs(E_EDL_HET) < tol] = 0
# Force
F_vDW[abs(F_vDW) < tol] = 0
F_EDL[abs(F_EDL) < tol] = 0
F_ABL[abs(F_ABL) < tol] = 0
F_Born[abs(F_Born) < tol] = 0
F_Ste[abs(F_Ste) < tol] = 0
if cbHET == 1 or cbHETUSER == 1:
    F_EDL_HET[abs(F_EDL_HET) < tol] = 0

# Calculate matrix for heterodomain influence
E_HET_T = np.zeros((len(H), 4))
F_HET_T = np.zeros((len(H), 4))
if cbHET == 1 or cbHETUSER == 1:
    E_EDL_HET_M = np.zeros((len(H), len(afvector)))
    F_EDL_HET_M = np.zeros((len(H), len(afvector)))

    for i in range(len(afvector)):
        #calculate combine EDL energy and force
        E_EDL_HET_M[:, i] = (1 - afvector[i])*E_EDL + afvector[i]*E_EDL_HET
        F_EDL_HET_M[:, i] = (1 - afvector[i])*F_EDL + afvector[i]*F_EDL_HET
        E_HET_T[:, i] = E_vDW.T + E_EDL_HET_M[:, i] + E_ABL.T + E_Born.T + E_Ste.T
        F_HET_T[:, i] = F_vDW.T + F_EDL_HET_M[:, i] + F_ABL.T + F_Born.T + F_Ste.T
    E_HET_T = E_HET_T * 1/kt

'''DATA FRAME CONSTRUCTION'''
E_total = E_vDW + E_EDL + E_ABL + E_Born + E_Ste
F_total = F_vDW + F_EDL + F_ABL + F_Born + F_Ste
EJ = np.array([E_vDW, E_EDL, E_ABL, E_Born, E_Ste, E_total]).T
Ekt = EJ * 1/kt
F = np.array([F_vDW, F_EDL, F_ABL, F_Born, F_Ste, F_total]).T
headlines_energy = ['H(m)', 'E_van_der_Waals', 'E_EDL', 'E_AB', 'E_Born', 'E_Steric', 'E_total']
headlines_force = ['H(m)',  'F_van_der_Waals', 'F_EDL', 'F_AB', 'F_Born', 'F_Steric', 'F_total']
#dfpy = pd.DataFrame(np.array([H.T, EJ, F, Ekt]), columns = headlines)

'''PLOT ENERGY AND FORCE VS DISTANCE'''
# set limits for y axis Ekt and force
limvekt= 1.5*abs(min(Ekt[:, 5]))
limvf = 1.5*abs(min(F[:, 5]))
# set max limit for x axis (nm)
hmaxdef = 100
# set line width for axis
lw = 2
# get separation distance in nm
Hnm = H/(1.0e-9) #Distance in nm

fig, ax = plt.subplots(1,2, figsize= [12, 6])
ax[0].plot(Hnm, Ekt[:, 0], color='b', label='van der Waals')
ax[0].plot(Hnm, Ekt[:, 1], color='r', label='EDL')
ax[0].plot(Hnm, Ekt[:, 2], color='lime', label='Acid-Base')
ax[0].plot(Hnm, Ekt[:, 3], color='magenta', label='Born')
ax[0].plot(Hnm, Ekt[:, 4], color='tab:orange', label='Steric')
ax[0].plot(Hnm, Ekt[:, 5], color='k', label='Total', linestyle='dashed')
ax[0].set_xlabel('Separation Distance (nm)')
ax[0].set_ylabel('Energy (kT)')
ax[0].set_xlim([0, hmaxdef])
ax[0].set_ylim([-limvekt, limvekt])
ax[0].legend()
ax[1].plot(Hnm, F[:, 0], color='b', label='van der Waals')
ax[1].plot(Hnm, F[:, 1], color='r', label='EDL')
ax[1].plot(Hnm, F[:, 2], color='lime', label='Acid-Base')
ax[1].plot(Hnm, F[:, 3], color='magenta', label='Born')
ax[1].plot(Hnm, F[:, 4], color='tab:orange', label='Steric')
ax[1].plot(Hnm, F[:, 5], color='k', label='Total', linestyle='dashed')
ax[1].set_xlabel('Separation Distance (nm)')
ax[1].set_ylabel('Force (N)')
ax[1].set_xlim([0, hmaxdef/5])
ax[1].set_ylim([-limvf, limvf])
ax[1].legend()
plt.show()

if cbHET == 1 or cbHETUSER == 1:
    fig, ax = plt.subplots(1, 2, figsize=[12, 6])
    ax[0].plot(Hnm, E_HET_T[:, 0], color='b', label='rhet = {0:.3e} m  AFRACT = {1:.2} ZOI'.format(rhetv[0], afvector[0]))
    ax[0].plot(Hnm, E_HET_T[:, 1], color='r', label='rhet = {0:.3e} m  AFRACT = {1:.2} ZOI'.format(rhetv[1], afvector[1]))
    ax[0].plot(Hnm, E_HET_T[:, 2], color='lime', label='rhet = {0:.3e} m  AFRACT = {1:.2} ZOI'.format(rhetv[2], afvector[2]))
    ax[0].plot(Hnm, E_HET_T[:, 3], color='magenta', label='rhet = {0:.3e} m  AFRACT = {1:.2} ZOI'.format(rhetv[3], afvector[3]))
    ax[0].plot(Hnm, Ekt[:, 5], color='k', label='Mean Field', linestyle='dashed')
    ax[0].set_xlabel('Separation Distance (nm)')
    ax[0].set_ylabel('Total Energy (kT)')
    ax[0].set_xlim([0, hmaxdef])
    ax[0].set_ylim([-limvekt, limvekt])
    ax[0].legend()
    ax[1].plot(Hnm, F_HET_T[:, 0], color='b', label='rhet = {0:.3e} m  AFRACT = {1:.2} ZOI'.format(rhetv[0], afvector[0]))
    ax[1].plot(Hnm, F_HET_T[:, 1], color='r', label='rhet = {0:.3e} m  AFRACT = {1:.2} ZOI'.format(rhetv[1], afvector[1]))
    ax[1].plot(Hnm, F_HET_T[:, 2], color='lime', label='rhet = {0:.3e} m  AFRACT = {1:.2} ZOI'.format(rhetv[2], afvector[2]))
    ax[1].plot(Hnm, F_HET_T[:, 3], color='magenta', label='rhet = {0:.3e} m  AFRACT = {1:.2} ZOI'.format(rhetv[3], afvector[3]))
    ax[1].plot(Hnm, F[:, 5], color='k', label='Mean Field', linestyle='dashed')
    ax[1].set_xlabel('Separation Distance (nm)')
    ax[1].set_ylabel('Force (N)')
    ax[1].set_xlim([0, hmaxdef / 5])
    ax[1].set_ylim([-limvf, limvf])
    ax[1].legend()
    plt.show()

'''GENERATION OF THE EXCEL DOCUMENT'''
route1 = 'D:/ALISON/EPN/MAESTRÍA METALURGIA/TESIS/xDLVO/parti_suite_results.xlsx'
par_cell = fn.fpar_out_xDLVO(
    # input parameters
    a1, a2, IS, zetac, zetap, aasp, sigmaC, T,
    lambdavdW, lambdaAB, lambdaSTE, gammaSTE, epsilonR, z, A132,
    SP, SS, Rmode, VDWmode,
    #  vdw from fundamentals
    ve, e1, n1, e2, n2, e3, n3, A132calc,
    # vdw coated systems
    T1, T2, A33,  # coating thickness and fluid Hamaker
    A12, A12p, A13, A1p2, A1p2p, A1p3, A23, A2p3,  # combined Hamaker
    A12c, A12pc, A13c, A1p2c, A1p2pc, A1p3c, A23c, A2p3c,  # combined Hamaker calculated
    A11, A1p1p, A22, A2p2p,  # single materials Hamaker
    s1A1p2p, s1A12p, s1A1p2, s1A12, s2A12p, s2A12, s3A1p2, s3A12,  # hamaker constributions
    # acid-base energy fundamentals
    g1pos, g1neg, g2pos, g2neg, g3pos, g3neg, gammaABcalc, gammaAB,
    # work of adhesion fundamentals
    g1LW, g2LW, g3LW, INDgammaAB, W132calc, W132,
    # aconr for steric fundamentals
    E1, E2, v1, v2, INDW132, Kint, acontCALC, acont,
    # checkboxes
    cbCOATED, cbA132, cbgammaAB, cbW132, cbacont,
    cb1, cb2, cb3,
    # heterogeneity
    cbHET, cbHETUSER, zetahet, rZOI)
fn.create_excel(route1, H, EJ, Ekt, F, cbHET,cbHETUSER, E_HET_T, F_HET_T, headlines_energy, headlines_force, rhetv, afvector, par_cell)



'''COMPARISON MATLAB VS PYTHON'''
# route of Excel files with matlab data
if cbHET == 0 and cbHETUSER == 0:
    if Rmode == 0:  # Smooth surface
        if cbCOATED == 0:
            if SS == 1:
                 route = 'C:/Users/Lenovo/Desktop/app/001_output_xDLVO.xls'
            if SP == 1:
                 route = 'C:/Users/Lenovo/Desktop/app/002_output_xDLVO.xls'
        else:
            if VDWmode == 1:  # coated colloid - coated collector
                if SS == 1:
                    route = 'C:/Users/Lenovo/Desktop/app/003_output_xDLVO.xls'
                if SP == 1:
                    route = 'C:/Users/Lenovo/Desktop/app/004_output_xDLVO.xls'
            if VDWmode == 2:  # colloid - coated collector
                if SS == 1:
                    route = 'C:/Users/Lenovo/Desktop/app/005_output_xDLVO.xls'
                if SP == 1:
                    route = 'C:/Users/Lenovo/Desktop/app/006_output_xDLVO.xls'
            if VDWmode == 3:  # coated colloid - collector
                if SS == 1:
                    route = 'C:/Users/Lenovo/Desktop/app/007_output_xDLVO.xls'
                if SP == 1:
                    route = 'C:/Users/Lenovo/Desktop/app/008_output_xDLVO.xls'
    if Rmode == 1:  # Rough colloid not coated
        route = 'C:/Users/Lenovo/Desktop/app/009_output_xDLVO.xls'  # SS
    if Rmode == 2:  # Rough collector not coated
        route = 'C:/Users/Lenovo/Desktop/app/0010_output_xDLVO.xls'  # SS
    if Rmode == 3:  # Rough colloid & collector not coated
        route = 'C:/Users/Lenovo/Desktop/app/0011_output_xDLVO.xls'  # SS
if cbHET == 1:
    route = 'C:/Users/Lenovo/Desktop/app/0012_output_xDLVO.xls'  # SS smooth
if cbHETUSER == 1:
    route = 'C:/Users/Lenovo/Desktop/app/0013_output_xDLVO.xls'  # SS smooth

# Dataframe data of matlab and python data
df = cm.data_frame(route, H, EJ, F, cbHET,cbHETUSER, E_HET_T, F_HET_T)
# Calculation of the percentage error
listE = df.columns.values[1:7]  # labels of python energy columns
listF = df.columns.values[7:13]  # labels of python force columns
if cbHET == 1 or cbHETUSER == 1:
    listE_HET = df.columns.values[13:17]  # labels of python heterodomain energy columns
    listF_HET = df.columns.values[17:21]  # labels of python heterodomain force columns

cm.error_p_m(df, [df.columns.values[0]], 'H')
cm.error_p_m(df, listE, 'E')
cm.error_p_m(df, listF, 'F')
if cbHET == 1 or cbHETUSER == 1:
    cm.error_p_m(df, listE_HET, 'E')
    cm.error_p_m(df, listF_HET, 'F')



