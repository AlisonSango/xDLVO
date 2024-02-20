import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog

'''Graphical User Interface'''

#Functions
# def activate_panel2():
#     # Activate o deactivate entries
#     state = cbA132.get()
#     for entry in entries2:
#         entry.config(state=tk.NORMAL if state else tk.DISABLED)
#     entry2.config(state=tk.NORMAL if state else tk.DISABLED)
#     button2.config(state=tk.NORMAL if state else tk.DISABLED)
#
# def activate_panel3():
#     # Activate o deactivate entries
#     state = cbgammaAB.get()
#     for entry in entries3:
#         entry.config(state=tk.NORMAL if state else tk.DISABLED)
#     entry3.config(state=tk.NORMAL if state else tk.DISABLED)
#     button3.config(state=tk.NORMAL if state else tk.DISABLED)
#
# def activate_panel4():
#     # Activate o deactivate entries
#     state = cbW132.get()
#     for entry in entries4:
#         entry.config(state=tk.NORMAL if state else tk.DISABLED)
#     entry4.config(state=tk.NORMAL if state else tk.DISABLED)
#     button4.config(state=tk.NORMAL if state else tk.DISABLED)
#
# def activate_panel5():
#     # Activate o deactivate entries
#     state = cbacont.get()
#     for entry in entries5:
#         entry.config(state=tk.NORMAL if state else tk.DISABLED)
#     entry5_1.config(state=tk.NORMAL if state else tk.DISABLED)
#     entry5_2.config(state=tk.NORMAL if state else tk.DISABLED)
#     button5.config(state=tk.NORMAL if state else tk.DISABLED)

def activate_panel_HET():
    # Activate o deactivate entries
    state = cbHET.get()
    entry6_10.config(state=tk.NORMAL if state else tk.DISABLED)
    if state:
        cbHETUSER.set(False)
        cbMEAN.set(False)

def activate_panel_HETUSER():
    # Activate o deactivate entries
    state = cbHETUSER.get()
    entry6_6.config(state=tk.NORMAL if state else tk.DISABLED)
    entry6_7.config(state=tk.NORMAL if state else tk.DISABLED)
    entry6_8.config(state=tk.NORMAL if state else tk.DISABLED)
    entry6_9.config(state=tk.NORMAL if state else tk.DISABLED)
    entry6_10.config(state=tk.NORMAL if state else tk.DISABLED)
    if state:
        cbHET.set(False)
        cbMEAN.set(False)

def open_window_coated_system():
    if cbCOATED.get():
        # Aditional coated system Window
        windowCS = tk.Toplevel(root)
        windowCS.title("Coated System")

        # Coated system Panel 1
        panelCS1 = tk.LabelFrame(windowCS, text='Type of Coated System', width=50, height=50, fg='blue', padx=3, pady=3)
        panelCS2 = tk.LabelFrame(windowCS, text='Coating thickness  and Fluid Hamaker constant', width=50, height=50, fg='blue', padx=3, pady=3)
        panelCS3 = tk.LabelFrame(windowCS, text='Combined Hamaker constant - Coated system', width=50, height=50, fg='blue', padx=3, pady=3)
        panelCS4 = tk.LabelFrame(windowCS, text='Hamaker constants - Single material values', width=50, height=50, fg='blue', padx=3, pady=3)
        panelCS5 = tk.LabelFrame(windowCS, text='Hamaker constant contributions', width=50, height=50, fg='blue', padx=3, pady=3)
        panelCS5_1 = tk.LabelFrame(panelCS5, text='Coated Colloid - Coated Collector', width=50, height=50, fg='blue', padx=3, pady=3)
        panelCS5_2 = tk.LabelFrame(panelCS5, text='Colloid - Coated Collector', width=50, height=50, fg='blue', padx=3, pady=3)
        panelCS5_3 = tk.LabelFrame(panelCS5, text='Coated Colloid - Collector', width=50, height=50, fg='blue', padx=3, pady=3)
        panelCS1.grid(row=0, column=0, padx=3, pady=3, sticky='n')
        panelCS2.grid(row=0, column=1, padx=3, pady=3, sticky='n')
        panelCS3.grid(row=1, column=0, padx=3, pady=3, rowspan=2, sticky='n')
        panelCS4.grid(row=2, column=0, padx=3, pady=3, sticky='n')
        panelCS5.grid(row=3, column=0, padx=3, pady=3, rowspan=2, sticky='n')
        panelCS5_1.grid(row=0, column=0, padx=3, pady=3, sticky='n')
        panelCS5_2.grid(row=0, column=1, padx=3, pady=3, sticky='n')
        panelCS5_3.grid(row=0, column=2, padx=3, pady=3, sticky='n')

