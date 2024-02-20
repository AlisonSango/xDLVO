import numpy as np
import pandas as pd

##Van der Waals INTERACTIONS
#Energy vdW_Sphere-Plate_colloid_plate (J)
def E_vdW_SP_Colloid_Plate(H, A132,a1, lambdavdW):
    #retarded Van der Waals interaction for sphere-plate geometry
    #particle deposition and agregation (chap.3, pag.49. Table 3.4, eq. 3.41)
    b=5.32
    deltaG_vdW = -A132*a1/(6*H) * (1 - b * H / lambdavdW * np.log(1 + lambdavdW /(b*H)))
    return deltaG_vdW

#Energy vdW_Sphere-Plate_coated systems(J)
def E_vdW_SP_coated_systems(H, a1, lambdavdW, T1, T2, Ac_1p_2p, Ac_1_2p, Ac_1p_2, Ac_1_2, system):
    ap = a1 - T2 #colloid core radius
    ##Types of coated systems
    if system == 1:
        #coefficient 1
        if Ac_1p_2p == 0:
            C1 = 0
        else:
            C1 = ap + T1
        #coefficient 2
        if Ac_1p_2p == 0:
            C2 = 0
        else:
            C2 = 2*ap + 2*T1
        #coefficient 3
        if Ac_1p_2p == 0:
            C3 = 0
        else:
            C3 = 2*ap + T1
        #coefficient 4
        if Ac_1p_2p == 0:
            C4 = 0
        else:
            C4 = 2*ap + 2*T1 + T2
        #coefficient 5
        if Ac_1p_2p == 0:
            C5 = 0
        else:
            C5 = T1 + T2
        #coefficient 6
        if Ac_1p_2p == 0:
            C6 = 0
        else:
            C6 = 2* ap * T1 + T2
        #Colloid coating thickness 1
        if Ac_1p_2p == 0:
            T1 = 0
        # Colloid coating thickness 2
        if Ac_1p_2p == 0:
            T2 = 0
        E_vdW_CS = -Ac_1p_2p * (1/6*(C1/H+ C1/(H+C2)+np.log(H/(H+C2)))*(lambdavdW/(lambdavdW+11.12*H)))-Ac_1_2p*(1/6 *(ap/(H+T1)+ap/(H+C3)+np.log((H+T1)/(H+C3)))* (lambdavdW/(lambdavdW+11.12*(H+T1))))-Ac_1p_2*(1/6*
           (C1/(H+T2)+C1/(H+C4)+np.log((H+T2)/(H+C4)))*(lambdavdW/(lambdavdW+11.12*(H+T2))))-Ac_1_2*(1/6*(ap/(H+C5)
           +ap/(H+C6)+np.log((H+C5)/(H+C6)))*(lambdavdW/(lambdavdW+11.12*(H + C5))))
    if system == 2:
        if Ac_1_2 == 0:
            T2=0
        #Coefficient 1
        if Ac_1_2 == 0:
            C1=0
        else:
            C1 = ap * 2
        # Coefficient 2
        if Ac_1_2 == 0:
            C2 = 0
        else:
            C2 = ap * 2 + T2
        E_vdW_CS = -Ac_1_2p*(1/6*(ap/H+ap/(H+C1)+np.log(H/(H+C1)))*(lambdavdW/(lambdavdW+11.12*H)))-Ac_1_2*(1/6*(ap/(H+T2)+ap/(H+C2)+np.log((H +T2)/(H+C2)))*(lambdavdW/(lambdavdW+11.12*(H + T2))))
    if system == 3:
        if Ac_1p_2 == 0:
            C1 = 0
        else:
            C1 = ap + T1
        if Ac_1p_2 ==0:
            C2 = 0
        else:
            C2 = ap*2+T1*2
        if Ac_1p_2 == 0:
            C3 = 0
        else:
            C3 = 2*ap +T1
        E_vdW_CS = -Ac_1p_2*(1/6*(C1/H+C1/(H+C2)+np.log(H/(H+C2)))*(lambdavdW/(lambdavdW+11.12*H)))-Ac_1_2*(1/6*(ap/(H+T1)+ap/(H+C3)+np.log((H+T1)/(H + C3)))*(lambdavdW/(lambdavdW+11.12*(H+T1))))
    return E_vdW_CS

#Energy vdW_Sphere-Plate_RMODE (J)
def E_vdW_SP_RMODE(H,n,A132,aasp,a1,lambdavdW,RMODE,Nco):
    b=5.32 #appropiate for sphere-plate interaction
    if RMODE==1: #ASPERITIES ON COLLOID
        #a1=n*aasp
        deltaGvdW= (n*-A132*aasp*H**-1/6)*(1-b*H/lambdavdW*np.log(1+lambdavdW*H**-1/b))

    if RMODE==2: #ASPERITIES ON COLLECTOR
        #a1=a1
        deltaGvdW= n*H**-1*(-A132*a1*aasp/6/(a1+aasp))*(1-(b*H*np.log(1+lambdavdW*H**-1/b))/lambdavdW)

    if RMODE==3: #ASPERITIES ON BOTH SURFACES
        #a1=aasp (compare with the function above)
        deltaGvdW= Nco*n*H**-1*(-A132*aasp*aasp/6/(aasp+aasp))*(1-(b*H*np.log(1+lambdavdW*H**-1/b))/lambdavdW)

    #make zero Energy values calculated for H>aasp
    #(comply with Dejarguin aproximation)
    c=[H>aasp]
    deltaGvdW[c]=0.0
    return deltaGvdW

#Energy vdW_Sphere-sphere_colloid_plate (J)
def E_vdW_SS_colloid_plate(H, A132,a1, a2, lambdavdW):
    # retarded Van der Waals interaction for sphere-sphere geometry
    # particle deposition and agregation (chap.3, pag.49. Table 3.4, eq. 3.40)
    b = 5.32 #can be used or optimized for sphere - sphere interaction
    deltaG_vdW = -A132*a1*a2/(6*H*(a1+a2))*(1- b * H /lambdavdW * np.log(1 + lambdavdW /(b*H)))
    return deltaG_vdW

