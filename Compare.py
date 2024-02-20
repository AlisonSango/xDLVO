import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import openpyxl
def data_frame(route, H, EJ, F, cbHET,cbHETUSER, E_HET_T, F_HET_T):
    #Data frame with matlab data
    headlines_E = ['H(m)_m', 'E_van_der_Waals_m', 'E_EDL_m', 'E_AB_m', 'E_Born_m', 'E_Steric_m', 'E_total_m']
    headlines_F = ['H(m)_m','F_van_der_Waals_m','F_EDL_m', 'F_AB_m', 'F_Born_m', 'F_Steric_m', 'F_total_m']
    headlines = ['H(m)', 'E_van_der_Waals', 'E_EDL', 'E_AB', 'E_Born', 'E_Steric', 'E_total', 'F_van_der_Waals',
                     'F_EDL', 'F_AB', 'F_Born', 'F_Steric', 'F_total']
    headlines_HET = ['H(m)', 'E_van_der_Waals', 'E_EDL', 'E_AB', 'E_Born', 'E_Steric', 'E_total', 'F_van_der_Waals',
                     'F_EDL', 'F_AB', 'F_Born', 'F_Steric', 'F_total','E_0.25_ZOI', 'E_0.5_ZOI', 'E_0.75_ZOI',
                     'E_1.0_ZOI', 'F_0.25_ZOI', 'F_0.5_ZOI', 'F_0.75_ZOI', 'F_1.0_ZOI']
    data_energy_m = pd.read_excel(route, sheet_name='Energy(J)', usecols='A:G', names = headlines_E)
    data_force_m = pd.read_excel(route, sheet_name='Force(N)', usecols='A:G', names = headlines_F)

    if cbHET == 1 or cbHETUSER == 1:
        data_HET_energy_m = pd.read_excel(route, sheet_name='HET_Energy(kT)', usecols='A:E',
                                          names = ['H(m)_m','E_0.25_ZOI_m', 'E_0.5_ZOI_m', 'E_0.75_ZOI_m', 'E_1.0_ZOI_m'], skiprows=2)
        data_HET_force_m = pd.read_excel(route, sheet_name='HET_Force(N)', usecols='A:E',
                                      names=['H(m)_m','F_0.25_ZOI_m', 'F_0.5_ZOI_m', 'F_0.75_ZOI_m', 'F_1.0_ZOI_m'], skiprows=2)
        df_m_1 = pd.merge(data_energy_m, data_force_m, how='inner', on='H(m)_m')
        df_m_2 = pd.merge(data_HET_energy_m, data_HET_force_m, how='inner', on='H(m)_m')
        df_m = pd.merge(df_m_1, df_m_2, how='inner', on='H(m)_m')
    else:
        df_m = pd.merge(data_energy_m, data_force_m, how='inner', on='H(m)_m')
    #merge data frame
    if cbHET == 1 or cbHETUSER == 1:
        df_py = pd.DataFrame(np.column_stack((H.T, EJ, F, E_HET_T, F_HET_T)), columns=headlines_HET)
    else:
        df_py = pd.DataFrame(np.column_stack((H.T, EJ, F)), columns=headlines)
    df = pd.concat([df_py, df_m], axis=1)
    return (df)

def error_p_m (df, list, type):
    for interaction in list:
        #calculation of percentage error
        df['Error_{:s}'.format(interaction)] = (abs(df['{:s}_m'.format(interaction)] - df['{:s}'.format(interaction)])
                                                * 100 / abs(df['{:s}_m'.format(interaction)]))
        #Figure comparison matlab, python and error
        # fig, ax = plt.subplots(2,1, figsize= [7, 10])
        # ax[0].semilogx(df.iloc[:, 0], df['{:s}_m'.format(interaction)], linestyle='dashed', marker= 'd', markevery= 40,
        #                label='{:s}_m'.format(interaction))
        # ax[0].semilogx(df.iloc[:, 0], df['{:s}'.format(interaction)], 'r', label=interaction)
        # ax[0].set_xlabel('distance (m)')
        # if type=='E':
        #     ax[0].set_ylabel('Energy (J)')
        # elif type=='F':
        #     ax[0].set_ylabel('Force (N)')
        # elif type =='H':
        #     ax[0].set_ylabel('Distance (m)')
        # ax[1].semilogx(df.iloc[:, 0], df['Error_{:s}'.format(interaction)], label = 'error')
        # ax[1].set_ylabel('Error (%)')
        # ax[0].legend()
        # plt.show()