def calculate_profiles():
    # Aditional calculate profiles Window
    windowCP = tk.Toplevel(root)
    windowCP.title("Energy and Force Profiles")

# Root widget
root = tk.Tk()
root.title('GUIxDLVO')  # window title

#Main Parameters panel
panel1 = tk.LabelFrame(root, text='Main Parameters (default = CML-water-silica @ pH 6.7, IS 6 mM)', width=450, height=651, fg='blue', padx=3, pady=3)
panel1.grid(row=0, column=0, padx=3, pady=3, rowspan=3, sticky='n')
panel1.grid_propagate(0)

labels_panel1 = ['Temperature(K)', 'Ionic strength (IS) (mol/m3)', 'Colloid radius (a1) (m)', 'Collector radius (a2) (m)',
                 'Colloid zeta potential (z1) (V)', 'Collector zeta potential (z2) (V)', 'Valence of the symmetric electrolyte (z) (-)',
                 'Relative permittivity of water (epsilonR) (-)', 'vdW characterisitic wavelength (lambdaVDW) (m)',
                 'Born collision diameter (sigmac) (m)']
values_panel1 = [293.15, 6.0, 2.2e-6, 2.55e-4, -0.070, -0.065, 1, 80.0, 1.0e-7, 3.0e-10]
var_panel1 = {label: tk.StringVar(value=value) for label, value in zip(labels_panel1, values_panel1)}

for i, label in enumerate(labels_panel1):
    tk.Entry(panel1, textvariable=var_panel1[label], width=10, justify='center').grid(row=i, column=0, padx=1, pady=1, sticky='w')
    tk.Label(panel1, text=f"{label}").place(x=68, y=i*21)

#Extended XDLVO parameters subpanel
panel1_1 = tk.LabelFrame(panel1, text='Extended xDLVO parameters', width=428, height=115, fg='blue')
panel1_1.grid(padx=0, pady=10,  columnspan=2)
panel1_1.grid_propagate(0)

labels_exten_xDLVO = ['Lewis acid-base decay length (lambdaAB) (m)', 'Steric decay length (lambdaSTE) (m)',
                      'Steric energy at minimum separation distance (gammaSTE) (J/m2)', 'Asperity height above mean surface (aasp) (m)']
values_exten_xDLVO = [6.0e-10, 4.1e-10, 1.7e-2, 0.0]
var_exten_xDLVO = {label: tk.StringVar(value=value) for label, value in zip(labels_exten_xDLVO, values_exten_xDLVO)}

for i, label in enumerate(labels_exten_xDLVO):
    tk.Entry(panel1_1, textvariable=var_exten_xDLVO[label], width=10, justify='center').grid(row=i, column=0, padx=1, pady=1)
    tk.Label(panel1_1, text=f"{label}").grid(row=i, column=1, padx=1, pady=1, sticky='w')

    if abs(float(var_exten_xDLVO[label].get())) > 100 or 0 < abs(float(var_exten_xDLVO[label].get())) < 0.01:
        var_exten_xDLVO[label].set("{:.2e}".format(float(var_exten_xDLVO[label].get())))

# van der Waals subpanel
panel1_2 = tk.LabelFrame(panel1, text='van der Waals', width=428, height=90, fg='blue') #width=400
panel1_2.grid(padx=3, pady=3,  columnspan=2)
panel1_2.grid_propagate(0)

cbCOATED = tk.BooleanVar()
tk.Checkbutton(panel1_2, text='Coated system', variable=cbCOATED, command=open_window_coated_system).place(x=250, y=20)