#Energy vdW_Sphere - Sphere_coated systems(J)
def E_vdW_SS_coated_systems(H, a1, a2, lambdavdW, T1, T2, Ac_1p_2p, Ac_1_2p, Ac_1p_2, Ac_1_2, system):
    ap = a1 - T1 #colloid core radius
    ac = a2 - T2 #collector core radius
    #types of coated systems
    if system == 1: # coated_colloid-coated_collector
        #Coefficient 1
        if Ac_1p_2p == 0:
            C1 = 0
        else:
            C1 = ap + T1
        #coefficient 2
        if Ac_1p_2p == 0:
            C2 = 0
        else:
            C2 = ac + T2
        #coefficient 3
        if Ac_1p_2p == 0:
            C3 = 0
        else:
            C3 = ap + ac + T1 + T2
        #Coefficient 4
        if Ac_1p_2p == 0:
            C4 = 0
        else:
            C4 = ap + ac + T2
        #Coefficient 5
        if Ac_1p_2p == 0:
            C5 = 0
        else:
            C5 = ap + ac + T1
        #Coefficient 6
        if Ac_1p_2p == 0:
            C6 = 0
        else:
            C6 = T1 + T2
        #Coefficient 7
        if Ac_1p_2p == 0:
            C7 = 0
        else:
            C7 = ap + ac
        E_vdW_CS = -Ac_1p_2p*(1/6*(2*C1*C2/(H**2+2*H*C3)+2*C1*C2/(H**2+2*H*C3+4*C1*C2)+np.log((H**2+2*H*C3)
                /(H**2+2*H*C3+4*C1*C2)))*(lambdavdW/(lambdavdW+11.12*H)))-Ac_1_2p*(1/6*(2*(a1-T1)*C2/((H+T1)**2
                +2*(H+T1)*C4)+2*(a1-T1)*C2/((H+T1)**2+2*(H+T1)*C4+4*(a1-T1)*C2)+np.log(((H+T1)**2+2*(H+T1)*C4)/((H+T1)**2
                +2*(H+T1)*C4+4*(a1-T1)*C2)))*(lambdavdW/(lambdavdW+11.12*(H+T1))))-Ac_1p_2*(1/6*(4*C1*(a2-T2)/((H+T2)**2
                +2*(H+T2)*C5)+2*C1*(a2-T2)/((H+T2)**2+2*(H+T2)*C5+4*C1*(a2-T2))+np.log(((H+T2)**2+2*(H+T2)*C5)/((H+T2)**2
                +2*(H+T2)*C5+4*(a2-T2)*C1)))*(lambdavdW/(lambdavdW+11.12*(H+T2))))-Ac_1_2*(1/6*(2*(a1-T1)*(a2-T2)
                /((H+T1+T2)**2+2*(H+T1+T2)*C7)+2*(a1-T1)*(a2-T2)/((H+T1+T2)**2+2*(H+T1+T2)*C7+4*(a1-T1)*(a2-T2))
                +np.log(((H+T1+T2)**2+2*(H+T1+T2)*C7)/((H+T1+T2)**2+2*(H+T1+T2)*C7+4*(a1-T1)*(a2-T2))))*(lambdavdW/(lambdavdW
                + 11.12*(H+T1+T2))))
    if system == 2: #Colloid - Layered Collector
        if Ac_1_2 == 0:
            T2 = 0
        # Coefficient 1
        if Ac_1_2p == 0:
            C1 = 0
        else:
            C1 = (a2-T2) + T2 #CHECK THIS REDUNDANCY IN EXCEL FILE
        #coefficient 2
        if Ac_1_2p == 0:
            C2 = 0
        else:
            C2 = a1 + a2 - T2 + T2 #CHECK THIS REDUNDANCY IN EXCEL FILE
        #coefficient 3
        if Ac_1_2p == 0:
            C3 = 0
        else:
            C3 = a1 + a2 - T2
        E_vdW_CS = -Ac_1_2p*(1/6*(2*a1*C1/(H**2+2*H*C2)+2*a1*C1/(H**2+2*H*C2+4*a1*C1)+np.log((H**2+2*H*C2)/(H**2+2*H*C2+4*a1*C1)))
                *(C1/(C1+11.12*H)))+Ac_1_2*(1/6*(2*a1*(a2-T2)/((H+T2)**2+2*(H+T2)*C3)+2*a1*(a2-T2)/((H+T2)**2+2*(H+T2)*C3
                +4*a1*(a2-T2))+np.log(((H+T2)**2+2*(H+T2)*C3)/((H+T2)**2+2*(H+T2)*C3+4*a1*(a2-T2))))*(C1/(C1+11.12*(H+T2))))
    if system == 3: #coated Colloid - Collector
        if Ac_1p_2 == 0:
            T1 = 0
        #Coefficient 1
        if Ac_1p_2 == 0:
            C1 = 0
        else:
            C1 = a1 - T1 + T1
        #Coefficient 2
        if Ac_1p_2 == 0:
            C2 = 0
        else:
            C2 = a1 + a2 - T1 + T1
        #Coefficient 3
        if Ac_1p_2 == 0:
            C3 = 0
        else:
            C3 = a1 + a2 - T1

        E_vdW_CS =-Ac_1p_2*(1/6*(2*C1*a2/(H**2+2*H*C2)+2*C1*a2/(H**2+2*H*C2+4*C1*a2)+np.log((H**2+2*H*C2)/(H**2+2*H*C2+4*C1*a2)))
                *(C1/(C1+11.12*H)))-Ac_1_2*(1/6*(2*a2*(a1-T1)/((H+T1)**2+2*(H+T1)*C3)+2*a2*(C1-T1)/((H+T1)**2+2*(H+T1)*C3
                +4*a2*(a1-T1))+np.log(((H+T1)**2+2*(H+T1)*C3)/((H+T1)**2+2*(H+T1)*C3+4*a2*(a1-T1))))*(C1/(C1+11.12*(H+T1))))
    return E_vdW_CS

#Energy vdW_Sphere-sphere_RMODE (J)
def E_vdW_SS_RMODE(n,H,A132,aasp,a2,lambdavdW,a1,RMODE,Nco):
    b=5.32  #appropiate for sphere-plate interaction
    if RMODE == 1:   #ASPERITIES ON COLLOID
        deltaGvdW=-n*A132*aasp*a2*H**-1/(6*(aasp+a2))*(1-b*H/lambdavdW*np.log(1+lambdavdW*H**-1/b))

    if RMODE == 2:  #ASPERITIES ON COLLECTOR
        deltaGvdW=n*H**-1*(-A132*a1*aasp/6/(a1+aasp))*(1-(b*H*np.log(1+lambdavdW*H**-1/b))/lambdavdW)

    if RMODE == 3:  #ASPERITIES ON BOTH SURFACES
        deltaGvdW=Nco*n*H**-1*(-A132*aasp*aasp/6/(aasp+aasp))*(1-(b*H*np.log(1+lambdavdW*H**-1/b))/lambdavdW)

    # make zero Energy values calculated for H>aasp
    #(comply with Dejarguin aproximation)
    c = H > aasp
    deltaGvdW[c]=0.0
    return deltaGvdW

#Force vdW_Sphere-Plate_colloid_plate (N)
def F_vdW_SP_colloid_plate(H,A132,a1,lambdavdW):
    b=5.32 #appropiate for sphere-plate interaction
    ForcevdW = -A132*a1*H**-2/6*(lambdavdW/(lambdavdW+b*H))
    return ForcevdW

#Force vdW_Sphere - Plate_coated systems(N)
def F_vdW_SP_coated_systems(H, a1, lambdavdW, T1, T2, Ac_1p_2p, Ac_1_2p, Ac_1p_2, Ac_1_2, system):
    ap = a1 - T2 #colloid core radius
    #TYPES OF COATED SYSTEM
    if system == 1: #Layered_colloid_Layered_collector
        # #Coefficient 1
        if Ac_1p_2p == 0:
            C1 = 0
        else:
            C1 = ap + T1
        #coefficient 2
        if Ac_1p_2p == 0:
            C2 = 0
        else:
            C2 = 2 * ap + 2 * T1
        #coefficient 3
        if Ac_1p_2p == 0:
            C3 = 0
        else:
            C3 = 2 * ap + T1
        #Coefficient 4
        if Ac_1p_2p == 0:
            C4 = 0
        else:
            C4 = 2 * ap + 2 * T1 + T2
        #Coefficient 5
        if Ac_1p_2p == 0:
            C5 = 0
        else:
            C5 = T1 + T2
        #Coefficient 6
        if Ac_1p_2p == 0:
            C6 = 0
        else:
            C6 = 2 * ap + T1 + T2
        #Colloid coating thickness 1
        if Ac_1p_2p == 0:
            T1 = 0
        #Colloid coating thickness 2
        if Ac_1p_2p == 0:
            T2 = 0

        F_vdW_CS = (Ac_1p_2p*(-1/6*(lambdavdW/(lambdavdW+11.12*H)*(C1/H**2-1/H+C1/(H+C2)**2+1/(H+C2))+11.12*lambdavdW
                /(lambdavdW+11.12*H)**2*(C1/H+C1/(H+C2)+np.log(H/(H+C2)))))+Ac_1_2p*(-1/6*(lambdavdW/(lambdavdW+11.12*(H+T1))
                *(ap/(H+T1)**2-1/(H+T1)+ap/(H+C3)**2+1/(H+C3))+11.12*lambdavdW/(lambdavdW+11.12*(H+T1))**2*(ap/(H+T1)+ap
                /(H+C3)+np.log((H+T1)/(H+C3)))))+Ac_1p_2*(-1/6*(lambdavdW/(lambdavdW+11.12*(H+T2))*(C1/(H+T2)**2-1/(H+T2)+C1
                /(H+C4)**2+1/(H+C4))+11.12*lambdavdW/(lambdavdW+11.12*(H+T2))**2*(C1/(H+T2)+C1/(H+C4)+np.log((H+T2)/(H+C4)))))
                +Ac_1_2*(-1/6*(lambdavdW/(lambdavdW+11.12*(H+C5))*(ap/(H+C5)**2-1/(H+C5)+ap/(H+C5)**2+1/(H+C6))+11.12*lambdavdW
                /(lambdavdW+11.12*(H+C5))**2*(ap/(H+C5)+ap/(H+C6)+np.log((H+C5)/(H+C6))))))

    if system == 2:
        if Ac_1_2 == 0:
            T2 = 0
        #Coefficient 1
        if Ac_1_2 == 0:
            C1 = 0
        else:
            C1 = ap * 2
        #coefficient 2
        if Ac_1_2 == 0:
            C2 = 0
        else:
            C2 = ap * 2 + T2

        F_vdW_CS=Ac_1_2p*(-1/6*(lambdavdW/(lambdavdW+11.12*H)*(ap/H**2-1/H+ap/(H+C1)**2+1/(H+C1))+11.12*lambdavdW/
            (lambdavdW+11.12*H)**2*(ap/H+ap/(H+C1)+np.log(H/(H+C1)))))+Ac_1_2*(-1/6*(lambdavdW/(lambdavdW+11.12*(H+T2))*
            (ap/(H+T2)**2-1/(H+T2)+ap/(H+C2)**2+1/(H+C2))+11.12*lambdavdW/(lambdavdW+11.12*(H+T2))**2*(ap/(H+T2)+ap/(H+C2)
            +np.log((H+T2)/(H+C2)))))

    if system == 3:
        if Ac_1p_2 == 0:
            C1 = 0
        else:
            C1 = ap + T1
        if Ac_1p_2 == 0:
            C2 = 0
        else:
            C2 = ap * 2 + T1 * 2
        if Ac_1p_2 == 0:
            C3 = 0
        else:
            C3 = 2 * ap + T1

        F_vdW_CS=Ac_1p_2*(-1/6*(lambdavdW/(lambdavdW+11.12*H)*(C1/H**2-1/H+C1/(H+C2)**2+1/(H+C2))+11.12*lambdavdW/
            (lambdavdW+11.12*H)**2*(C1/H+C1/(H+C2)+np.log(H/(H+C2)))))+Ac_1_2*(-1/6*(lambdavdW/(lambdavdW+11.12*(H+T1))
            *(ap/(H+T1)**2-1/(H+T1)+ap/(H+C3)**2+1/(H+C3))+11.12*lambdavdW/(lambdavdW+11.12*(H+T1))**2*(ap/(H+T1)+ap
            /(H+C3)+np.log((H+T1)/(H+C3)))))
    return F_vdW_CS

#Force vdW_Sphere-Plate_RMODE (N)
def F_vdW_SP_RMODE(H,n,A132,aasp,a1,lambdavdW,RMODE,Nco):
    b=5.32 #appropiate for sphere-plate interaction
    if RMODE==1: #ASPERITIES ON COLLOID
        #a1=n*aasp
        ForcevdW=(n*-A132*aasp*H**-2/6)*(lambdavdW/(lambdavdW+H*b))

    if RMODE==2: #ASPERITIES ON COLLECTOR
        #a1=a1
        ForcevdW= n*H**-2*(-A132*a1*aasp/6/(a1+aasp))*(lambdavdW/(lambdavdW+H*b))

    if RMODE==3: #ASPERITIES ON BOTH SURFACES
        #a1=aasp
        ForcevdW= Nco*n*H**-2*(-A132*aasp*aasp/6/(aasp+aasp))*(lambdavdW/(lambdavdW+H*b))
        
    # make zero Force values calculated for H>aasp 
    #(comply with Dejarguin aproximation)
    c=H>aasp
    ForcevdW[c]=0.0
    return ForcevdW

#Force vdW_Sphere-sphere_colloid_plate (N)
def F_vdW_SS_colloid_plate(H,A132,a1,a2,lambdavdW):
    b=5.32 #can be used or optimized for sphere sphere interaction
    ForcevdW = -A132*a1*a2*H**-2/(6*(a1+a2))*(lambdavdW/(lambdavdW+b*H))
    return ForcevdW

#Force vdW_Sphere - sphere_coated systems(N)
def F_vdW_SS_coated_systems(H, a1, a2, lambdavdW, T1, T2, Ac_1p_2p, Ac_1_2p, Ac_1p_2, Ac_1_2, system):
    ap = a1 - T1 #colloid core radius
    ac = a2 - T2 #collector core radius
    ##TYPEs OF COATED SYSTEM
    
    if system == 1: # Layered_colloid_Layered_collector
        #Coefficient 1
        if Ac_1p_2p == 0:
            C1 = 0
        else:
            C1 = ap + T1
        #coefficient 2
        if Ac_1p_2p == 0:
            C2 = 0
        else:
            C2 = ac + T2
        #coefficient 3
        if Ac_1p_2p == 0:
            C3 = 0
        else:
            C3 = ap + ac + T1 + T2
        #Coefficient 4
        if Ac_1p_2p == 0:
            C4 = 0
        else:
            C4 = ap + ac + T2
        #Coefficient 5
        if Ac_1p_2p == 0:
            C5 = 0
        else:
            C5 = ap + ac + T1
        #Coefficient 6
        if Ac_1p_2p == 0:
            C6 = 0
        else:
            C6 = T1 + T2
        #Coefficient 7
        if Ac_1p_2p == 0:
            C7 = 0
        else:
            C7 = ap + ac
        
        F_vdW_CS=Ac_1p_2p*(-1/6*(lambdavdW/(lambdavdW+11.12*H)*(4*C1*C2*(H+C3)*(1/(H**2+2*H*C3)**2+1/(H**2+2*H*C3+4*C1*C2)**2)
            -2*(H+C3)*(1/(H**2+2*H*C3)-1/(H**2+2*H*C3+4*C1*C2)))+11.12*lambdavdW/((lambdavdW+11.12*H)**2)*(2*C1*C2/(H**2+2*H*C3)
            +2*C1*C2/(H**2+2*H*C3+4*C1*C2)+np.log((H**2+2*H*C3)/(H**2+2*H*C3+4*C1*C2)))))+Ac_1_2p*(-1/6*(lambdavdW
            /(lambdavdW+11.12*(H+T1))*(4*(a1-T1)*C2*(H+C3)*(1/((H+T1)**2+2*(H+T1)*C4)**2+1/((H+T1)**2+2*(H+T1)*C4+4*(a1
            -T1)*C2)**2)-2*(H+C3)*(1/((H+T1)**2+2*(H+T1)*C4)-1/((H+T1)**2+2*(H+T1)*C4+4*(a1-T1)*C2)))+11.12*lambdavdW/(lambdavdW
            +11.12*(H+T1))**2*(2*(a1-T1)*C2/((H+T1)**2+2*(H+T1)*C4)+2*(a1-T1)*C2/((H+T1)**2+2*(H+T1)*C4+4*(a1-T1)*C2)
            +np.log(((H+T1)**2+2*(H+T1)*C4)/((H+T1)**2+2*(H+T1)*C4+4*(a1-T1)*C2)))))+Ac_1p_2*(-1/6*(lambdavdW/(lambdavdW
            +11.12*(H+T2))*(4*C1*(a2-T2)*(H+C3)*(1/((H+T2)**2+2*(H+T2)*C5)**2+1/((H+T2)**2+2*(H+T2)*C5+4*(a2-T2)*C1)**2)
            -2*(H+C3)*(1/((H+T2)**2+2*(H+T2)*C5)-1/((H+T2)**2+2*(H+T2)*C5+4*(a2-T2)*C1)))+11.12*lambdavdW/(lambdavdW
            +11.12*(H+T2))**2*(2*C1*(a2-T2)/((H+T2)**2+2*(H+T2)*C5)+2*C1*(a2-T2)/((H+T2)**2+2*(H+T2)*C5+4*C1*(a2-T2))
            +np.log(((H+T2)**2+2*(H+T2)*C5)/((H+T2)**2+2*(H+T2)*C5+4*(a2-T2)*C1)))))+Ac_1_2*(-1/6*(lambdavdW/(lambdavdW
            +11.12*(H+T1+T2))*(4*(a1-T1)*(a2-T2)*(H+C3)*(1/((H+T1+T2)**2+2*(H+T1+T2)*C7)**2+1/((H+T1+T2)**2+2*(H+T1+T2)*C7
            +4*(a1-T1)*(a2-T2))**2)-2*(H+C3)*(1/((H+T1+T2)**2+2*(H+T1+T2)*C7)-1/((H+T1+T2)**2+2*(H+T1+T2)*C7+4*(a1-T1)*(a2
            -T2))))+11.12*lambdavdW/(lambdavdW+11.12*(H+T1+T2))**2*(2*(a1-T1)*(a2-T2)/((H+T1+T2)**2+2*(H+T1+T2)*C7)+2*(a1
            -T1)*(a2-T2)/((H+T1+T2)**2+2*(H+T1+T2)*C7+4*(a1-T1)*(a2-T2))+np.log(((H+T1+T2)**2+2*(H+T1+T2)*C7)/((H+T1+T2)**2
            +2*(H+T1+T2)*C7+4*(a1-T1)*(a2-T2))))))

    if system == 2: # Colloid - Layered collector
        if Ac_1_2 == 0:
            T2 = 0
        #Coefficient 1
        if Ac_1_2p == 0:
            C1 = 0
        else:
            C1 = (a2 - T2) + T2 #CHECK THIS REDUNDANCY IN EXCEL FILE
        #coefficient 2
        if Ac_1_2p == 0:
            C2 = 0
        else:
            C2 = a1 + a2 - T2 + T2 #CHECK THIS REDUNDANCY IN EXCEL FILE
        #coefficient 3
        if Ac_1_2p == 0:
            C3 = 0
        else:
            C3 = a1 + a2 - T2

        F_vdW_CS=Ac_1_2p*(-1/6*(lambdavdW/(lambdavdW+11.12*H)*(4*a1*C1*(H+C2)*(1/((H**2+2*H*C2))**2+1/(H**2+2*H*C2+4*a1*C1)**2)
            -2*(H+C2)*(1/(H**2+2*H*C2)-1/(H**2+2*H*C2+4*a1*C1)))+11.12*lambdavdW/(lambdavdW+11.12*H)**2*(2*a1*C1/(H**2+2*H*C2)
            +2*a1*C1/(H**2+2*H*C2+4*a1*C1)+np.log((H**2+2*H*C2)/(H**2+2*H*C2+4*a1*C1)))))+Ac_1_2*(-1/6*(lambdavdW/(lambdavdW+11.12*(H
            +T2))*(4*a1*(a2-T2)*(H+C2)*(1/((H+T2)**2+2*(H+T2)*C3)**2+1/((H+T2)**2+2*(H+T2)*C3+4*a1*(a2-T2))**2)-2*(H+C2)
            *(1/((H+T2)**2+2*(H+T2)*C3)-1/((H+T2)**2+2*(H+T2)*C3+4*a1*(a2-T2))))+11.12*lambdavdW/(lambdavdW+11.12*(H+T2))**2
            *(2*a1*(a2-T2)/((H+T2)**2+2*(H+T2)*C3)+2*a1*(a2-T2)/((H+T2)**2+2*(H+T2)*C3+4*a1*(a2-T2))+np.log(((H+T2)**2+2*(H+T2)*C3)
            /((H+T2)**2+2*(H+T2)*C3+4*a1*(a2-T2))))))

    if system == 3: # Layered colloid - Collector
    
        if Ac_1p_2 == 0:
            T1 = 0
        #Coefficient 1
        if Ac_1p_2 == 0:
            C1 = 0
        else:
            C1 = a1 - T1 + T1
        #Coefficient 2
        if Ac_1p_2 == 0:
            C2 = 0
        else:
            C2 = a1 + a2 - T1 + T1
        #Coefficient 3
        if Ac_1p_2 == 0:
            C3 = 0
        else:
            C3 = a1 + a2 - T1

        F_vdW_CS=Ac_1p_2*(-1/6*(lambdavdW/(lambdavdW+11.12*H)*(4*C1*a2*(H+C2)*(1/((H**2+2*H*C2))**2+1/(H**2+2*H*C2+4*C1*a2)**2)
            -2*(H+C2)*(1/(H**2+2*H*C2)-1/(H**2+2*H*C2+4*C1*a2)))+11.12*lambdavdW/(lambdavdW+11.12*H)**2*(2*C1*a2/(H**2+2*H*C2)
            +2*C1*a2/(H**2+2*H*C2+4*C1*a2)+np.log((H**2+2*H*C2)/(H**2+2*H*C2+4*C1*a2)))))+Ac_1_2*(-1/6*(lambdavdW/(lambdavdW
            +11.12*(H+T1))*(4*a2*(a1-T1)*(H+C2)*(1/((H+T1)**2+2*(H+T1)*C2)**2+1/((H+T1)**2+2*(H+T1)*C2+4*a2*(a1-T1))**2)-2*(H+C2)
            *(1/((H+T1)**2+2*(H+T1)*C2)-1/((H+T1)**2+2*(H+T1)*C2+4*a2*(a1-T1))))+11.12*lambdavdW/(lambdavdW+11.12*(H+T1))**2
            *(2*a2*(a1-T1)/((H+T1)**2+2*(H+T1)*C2)+2*a2*(lambdavdW-T1)/((H+T1)**2+2*(H+T1)*C2+4*a2*(a1-T1))+np.log(((H+T1)**2
            +2*(H+T1)*C2)/((H+T1)**2+2*(H+T1)*C2+4*a2*(a1-T1))))))
    return F_vdW_CS