#Hamaker subpanel
panel1_2_1 = tk.LabelFrame(panel1_2, text='Hamaker constant (A132) (J)', width=300, height=100, fg='blue')
panel1_2_1.grid(padx=10, pady=3)

var_panel1_2_1 = {'A132':tk.StringVar(value=7.17e-21)}

tk.Entry(panel1_2_1, textvariable=var_panel1_2_1['A132'], width=10, justify='center').grid(row=1, column=0, padx=1, pady=1, sticky='nw')

cbA132 = tk.BooleanVar()
tk.Checkbutton(panel1_2_1, text='Calculate from fundamentals', variable=cbA132, command=activate_panel2).grid(sticky='s')

# Acid-Base energy subpanel
panel1_3 = tk.LabelFrame(panel1, text='Acid-Base energy at minimum separation distance (gammaAB) (J/m2)', width=428, height=50, fg='blue')
panel1_3.grid(padx=10, pady=3,  columnspan=2)
panel1_3.grid_propagate(0)

var_panel1_3 = {'gammaAB':tk.StringVar(value=-0.0270305)}

tk.Entry(panel1_3, textvariable=var_panel1_3['gammaAB'], width=10, justify='center').grid(row=0, column=0, padx=3, pady=1)

cbgammaAB = tk.BooleanVar()
tk.Checkbutton(panel1_3, text='Calculate from fundamentals', variable=cbgammaAB, command=activate_panel3).grid(row=0, column=1, padx=1, pady=1, sticky='nsew')

# Work of adhesion subpanel
panel1_4 = tk.LabelFrame(panel1, text='Work of adhesion (W132) (J/m2)', width=428, height=50, fg='blue')
panel1_4.grid(padx=10, pady=3,  columnspan=2)
panel1_4.grid_propagate(0)

var_panel1_4 = {'W132':tk.StringVar(value=-0.029)}

tk.Entry(panel1_4, textvariable=var_panel1_4['W132'], width=10, justify='center').grid(row=0, column=0, padx=3, pady=1)

cbW132 = tk.BooleanVar()
tk.Checkbutton(panel1_4, text='Calculate from fundamentals', variable=cbW132, command=activate_panel4).grid(row=0, column=1, padx=1, pady=1, sticky='nsew')

# Contact Radius subpanel
panel1_5 = tk.LabelFrame(panel1, text='Contact Radius (acont) (m)', width=428, height=50, fg='blue')
panel1_5.grid(padx=10, pady=3,  columnspan=2)
panel1_5.grid_propagate(0)

var_panel1_5 = {'acont': tk.StringVar(value=5.0e-8)}

tk.Entry(panel1_5, textvariable=var_panel1_5['acont'], width=10, justify='center').grid(row=0, column=0, padx=3, pady=1)

cbacont = tk.BooleanVar()
tk.Checkbutton(panel1_5, text='Calculate from fundamentals', variable=cbacont, command=activate_panel5).grid(row=0, column=1, padx=1, pady=1, sticky='nsew')

# Roughness panel
panel1_RM = tk.LabelFrame(panel1, text='Roughness mode', width=50, height=40, fg='blue')
panel1_RM.place(x=265, y=0)

var_RM0 = tk.BooleanVar()
cb1 = tk.BooleanVar()
cb2 = tk.BooleanVar()
cb3 = tk.BooleanVar()
tk.Checkbutton(panel1_RM, text='Smooth surfaces', variable=var_RM0).grid(sticky='w')
tk.Checkbutton(panel1_RM, text='Rough Colloid', variable=cb1).grid(sticky='w')
tk.Checkbutton(panel1_RM, text='Rough Collector', variable=cb2).grid(sticky='w')
tk.Checkbutton(panel1_RM, text='Rough Colloid & Collector', variable=cb3).grid(sticky='w')

# Geometry panel
panel1_G = tk.LabelFrame(panel1, text='Geometry', width=50, height=40, fg='blue')
panel1_G.place(x=370, y=120)