#Force vdW_Sphere-Sphere_RMODE(N)
def F_vdW_SS_RMODE(n,H,a2,A132,aasp,lambdavdW,a1,RMODE,Nco):
    b=5.32 #appropiate for sphere-plate interaction
    if RMODE==1: #ASPERITIES ON COLLOID
        ForcevdW=n*(a2*-A132*aasp*H**-2/(6*(aasp+a2)))*(lambdavdW/(lambdavdW+H*b))
    
    if RMODE==2: #ASPERITIES ON COLLECTOR
        ForcevdW=n*H**-2*(-A132*a1*aasp/6/(a1+aasp))*(lambdavdW/(lambdavdW+H*b))
    
    if RMODE==3: #ASPERITIES ON BOTH SURFACES
        ForcevdW=Nco*n*H**-2*(-A132*aasp*aasp/6/(aasp+aasp))*(lambdavdW/(lambdavdW+H*b))
    
    # make zero Force values calculated for H>aasp 
    #(comply with Dejarguin aproximation)
    c=H>aasp
    ForcevdW[c]=0.0
    return ForcevdW

##ELECTRIC DOUBLE LAYER INTERACTION

#Energy EDL_Sphere-Plate_colloid_plate (J)
def E_EDL_SP_colloid_plate(H,theta, epsilonW, k, kB, T, z, zeta1, e_charge, zeta2, a1):
    deltaG_EDL=(theta)*(64*np.pi*epsilonW/k*(kB*T/(z*e_charge))**2*np.tanh(z*e_charge*zeta1/(4*kB*T))*np.tanh(z*e_charge*zeta2/(4*kB*T))*((k*a1-1)*np.exp(-k*H)+(k*a1+1)*np.exp(-k*(H+2*a1))))
    return deltaG_EDL

#Energy EDL_Sphere-Plate_RMODE1 (J)
def E_EDL_SP_RMODE(H,n,eps,K,kB,T,z,zeta1,e_charge,zeta2,aasp,a1,RMODE,Nco):
    if RMODE==1:
        #a1=n*aasp
        deltaGEDL= (n*64*np.pi*eps/K*(kB*T/z/e_charge)**2*np.tanh(z*e_charge*zeta1/4/kB/T)*np.tanh(z*e_charge*zeta2/4/kB/T)*((K*aasp-1)*np.exp(-K*H)+(K*aasp+1)*np.exp(-K*(H+2*aasp))))
    
    if RMODE==2:
        #a1=a1
        deltaGEDL=n*(64*np.pi*eps*a1*aasp/(a1+aasp)*(kB*T/z/e_charge)**2*np.tanh(z*e_charge*zeta1/4/kB/T)*np.tanh(z*e_charge*zeta2/4/kB/T)*np.exp(-K*H))
    
    if RMODE==3:
        #a1=aasp
        deltaGEDL=Nco*n*(64*np.pi*eps*aasp*aasp/(aasp+aasp)*(kB*T/z/e_charge)**2*np.tanh(z*e_charge*zeta1/4/kB/T)*np.tanh(z*e_charge*zeta2/4/kB/T)*np.exp(-K*H))

    # make zero Energy values calculated for H>aasp
    #(comply with Dejarguin aproximation)
    c=H>aasp
    deltaGEDL[c]=0.0
    return deltaGEDL

#Energy EDL_Sphere-sphere_colloid_plate (J)
def E_EDL_SS_colloid_plate(H,theta, epsilonW, k, kB, T, z, zeta1, e_charge, zeta2, a1, a2):
    deltaG_EDL= theta*(64*np.pi*epsilonW*a1*a2/(a1+a2)*(kB*T/z/e_charge)**2*np.tanh(z*e_charge*zeta1/4/kB/T)*np.tanh(z*e_charge*zeta2/4/kB/T)*np.exp(-k*H))
    return deltaG_EDL

#Energy EDL_Sphere-Sphere_RMODE (J)
def E_EDL_SS_RMODE(H,a2,eps,K,kB,T,z,zeta1,e_charge,zeta2,aasp,a1,RMODE,n,Nco):
    if RMODE==1:
          deltaGEDL=n*64*np.pi*eps*aasp*a2/(aasp+a2)*(kB*T/z/e_charge)**2*np.tanh(z*e_charge*zeta1/4/kB/T)*np.tanh(z*e_charge*zeta2/4/kB/T)*np.exp(-K*H)
    
    if RMODE==2:
          deltaGEDL=n*(64*np.pi*eps*a1*aasp/(a1+aasp)*(kB*T/z/e_charge)**2*np.tanh(z*e_charge*zeta1/4/kB/T)*np.tanh(z*e_charge*zeta2/4/kB/T)*np.exp(-K*H))
    
    if RMODE==3:
          deltaGEDL=Nco*n*(64*np.pi*eps*aasp*aasp/(aasp+aasp)*(kB*T/z/e_charge)**2*np.tanh(z*e_charge*zeta1/4/kB/T)*np.tanh(z*e_charge*zeta2/4/kB/T)*np.exp(-K*H))

    # make zero Energy values calculated for H>aasp 
    #(comply with Dejarguin aproximation)
    c=H>aasp
    deltaGEDL[c]=0.0
    return deltaGEDL

#Force EDL_Sphere-Plate_colloid_plate (N)
def F_EDL_SP_colloid_plate (H, theta,eps,k,kB,T,z,zeta1, e_charge, zeta2,a1):
    ForceEDL=(theta)*(64*np.pi*eps*(kB*T/z/e_charge)**2*np.tanh(z*e_charge*zeta1/4/kB/T)*np.tanh(z*e_charge*zeta2/4/kB/T)*((k*a1-1)*np.exp(-k*H)+(k*a1+1)*np.exp(-k*(H+2*a1))))
    return ForceEDL

#Force EDL_Sphere-Plate_RMODE(N)
def F_EDL_SP_RMODE(H,n,eps,K,kB,T,z,zeta1,e_charge,zeta2,aasp,a1,RMODE,Nco):
    if RMODE==1:
        #a1=n*aasp
        F_EDL= n*64*np.pi*eps*(kB*T/z/e_charge)**2*np.tanh(z*e_charge*zeta1/4/kB/T)*np.tanh(z*e_charge*zeta2/4/kB/T)*((K*aasp-1)*np.exp(-K*H)+(K*aasp+1)*np.exp(-K*(H+2*aasp)))
    
    if RMODE==2:
        #a1=a1
        F_EDL= n*(64*np.pi*eps*K*a1*aasp/(a1+aasp)*(kB*T/z/e_charge)**2*np.tanh(z*e_charge*zeta1/4/kB/T)*np.tanh(z*e_charge*zeta2/4/kB/T)*np.exp(-K*H))
    
    if RMODE==3:
        #a1=aasp
        F_EDL=Nco*n*(64*np.pi*eps*K*aasp*aasp/(aasp+aasp)*(kB*T/z/e_charge)**2*np.tanh(z*e_charge*zeta1/4/kB/T)*np.tanh(z*e_charge*zeta2/4/kB/T)*np.exp(-K*H))
    
    # make zero Force values calculated for H>aasp 
    #(comply with Dejarguin aproximation)
    c=H>aasp
    F_EDL[c]=0.0
    return F_EDL
#Force EDL_Sphere-sphere_colloid_plate (N)
def F_EDL_SS_colloid_plate(H, theta, eps, k, kB, T, z, zeta1, e_charge, zeta2, a1,a2):
    ForceEDL=theta*(64*np.pi*eps*k*a1*a2/(a1+a2)*(kB*T/z/e_charge)**2*np.tanh(z*e_charge*zeta1/4/kB/T)*np.tanh(z*e_charge*zeta2/4/kB/T)*np.exp(-k*H))
    return ForceEDL

# Force EDL_Sphere-Sphere_RMODE (N)
def F_EDL_SS_RMODE(H, a2, eps, K, kB, T, z, zeta1, e_charge, zeta2, aasp, a1, RMODE, n, Nco):
    if RMODE == 1:
        ForceGEDL =n*64*np.pi*eps*K*aasp*a2/(aasp+a2)*(kB*T/z/e_charge)**2*np.tanh(z*e_charge*zeta1/4/kB/T)*np.tanh(z*e_charge*zeta2/4/kB/T)*np.exp(-K*H)

    if RMODE == 2:
        ForceGEDL=n*(64*np.pi*eps*K*a1*aasp/(a1+aasp)*(kB*T/z/e_charge)**2*np.tanh(z*e_charge*zeta1/4/kB/T)*np.tanh(z*e_charge*zeta2/4/kB/T)*np.exp(-K*H))

    if RMODE == 3:
        ForceGEDL=Nco*n*(64*np.pi*eps*K*aasp*aasp/(aasp+aasp)*(kB*T/z/e_charge)**2*np.tanh(z*e_charge*zeta1/4/kB/T)*np.tanh(z*e_charge*zeta2/4/kB/T)*np.exp(-K*H))

    # make zero Force values calculated for H>aasp
    # (comply with Dejarguin aproximation)
    c=H>aasp
    ForceGEDL[c]=0.0
    return ForceGEDL

##Born INTERACTIONS

#Energy Born_Sphere-Plate_colloid_plate (J)
def E_Born_SP_colloid_plate (H, A132, sigmaC,a1):
    deltaG_Born= (abs(A132)*sigmaC**6/7560)*((6*a1-H)*H**-7+(8*a1+H)/(2*a1+H)**7)
    return deltaG_Born

#Energy Born_Sphere-Sphere(J)
def EBorn_SS (H,A132, sigmaC, a1):
    deltaG_Born= abs(A132)*sigmaC**6/7560*((6*a1-H)/H**7+(8*a1+H)/(2*a1+H)**7)
    return deltaG_Born

#Force Born_Sphere-Plate_colloid_plate (N)
def F_Born_SP_colloid_plate(H, A132,sigmaC,a1):
    ForceBorn=(abs(A132)*sigmaC**6/1260)*((7*a1-H)*H**-8+(9*a1+H)/(2*a1+H)**8)
    return ForceBorn

#Force Born_Sphere-Sphere (N)
def F_Born_SS(H,A132,sigmaC,a1):
    ForceBorn=(abs(A132)*sigmaC**6/1260)*((7*a1-H)*H**-8+(9*a1+H)/(2*a1+H)**8)
    return ForceBorn

##ACID-BASE LEWIS INTERACTIONS

#determine ho for minimum (Eborn+Evdw) Energy. Minimum separation distance in contact (m)
def calculation_ho (E_vDW, E_Born, A132, H):

    E_sum = E_Born + E_vDW
    imin = np.where(E_sum == min(E_sum))
    if A132 > 0:
        ho = H[imin]
    else:
        ho = 1.58e-10  # Minimum separation distance, generally accepted to be 1.58 amstrongs (in vacuum Israelachvili)
    return ho

#Energy AB_Sphere-Plate_colloid_plate (J)
def E_AB_SP_colloid_plate(H, lambdaAB,a1,gammaoAB, ho):
    deltaGAB=(1-lambdaAB/a1+(1+lambdaAB/a1)*np.exp(-2*a1/lambdaAB))*2*np.pi*a1*lambdaAB*gammaoAB*np.exp(-(H-ho)/lambdaAB)
    return deltaGAB