cbSS = tk.BooleanVar()
cbSP = tk.BooleanVar()
tk.Checkbutton(panel1_G, text='Sphere\nSphere', variable=cbSS).grid(sticky='w')
tk.Checkbutton(panel1_G, text='Sphere\nPlate', variable=cbSP).grid(sticky='w')

# # Hamaker constant parameters panel
# panel2 = tk.LabelFrame(root, text='Hamaker constant parameters', width=386, height=250, fg='blue', padx=3)
# panel2.grid(row=0, column=1, padx=5, pady=3, sticky='n')
# panel2.grid_propagate(0)
#
# labels_Hamaker = ['Main electronic absorption frequency (ve) (s-1)', 'Colloid dielectric constant (e1) (-)',
#                   'Colloid refractive index (n1) (-)', 'Collector dielectric constant (e2) (-)', 'Collector refractive index (n2) (-)',
#                   'Fluid dielectric constant (e3) (-)', 'Fluid refractive index (n3) (-)']
# values_Hamaker = [2.04e15, 2.55, 1.557, 3.8, 1.448, 80, 1.333]
# var_Hamaker = {label: tk.StringVar(value=value) for label, value in zip(labels_Hamaker, values_Hamaker)}
# var_panel2 = {'Hamaker constant (ve  equivalent)  (J)':tk.StringVar(value='calculate')}
#
# #Entries and Labels
# entries2 = [tk.Entry(panel2, textvariable=var_Hamaker[label], width=10, justify='center', state=tk.DISABLED) for label in labels_Hamaker]
# for i, label in enumerate(labels_Hamaker):
#     entries2[i].grid(row=i, column=0, padx=1, pady=1)
#     tk.Label(panel2, text=f"{label}").grid(row=i, column=1, padx=1, pady=1, sticky='w')
#
#     if abs(float(var_Hamaker[label].get())) > 100 or abs(float(var_Hamaker[label].get())) < 0.01:
#         var_Hamaker[label].set("{:.2e}".format(float(var_Hamaker[label].get())))
#
# entry2 = tk.Entry(panel2, textvariable=var_panel2['Hamaker constant (ve  equivalent)  (J)'], width=10, justify='center', state=tk.DISABLED)
# entry2.grid(row=11, column=0, padx=1, pady=1)
# tk.Label(panel2, text='Hamaker constant (ve  equivalent)  (J)').grid(row=11, column=1, padx=1, pady=1, sticky='w')
#
# button2 = tk.Button(panel2, text="Calculate", bg='lime', width=12, state=tk.DISABLED, #, command=calcular_panel1
#                     )
# button2.grid(row=len(labels_Hamaker)+2, column=0, columnspan=2, padx=5, pady=5)
#
# # Acid - Base panel
# panel3 = tk.LabelFrame(root, text='Acid-Base surface energy components', width=386, height=220, fg='blue', padx=3)
# panel3.grid(row=1, column=1, padx=5, pady=1)
# panel3.grid_propagate(0)
#
# labels_AB = ['Colloid electron acceptor (g1pos) (J/m2)', 'Colloid electron donor (g1neg) (J/m2)', 'Colloid electron acceptor (g2pos) (J/m2)',
#              'Colloid electron donor (g2neg) (J/m2)', 'Colloid electron acceptor (g3pos) (J/m2)', 'Colloid electron donor (g2neg) (J/m2)']
# values_AB = [0.0, 1.10e-3, 1.00e-4, 37.50e-3, 25.50e-3, 25.50e-3]
# var_AB = {label: tk.StringVar(value=value) for label, value in zip(labels_AB, values_AB)}
# var_panel3 = {'Acid-base energy at minimum separation distance (J/m2)': tk.StringVar(value='calculate')}
# entries3 = [tk.Entry(panel3, textvariable=var_AB[label], width=10, justify='center', state=tk.DISABLED) for label in labels_AB]
#
# for i, label in enumerate(labels_AB):
#     entries3[i].grid(row=i, column=0, padx=1, pady=1)
#     tk.Label(panel3, text=f"{label}").grid(row=i, column=1, padx=1, pady=1, sticky='w')
#
#     if abs(float(var_AB[label].get())) > 100 or 0 < abs(float(var_AB[label].get())) < 0.01:
#         var_AB[label].set("{:.2e}".format(float(var_AB[label].get())))
#
# entry3 = tk.Entry(panel3, textvariable=var_panel3['Acid-base energy at minimum separation distance (J/m2)'], width=10, justify='center', state=tk.DISABLED)
# entry3.grid(row=10, column=0, padx=1, pady=1)
# tk.Label(panel3, text='Acid-base energy at minimum separation distance (J/m2)').grid(row=10, column=1, padx=1, pady=1, sticky='w')
#
# button3 = tk.Button(panel3, text="Calculate", bg='lime', width=12, state=tk.DISABLED, #, command=calcular_panel1
#           )
# button3.grid(row=len(labels_AB)+2, column=0, columnspan=2, padx=5, pady=5)
#
# # Work of adhesion panel
# panel4 = tk.LabelFrame(root, text='Work of adhesion (for contact area)', width=386, height=170, fg='blue', padx=3)
# panel4.grid(row=2, column=1, padx=5, pady=1)
# panel4.grid_propagate(0)
#
# labels_adhesion = ['Colloid van der Waals free energy (g1LW) (J/m2)', 'Collector van der Waals free energy (g2LW) (J/m2)',
#                    'Fluid van der Waals free energy (g3LW) (J/m2)', 'Acid-base energy at minimum separation distance (J/m2)']
# values_adhesion = [42.00e-3, 27.30e-3, 21.80e-3, -0.0270305]
# var_adhesion = {label: tk.StringVar(value=value) for label, value in zip(labels_adhesion, values_adhesion)}
# var_panel4 = {'Work of adhesion (W132) (J/m2)': tk.StringVar(value='calculate')}
# entries4 = [tk.Entry(panel4, textvariable=var_adhesion[label], width=10, justify='center', state=tk.DISABLED) for label in labels_adhesion]
#
# for i, label in enumerate(labels_adhesion):
#     entries4[i].grid(row=i, column=0, padx=1, pady=1)
#     tk.Label(panel4, text=f"{label}").grid(row=i, column=1, padx=1, pady=1, sticky='w')
#
#     if abs(float(var_adhesion[label].get())) > 100 or abs(float(var_adhesion[label].get())) < 0.01:
#         var_adhesion[label].set("{:.2e}".format(float(var_adhesion[label].get())))
#
# entry4 = tk.Entry(panel4, textvariable=var_panel4['Work of adhesion (W132) (J/m2)'], width=10, justify='center', state=tk.DISABLED)
# entry4.grid(row=8, column=0, padx=1, pady=1)
# tk.Label(panel4, text='Work of adhesion (W132) (J/m2)').grid(row=8, column=1, padx=1, pady=1, sticky='w')
#
# button4 = tk.Button(panel4, text="Calculate", bg='lime', width=12, state=tk.DISABLED, #, command=calcular_panel1
#           )
# button4.grid(row=len(labels_adhesion)+2, column=0, columnspan=2, padx=5, pady=5)
#
# # Contact Radius panel
# panel5 = tk.LabelFrame(root, text='Contact Radius (for steric interaction)', width=360, height=220, fg='blue', padx=3)
# panel5.grid(row=0, column=2, padx=5, pady=3, sticky='n')
# panel5.grid_propagate(0)
#
# labels_steric = ['Colloid Young\'s modulus (E1) (N/m2)', 'Collector Young\'s modulus (E2) (N/m2)', 'Colloid Poison\'s ratio (v1) (-)',
#                  'Collector Poison\'s ratio (v2) (-)', 'Work of adhesion (W132) (J/m2)']
# values_steric = [3.0e9, 7.3e10, 0.33, 0.22, -0.028448]
# var_steric = {label: tk.StringVar(value=value) for label, value in zip(labels_steric, values_steric)}
# var_panel5 = {'Combined elastic modulus (Kint) (N/m2)': tk.StringVar(value='calculate'), 'Contact Radius (acont) (m)': tk.StringVar(value='calculate')}
# entries5 = [tk.Entry(panel5, textvariable=var_steric[label], width=10, justify='center', state=tk.DISABLED) for label in labels_steric]
#
# for i, label in enumerate(labels_steric):
#     entries5[i].grid(row=i, column=0, padx=1, pady=1)
#     tk.Label(panel5, text=f"{label}").grid(row=i, column=1, padx=1, pady=1, sticky='w')
#
#     if abs(float(var_steric[label].get())) > 100 or abs(float(var_steric[label].get())) < 0.01:
#         var_steric[label].set("{:.2e}".format(float(var_steric[label].get())))
#
# entry5_1 = tk.Entry(panel5, textvariable=var_panel5['Combined elastic modulus (Kint) (N/m2)'], width=10, justify='center', state=tk.DISABLED)
# entry5_1.grid(row=9, column=0, padx=1, pady=1)
# entry5_2 = tk.Entry(panel5, textvariable=var_panel5['Contact Radius (acont) (m)'], width=10, justify='center', state=tk.DISABLED)
# entry5_2.grid(row=10, column=0, padx=1, pady=1)
# tk.Label(panel5, text='Combined elastic modulus (Kint) (N/m2)').grid(row=9, column=1, padx=1, pady=1, sticky='w')
# tk.Label(panel5, text='Contact Radius (acont) (m)').grid(row=10, column=1, padx=1, pady=1, sticky='w')
#
# button5 = tk.Button(panel5, text="Calculate", bg='lime', width=12, state=tk.DISABLED,  #, command=calcular_panel1
#           )
# button5.grid(row=len(labels_adhesion)+2, column=0, columnspan=2, padx=5, pady=5)