#Energy AB_Sphere - Plate_RMODE1(J)
def E_AB_SP_RMODE(H, lambdaAB, aasp, nAB, gammaoAB, ho, RMODE, a1, Nco):
    if RMODE == 1:
        deltaGAB = (nAB*(1-lambdaAB/aasp+(1+lambdaAB/aasp)*np.exp(-2*aasp/lambdaAB))*2*np.pi*aasp*lambdaAB*gammaoAB*np.exp(-(H-ho)/lambdaAB))

    if RMODE == 2:
        aeff=2*aasp*a1/(aasp+a1) #[m] effective radius
        #Corecction factor
        correc_factor=(1-lambdaAB/aeff+lambdaAB**2/(2*aeff**2)-4*aeff/(3*lambdaAB)*np.exp(-2*aeff/lambdaAB)-(1+lambdaAB/aeff+lambdaAB**2/(2*aeff**2))
                     *np.exp(-4*aeff/lambdaAB))
        deltaGAB=nAB*correc_factor*np.pi*aeff*lambdaAB*gammaoAB*np.exp(-(H-ho)/lambdaAB)

    if RMODE == 3:
        aeff=2*aasp*aasp/(aasp+aasp) #[m] effective radius
        #Corecction factor
        correc_factor =(1-lambdaAB/aeff+lambdaAB**2/(2*aeff**2)-4*aeff/(3*lambdaAB)*np.exp(-2*aeff/lambdaAB)-(1+lambdaAB/aeff+lambdaAB**2/(2*aeff**2))
                        *np.exp(-4*aeff/lambdaAB))
        deltaGAB = Nco*nAB*correc_factor*np.pi*aeff*lambdaAB*gammaoAB*np.exp(-(H -ho)/lambdaAB)

    #make zero Energy values calculated for H> aasp
    #(comply with Dejarguin aproximation)
    c=H>aasp
    deltaGAB[c] = 0.0
    return deltaGAB

#Energy AB_Sphere-Sphere_colloid_collector (J)
def E_AB_SS_colloid_plate(H,lambdaAB,a1,gammaoAB,ho,a2):
    aeff = 2 * a1 * a2 / (a1 + a2)
    #Bounds on geometric Correction
    Lower=(1-lambdaAB/aeff+(1+lambdaAB/aeff)*np.exp(-2*aeff/lambdaAB))
    Upper=(1-lambdaAB/aeff+lambdaAB**2/(2*aeff**2)-4*aeff/(3*lambdaAB)*np.exp(-2*aeff/lambdaAB)-(1+lambdaAB/aeff+lambdaAB**2/(2*aeff**2))*np.exp(-4*aeff/lambdaAB))
    deltaGAB=((1-a1/a2)*Lower+a1/a2*Upper)*np.pi*aeff*lambdaAB*gammaoAB*np.exp(-(H-ho)/lambdaAB)
    return deltaGAB

#Energy AB_Sphere-Sphere_RMODE1 (J)
def E_AB_SS_RMODE(H,lambdaAB,aasp,nAB,gammaoAB,ho,RMODE,a1,a2,Nco):
    if RMODE==1:
        aeff=2*aasp*a2/(aasp+a2) #Effective radius for RMODE1
        #Corrections_RMODE1
        Lower=(1-lambdaAB/aeff+(1+lambdaAB/aeff)*np.exp(-2*aeff/lambdaAB))
        Upper=(1-lambdaAB/aeff+lambdaAB**2/(2*aeff**2)-4*aeff/(3*lambdaAB)*np.exp(-2*aeff/lambdaAB)-(1+lambdaAB/aeff+lambdaAB**2/(2*aeff**2))*np.exp(-4*aeff/lambdaAB))
        # Main function RMODE1
        deltaGAB=nAB*((1-aasp/a2)*Lower+aasp/a2*Upper)*np.pi*aeff*lambdaAB*gammaoAB*np.exp(-(H-ho)/lambdaAB)
    
    if RMODE==2:
        aeff=2*a1*aasp/(a1+aasp)#[m]Effective radius for RMODE2
        #Corrections_RMODE2
        correc_factor=(1-lambdaAB/aeff+lambdaAB**2/(2*aeff**2)-4*aeff/(3*lambdaAB)*np.exp(-2*aeff/lambdaAB)-(1+lambdaAB/aeff+lambdaAB**2/(2*aeff**2))*np.exp(-4*aeff/lambdaAB))
         #Main function RMODE2
        deltaGAB=nAB*correc_factor*np.pi*aeff*lambdaAB*gammaoAB*np.exp(-(H-ho)/lambdaAB)
    
    if RMODE==3:
        aeff=2*aasp*aasp/(aasp+aasp)#Effective radius for RMODE3 
        #Corrections_RMODE3
        correc_factor=(1-lambdaAB/aeff+lambdaAB**2/(2*aeff**2)-4*aeff/(3*lambdaAB)*np.exp(-2*aeff/lambdaAB)-(1+lambdaAB/aeff+lambdaAB**2/(2*aeff**2))*np.exp(-4*aeff/lambdaAB))
        # Main function RMODE3
        deltaGAB=Nco*nAB*correc_factor*np.pi*aeff*lambdaAB*gammaoAB*np.exp(-(H-ho)/lambdaAB)

    # make zero Energy values calculated for H>aasp 
    #(comply with Dejarguin aproximation)
    c=H>aasp
    deltaGAB[c]=0.0
    return deltaGAB

#Force AB_Sphere-Plate_colloid_plate (N)
def F_AB_SP_colloid_plate(H,lambdaAB,a1,gammaoAB,ho):
    ForceAB = (1-lambdaAB/a1+(1+lambdaAB/a1)*np.exp(-2*a1/lambdaAB))*2*np.pi*a1*gammaoAB*np.exp(-(H-ho)/lambdaAB)
    return ForceAB

#Force AB_Sphere-Plate_RMODE(J)
def F_AB_SP_RMODE(H, lambdaAB, aasp, nAB, gammaoAB, ho, RMODE, a1, Nco):
    if RMODE == 1:
        F_AB=nAB*(1-lambdaAB/aasp+(1+lambdaAB/aasp)*np.exp(-2*aasp/lambdaAB))*2*np.pi*aasp*gammaoAB*np.exp(-(H-ho)/lambdaAB)

    if RMODE == 2:
        aeff=2*aasp*a1/(aasp+a1) ##[m] effective radius
        #Corecction factor
        correc_factor=(1-lambdaAB/aeff+lambdaAB**2/(2*aeff**2)-4*aeff/(3*lambdaAB)*np.exp(-2*aeff/lambdaAB)
                       -(1+lambdaAB/aeff+lambdaAB**2/(2*aeff**2))*np.exp(-4*aeff/lambdaAB))
        F_AB=nAB*correc_factor*np.pi*aeff*gammaoAB*np.exp(-(H-ho)/lambdaAB)

    if RMODE == 3:
        aeff=2*aasp*aasp/(aasp+aasp)#[m] effective radius
        #Corecction factor
        correc_factor=(1-lambdaAB/aeff+lambdaAB**2/(2*aeff**2)-4*aeff/(3*lambdaAB)*np.exp(-2*aeff/lambdaAB)
                   -(1+lambdaAB/aeff+lambdaAB**2/(2*aeff**2))*np.exp(-4*aeff/lambdaAB))
        F_AB=Nco*nAB*correc_factor*np.pi*aeff*gammaoAB*np.exp(-(H-ho)/lambdaAB)

    #make zero Force values calculated for H>aasp
    #(comply with Dejarguin aproximation)
    c=H>aasp
    F_AB[c]=0.0
    return F_AB

#Force AB_Sphere-Sphere_colloid_collector (N)
def F_AB_SS_colloid_collector(H,lambdaAB,a1,gammaoAB,ho,a2):
    aeff=2*a1*a2/(a1+a2)
    #Bounds on geometric Correction
    Lower=(1-lambdaAB/aeff+(1+lambdaAB/aeff)*np.exp(-2*aeff/lambdaAB))
    Upper=(1-lambdaAB/aeff+lambdaAB**2/(2*aeff**2)-4*aeff/(3*lambdaAB)*np.exp(-2*aeff/lambdaAB)-(1+lambdaAB/aeff+lambdaAB**2/(2*aeff**2))*np.exp(-4*aeff/lambdaAB))
    ForceGAB=((1-a1/a2)*Lower+a1/a2*Upper)*np.pi*aeff*gammaoAB*np.exp(-(H-ho)/lambdaAB)
    return ForceGAB