#Profiles panel
panel6 = tk.LabelFrame(root, text='xDLVO Profiles', width=360, height=260, fg='blue', padx=3)
panel6.place(x=857, y=228)
panel6.grid_propagate(0)

var_panel6 = {'rZOI': tk.StringVar(value='calculate'), 'rhet1': tk.StringVar(value='calculate'), 'rhet2': tk.StringVar(value='calculate'),
              'rhet3': tk.StringVar(value='calculate'), 'rhet4': tk.StringVar(value='calculate'), 'rhet1USER': tk.StringVar(value='calculate'),
              'rhet2USER': tk.StringVar(value='calculate'), 'rhet3USER': tk.StringVar(value='calculate'), 'rhet4USER': tk.StringVar(value='calculate'),
              'zetahet': tk.StringVar(value=0.051)}

cbMEAN = tk.BooleanVar()
cbHET = tk.BooleanVar()
cbHETUSER = tk.BooleanVar()
tk.Checkbutton(panel6, text='Over  mean-field surface', variable=cbMEAN).grid(row=0, column=0, padx=1, pady=1, columnspan=4, sticky='w')
tk.Checkbutton(panel6, text='Over heterodomain radii (m) for ZOI areal fractions (AFRACT)', variable=cbHET, command=activate_panel_HET).grid(row=1, column=0, padx=1, pady=1, columnspan=4, sticky='w')
tk.Checkbutton(panel6, text='Over user-specified heterodomain radii (m)', variable=cbHETUSER, command=activate_panel_HETUSER).grid(row=4, column=0, padx=1, pady=1, columnspan=4, sticky='w')

entry6_1 = tk.Entry(panel6, textvariable=var_panel6['rZOI'], width=10, justify='center')
entry6_2 = tk.Entry(panel6, textvariable=var_panel6['rhet1'], width=10, justify='center', state=tk.DISABLED)
entry6_3 = tk.Entry(panel6, textvariable=var_panel6['rhet2'], width=10, justify='center', state=tk.DISABLED)
entry6_4 = tk.Entry(panel6, textvariable=var_panel6['rhet3'], width=10, justify='center', state=tk.DISABLED)
entry6_5 = tk.Entry(panel6, textvariable=var_panel6['rhet4'], width=10, justify='center', state=tk.DISABLED)
entry6_6 = tk.Entry(panel6, textvariable=var_panel6['rhet1USER'], width=10, justify='center', state=tk.DISABLED)
entry6_7 = tk.Entry(panel6, textvariable=var_panel6['rhet2USER'], width=10, justify='center', state=tk.DISABLED)
entry6_8 = tk.Entry(panel6, textvariable=var_panel6['rhet3USER'], width=10, justify='center', state=tk.DISABLED)
entry6_9 = tk.Entry(panel6, textvariable=var_panel6['rhet4USER'], width=10, justify='center', state=tk.DISABLED)
entry6_10 =tk.Entry(panel6, textvariable=var_panel6['zetahet'], width=10, justify='center', state=tk.DISABLED)
entry6_1.place(x=160, y=5)
entry6_2.grid(row=2, column=0, padx=1, pady=1)
entry6_3.grid(row=2, column=1, padx=1, pady=1)
entry6_4.grid(row=2, column=2, padx=1, pady=1)
entry6_5.grid(row=2, column=3, padx=1, pady=1)
entry6_6.grid(row=5, column=0, padx=1, pady=1)
entry6_7.grid(row=5, column=1, padx=1, pady=1)
entry6_8.grid(row=5, column=2, padx=1, pady=1)
entry6_9.grid(row=5, column=3, padx=1, pady=1)
entry6_10.place(x=45, y=148)