#Energy AB_Sphere-Sphere_RMODE1 (J)
def F_AB_SS_RMODE(H,lambdaAB,aasp,nAB,gammaoAB,ho,RMODE,a1,a2,Nco): #correc_factor_2,correc_factor_3
    if RMODE==1:
        aeff=2*aasp*a2/(aasp+a2)#Effective radius for RMODE1
        #Corrections_RMODE1
        Lower=(1-lambdaAB/aeff+(1+lambdaAB/aeff)*np.exp(-2*aeff/lambdaAB))
        Upper=(1-lambdaAB/aeff+lambdaAB**2/(2*aeff**2)-4*aeff/(3*lambdaAB)*np.exp(-2*aeff/lambdaAB)-
               (1+lambdaAB/aeff+lambdaAB**2/(2*aeff**2))*np.exp(-4*aeff/lambdaAB))
        # Main function RMODE1
        ForceGAB=nAB*((1-aasp/a2)*Lower+aasp/a2*Upper)*np.pi*aeff*gammaoAB*np.exp(-(H-ho)/lambdaAB)
    
    if RMODE==2:
        aeff=2*a1*aasp/(a1+aasp)#[m]Effective radius for RMODE2
        #Corrections_RMODE2
        correc_factor=(1-lambdaAB/aeff+lambdaAB**2/(2*aeff**2)-4*aeff/(3*lambdaAB)*np.exp(-2*aeff/lambdaAB)
                       -(1+lambdaAB/aeff+lambdaAB**2/(2*aeff**2))*np.exp(-4*aeff/lambdaAB))
         #Main function RMODE2
        ForceGAB=nAB*correc_factor*np.pi*aeff*gammaoAB*np.exp(-(H-ho)/lambdaAB)
    
    if RMODE==3:
        aeff=2*aasp*aasp/(aasp+aasp)#Effective radius for RMODE3
        #Corrections_RMODe3
        correc_factor=(1-lambdaAB/aeff+lambdaAB**2/(2*aeff**2)-4*aeff/(3*lambdaAB)*np.exp(-2*aeff/lambdaAB)
                       -(1+lambdaAB/aeff+lambdaAB**2/(2*aeff**2))*np.exp(-4*aeff/lambdaAB))
        # Main function RMODE
        ForceGAB=Nco*nAB*correc_factor*np.pi*aeff*gammaoAB*np.exp(-(H-ho)/lambdaAB)

    # make zero Force values calculated for H>aasp
    #(comply with Dejarguin aproximation)
    c=H>aasp
    ForceGAB[c]=0.0
    return ForceGAB

##STERIC INTERACTIONS
#Energy Steric_Sphere-Plate_colloid_plate (J)
def E_Ste_SP_colloid_plate (H,lambdaSte,gammaoSte,aSte):
    deltaGSte = gammaoSte * np.exp(-H/lambdaSte) * np.pi * aSte**2
    return deltaGSte

# Energy Steric_Sphere-Sphere(J)
def E_Ste_SS (H,lambdaSte,gammaoSte,aSte):
    deltaGSte = gammaoSte*np.exp(-H/lambdaSte)*np.pi*aSte**2
    return deltaGSte

#Force Ste_Sphere-Plate_colloid_plate (N)
def F_Ste_SP_colloid_plate(H,lambdaSte,gammaoSte,aSte):
    ForceSte = gammaoSte/lambdaSte*np.exp(-H/lambdaSte)*np.pi*aSte**2
    return ForceSte

#Force Ste_Sphere-Sphere(N)
def F_Ste_SS(H,lambdaSte,gammaoSte,aSte):
    ForceSte = gammaoSte/lambdaSte*np.exp(-H/lambdaSte)*np.pi*aSte**2
    return ForceSte

#Hamaker constant calculated from fundamentals
def fcalcA132 (ve, e1, n1, e2, n2, e3, n3, T, kb, hp):
    s2 = 2**0.5
    cA132=((3/4)*kb*T*(e1-e3)/(e1+e3)*(e2-e3)/(e2+e3)+3*hp*ve/8/s2*(n1**2-n3**2)*(n2**2-n3**2)/np.sqrt(n1**2+n3**2)
           /np.sqrt(n2**2+n3**2)/(np.sqrt(n1**2+n3**2)+np.sqrt(n2**2+n3**2)))
    return cA132

#Acid-Base energy at minimum separation distance (gammaAB) (J/m2) from fundamentals
def fcalcgammaAB (g1pos, g1neg, g2pos, g2neg, g3pos, g3neg):
    cgammaAB = 2*(np.sqrt(g3pos)*(np.sqrt(g1neg)+np.sqrt(g2neg)-np.sqrt(g3neg))+np.sqrt(g3neg)*(np.sqrt(g1pos)
                +np.sqrt(g2pos)-np.sqrt(g3pos))-np.sqrt(g1pos*g2neg)-np.sqrt(g1neg*g2pos))
    return cgammaAB

#Work of adhesion from fundamentals
def fcalcW132 (g1LW, g2LW, g3LW, gammaAB):
    cW132=2*(np.sqrt(g1LW*g3LW)+np.sqrt(g2LW*g3LW)-np.sqrt(g1LW*g2LW)-g3LW)+gammaAB
    return cW132

#Contact Radius from fundamentals
def fcalcacont (E1, v1, E2, v2, W132, a1):
    Kint = 4/3/((1-v1**2)/E1+(1-v2**2)/E2)
    cacont=(-6*np.pi*W132*a1**2/Kint)**(1/3)
    return cacont