tk.Label(panel6, text='ZOI radius (rZOI) (m)').place(x=235, y=3)
tk.Label(panel6, text='0.25 ZOI').grid(row=3, column=0, padx=1, pady=1)
tk.Label(panel6, text='0.5 ZOI').grid(row=3, column=1, padx=1, pady=1)
tk.Label(panel6, text='0.75 ZOI').grid(row=3, column=2, padx=1, pady=1)
tk.Label(panel6, text='1.0 ZOI').grid(row=3, column=3, padx=1, pady=1)
tk.Label(panel6, text='Heterodomain zeta potential (zhet) (V)').grid(row=6, column=1, padx=1, pady=1, columnspan=3)

tk.Button(panel6, text='Calculate Profiles', bg='lime',  width=25, command=calculate_profiles).grid(row=8, column=0, columnspan=4, padx=5, pady=5)
tk.Button(panel6, text='Set Output Directory', bg='lime', #, command=calcular_panel1
          ).place(x=75, y=210)
tk.Button(panel6, text='Save to file', bg='lime', #, command=calcular_panel1
          ).place(x=210, y=210)

#Authors panel
panel7 = tk.LabelFrame(root, text='Authors', width=360, height=162, padx=3)
panel7.grid(row=2, column=2, padx=5, pady=3, sticky='s')
panel7.grid_propagate(0)

#Coated system
labels_type_coated = ['Coated Colloid - Coated Collector', 'Colloid - Coated Collector', 'Coated Colloid -  Collector']
labels_thickness = ['Colloid coating thickness (T1) (m)', 'Collector coating thickness (T2) (m)', 'Fluid Hamaker Constant (A33) (J)']
labels_combined_A132 = ['Colloid - Collector (A12) (J)', 'Colloid - Collector Coating (A12p) (J)', 'Colloid - Fluid (A13) (J)',
                        'Colloid Coating - Collector  (A1p2) (J)', 'Colloid Coating - Collector Coating (A1p2p) (J)',
                        'Colloid Coating - Fluid  (A1p3) (J)', 'Collector - Fluid  (A23) (J)', 'Collector Coating - Fluid  (A2p3) (J)']
#Calculate from single material values
labels_single = ['Colloid Hamaker constant (A11) (J)', 'Colloid coating Hamaker constant (A1p1p) (J)', 'Collector Hamaker constant (A22) (J))',
                 'Collector coating Hamaker constant (A2p2p) (J)']
labels_contributions =['Colloid coating - Collector Coating', 'Colloid - Collector Coating', 'Colloid coating - Collector',
                       'Colloid - Collector']
#Coated Colloid - Coated Collector: los 4
#Colloid - Coated Collector: 2 y 4
#Coated Colloid - Collector: 3 y 2

root.mainloop()  # The window won't appear until we enter the Tkinter event loop