# First sheet of excel document
def fpar_out_xDLVO(
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
        cbHET, cbHETUSER, zetahet, rZOI):

    par_cell = [['Geometry', ' ', ' ', ' '],
                ['Sphere-Sphere', SS, ' ', ' '],
                ['Sphere-Plate', SP, ' ', ' '],
                [' ', ' ', ' ', ' '],
                ['Roughness_mode(0_smooth)(1_rough_collector)(2_rough_colloid)(3_rough_colloid_collector)', Rmode, ' ',
                 ' '],
                #[' ', ' ', ' ', ' '],
                #['Van_der_Waals_mode (1_coated_colloid-coated collector)(2_colloid-coated_collector)(3_coated_colloid-collector)',
                # VDWmode, ' ', ' '],
                [' ', ' ', ' ', ' '],
                ['Main_DLVO_Parameters', ' ', ' ', ' '],
                ['Temperature(K)', T, ' ', ' '],
                ['Ionic_strenght(mol/m3)', IS, ' ', ' '],
                ['Colloid_radius(m)', a1, ' ', ' '],
                ['Collector_radius(m)', a2, ' ', ' '],
                ['Colloid_zeta_potential(V)', zetap, ' ', ' '],
                ['Collector_zeta_potential(V)', zetac, ' ', ' '],
                ['Valence_of_the_symmetric_electrolyte(-)', z, ' ', ' '],
                ['Relativity_permitivity_of_water(-)', epsilonR, ' ', ' '],
                ['vdW_characteristic_wavelength(m)', lambdavdW, ' ', ' '],
                ['Born_collision_diameter(m)', sigmaC, ' ', ' '],
                [' ', ' ', ' ', ' '],
                ['Extended_DLVO_Parameters', ' ', ' ', ' '],
                ['Lewis_acid-base_decay_length(m)', lambdaAB, ' ', ' '],
                ['Steric_decay_length(m)', lambdaSTE, ' ', ' '],
                ['Steric_energy_at_minimum_separation_distance(J/m2)', gammaSTE, ' ', ' '],
                ['Asperity_height_above_mean_surface(m)', aasp, ' ', ' '],
                [' ', ' ', ' ', ' '],
                ['van_der_Waals', ' ', ' ', ' '],
                ['Coated_system(0=uncoated)(1=coated,see_end_of_sheet)', cbCOATED, ' ', ' '],
                ['Hamaker_constant(J)', A132, 'Calculated_from_fundamentals', cbA132],
                [' ', ' ', ' ', ' '],
                ['Acid-base_energy', ' ', ' ', ' '],
                ['Acid-base_energy_at minimum_separation_distance(J)', gammaAB, 'Calculated_from_fundamentals',
                 cbgammaAB],
                [' ', ' ', ' ', ' '],
                ['Work_of_adhesion', ' ', ' ', ' '],
                ['Work_of_adhesion(J)', W132, 'Calculated_from_fundamentals', cbW132],
                [' ', ' ', ' ', ' '],
                ['Contact_radius', ' ', ' ', ' '],
                ['Contac_radius_for_steric_interaction(m)', acont, 'Calculated_from_fundamentals', cbacont],
                [' ', ' ', ' ', ' '],
                [' ', ' ', ' ', ' '],
                ['MAIN_PARAMETERS_CALCULATED_FROM_FUNDAMENTALS', ' ', ' ', ' '],
                [' ', ' ', ' ', ' '],
                ['Hamaker_constant_parameters(uncoated_systems)', ' ', ' ', ' '],
                ['Main_electronic_absorption_frequency(s-1)', ve, ' ', ' '],
                ['Colloid_dielectric_constant(-)', e1, ' ', ' '],
                ['Colloid_refractive_index(-)', n1, ' ', ' '],
                ['Collector_dielectric_constant(-)', e2, ' ', ' '],
                ['Collector_refractive_index(-)', n2, ' ', ' '],
                ['Fluid_dielectric_constant(-)', e3, ' ', ' '],
                ['Fluid_refractive_index(-)', n3, ' ', ' '],
                ['Hamaker_constant(J)', A132calc, ' ', ' '],
                [' ', ' ', ' ', ' '],
                ['Acid-base_surface_energy_components', ' ', ' ', ' '],
                ['Colloid_electron_acceptor(J/m2)', g1pos, ' ', ' '],
                ['Colloid_electron_donor(J/m2)', g1neg, ' ', ' '],
                ['Collector_electron_acceptor(J/m2)', g2pos, ' ', ' '],
                ['Collector_electron_donor(J/m2)', g2neg, ' ', ' '],
                ['Fluid_electron_acceptor(J/m2)', g3pos, ' ', ' '],
                ['Fluid_electron_donor(J/m2)', g3neg, ' ', ' '],
                ['Acid-base_energy_at_minimum_separation(J/m2)', gammaABcalc, ' ', ' '],
                [' ', ' ', ' ', ' '],
                ['Work_of_adhesion(for_contact_area)', ' ', ' ', ' '],
                ['Colloid_van_der_Waals_free_energy(J/m2)', g1LW, ' ', ' '],
                ['Collector_van_der_Waals_free_energy(J/m2)', g2LW, ' ', ' '],
                ['Fluid_van_der_Waals_free_energy(J/m2)', g3LW, ' ', ' '],
                ['Acid-base_energy_at_minimum_separation(J/m2)', INDgammaAB, ' ', ' '],
                ['Work_of_adhesion(J/m2)', W132calc, ' ', ' '],
                [' ', ' ', ' ', ' '],
                ['Contact_radius(for_steric_interaction)', ' ', ' ', ' '],
                ['Colloid_Young''s_modulus(N/m2)', E1, ' ', ' '],
                ['Collector_Young''s_modulus(N/m2)', E2, ' ', ' '],
                ['Colloid_Poisson''s ratio(-)', v1, ' ', ' '],
                ['Collector_Poisson''s ratio(-)', v2, ' ', ' '],
                ['Work_of_adhesion(J/m2)', INDW132, ' ', ' '],
                ['Combined_elastic_modulus(N/m2)', Kint, ' ', ' '],
                ['Contact_radius(m)', acontCALC, ' ', ' '],
                [' ', ' ', ' ', ' '],
                [' ', ' ', ' ', ' '],
                ['COATED_SYSTEMS_van_der_Waals_PARAMETERS', ' ', ' ', ' '],
                [' ', ' ', ' ', ' '],
                ['Type_of_coated_system', ' ', ' ', ' '],
                ['Coated_colloid-Coated_collector', cb1, ' ', ' '],
                ['Colloid-Coated_Collector', cb2, ' ', ' '],
                ['Coated_colloid-Collector', cb3, ' ', ' '],
                [' ', ' ', ' ', ' '],
                ['Coating_thickness_and_fluid_Hamaker_constant', ' ', ' ', ' '],
                ['Colloid_coating_thickness(m)', T1, ' ', ' '],
                ['Collector_coating_thickness(m)', T2, ' ', ' '],
                ['Fliud Hamaker constant', A33, ' ', ' '],
                [' ', ' ', ' ', ' '],
                ['Combined_Hamaker_constant_Coated_sytems', ' ', ' ', ' '],
                ['Colloid-collector(J)', A12, 'Calculated_from_single_material_values ', A12c],
                ['Colloid-collector_coating(J)', A12p, 'Calculated_from_single_material_values ', A12pc],
                ['Colloid-fluid(J)', A13, 'Calculated_from_single_material_values ', A13c],
                ['Colloid_coating-collector(J)', A1p2, 'Calculated_from_single_material_values ', A1p2c],
                ['Colloid_coating-collector_coating(J)', A1p2p, 'Calculated_from_single_material_values ', A1p2pc],
                ['Colloid_coating-fluid(J)', A1p3, 'Calculated_from_single_material_values ', A1p3c],
                ['Collector-fluid(J)', A23, 'Calculated_from_single_material_values ', A23c],
                ['Collector_coating-fluid(J)', A2p3, 'Calculated_from_single_material_values ', A2p3c],
                [' ', ' ', ' ', ' '],
                ['Hamaker_constants_Single_material_values', ' ', ' ', ' '],
                ['Colloid_Hamaker_constant_(J)', A11, ' ', ' '],
                ['Colloid_coating_Hamaker_constant_(J)', A1p1p, ' ', ' '],
                ['Collector_Hamaker_constant_(J)', A22, ' ', ' '],
                ['Collector_coating_Hamaker_constant_(J)', A2p2p, ' ', ' '],
                [' ', ' ', ' ', ' '],
                [' ', ' ', ' ', ' '],
                ['Hamaker_constant_contributions', ' ', ' ', ' '],
                [' ', ' ', ' ', ' '],
                ['SYSTEM_Coated_colloid-Coated_collector', ' ', ' ', ' '],
                ['Colloid_coating-Collector_coating(J)', s1A1p2p, ' ', ' '],
                ['Colloid-Collector_coating(J)', s1A12p, ' ', ' '],
                ['Colloid_coating-Collector(J)', s1A1p2, ' ', ' '],
                ['Colloid-Collector(J)', s1A12, ' ', ' '],
                [' ', ' ', ' ', ' '],
                ['SYSTEM_Colloid-Coated_collector', ' ', ' ', ' '],
                ['Colloid-Collector_coating(J)', s2A12p, ' ', ' '],
                ['Colloid-Collector(J)', s2A12, ' ', ' '],
                [' ', ' ', ' ', ' '],
                ['SYSTEM_Coated_colloid-Collector', ' ', ' ', ' '],
                ['Colloid_coating-Collector(J)', s3A1p2, ' ', ' '],
                ['Colloid-Collector(J)', s3A12, ' ', ' '],
                [' ', ' ', ' ', ' '],
                ['SYSTEM_Heterodomain_influence', ' ', ' ', ' '],
                ['Calculate_heterodomain_influence_AFRACT_fractions', cbHET, ' ', ' '],
                ['Calculate_heterodomain_influence_user_define_rhet', cbHETUSER, ' ', ' '],
                ['Heterodomain_zeta_potential(V)', zetahet, ' ', ' '],
                ['rZOI_zone_of_influence_radius(m)', rZOI, ' ', ' ']]
    return par_cell

#Excel document
def create_excel (route, H, EJ, Ekt, F, cbHET,cbHETUSER, E_HET_T, F_HET_T, headlines_energy, headlines_force, rhetv,
                  afvector, par_cell):
    # data frames for different sheets
    df_par = pd.DataFrame(par_cell)
    df_EJ = pd.DataFrame(np.column_stack((H, EJ)), columns=headlines_energy)
    df_Ekt = pd.DataFrame(np.column_stack((H, Ekt)), columns=headlines_energy)
    df_F = pd.DataFrame(np.column_stack((H, F)), columns=headlines_force)
    if cbHET == 1 or cbHETUSER == 1:
        list_rhetv = ['RHET(m)', rhetv[0], rhetv[1], rhetv[2], rhetv[3]]
        list_afvector = ['AFRACT', afvector[0], afvector[1], afvector[2], afvector[3]]
        df_header = pd.DataFrame([list_rhetv, list_afvector, ['H(m)']])
        df_E_HET = pd.concat([df_header, pd.DataFrame(np.column_stack((H.T, E_HET_T)))])
        df_F_HET = pd.concat([df_header, pd.DataFrame(np.column_stack((H.T, F_HET_T)))])
    # excel sheets
    with pd.ExcelWriter(route) as writer:
        df_par.to_excel(writer, sheet_name='Input_Parameters', index=False, header=False)
        df_EJ.to_excel(writer, sheet_name='Energy(J)', index=False)
        df_Ekt.to_excel(writer, sheet_name='Energy(kT)', index=False)
        df_F.to_excel(writer, sheet_name='Force(N)', index=False)
        if cbHET == 1 or cbHETUSER == 1:
            df_E_HET.to_excel(writer, sheet_name='HET_Energy(kT)', index=False, header=False)
            df_F_HET.to_excel(writer, sheet_name='HET_Force(N)', index=False, header=False)