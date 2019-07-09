#Gympass test - Rogerio Junior - 2019
#Using Python with Pandas - looking for vectorized (no loop solution) as the input data has a dataframe type

import sys
import time
import pandas as pd
import csv
import re
import numpy as np

#read csv using pandas for easier encoding and delimitation
#currently using local folder, please change it to your local folder
#my path for test /home/rsjr/Dev/Kart/kart.txt

file_path = input('Entre o caminho do arquivo de entrada: ')


kart_df = pd.read_csv(file_path,
                      encoding = "utf-8",
                      sep='\s+',
                      decimal=",",
                      skiprows=[0],
                      header=None,
                      engine='python',
                      names=["Hora","CPiloto","c","NPiloto","NVoltas","TVolta","VMedia"])
#main table pre-processing
#Delete column 'c' as it has only '-' values, not relevant
kart_df = kart_df.drop(['c'], axis=1)

#transform lap elapsed time to seconds so we can sum afterwards
#replace `.` to `:` in order to faciliate string split
new_tvolta = kart_df['TVolta'].str.replace('.', ':')

#split 0:00:00 to 0, 00, 00
new_tvolta = new_tvolta.str.split(':')

#convert min, seconds, miliseconds to seconds using apply
new_tvolta = new_tvolta.apply(lambda x: (float(x[2]) / 1000 + float(x[0]) * 60 + float(x[1])))

#delete unprocessed TVolta Column
kart_df = kart_df.drop(['TVolta'], axis=1)
kart_df_final = pd.concat([kart_df,new_tvolta], axis=1)

#dataframes for the results related to each pilot

final_results_df = pd.DataFrame()

massa_df = pd.DataFrame()
massa_res_df = pd.DataFrame()
best_lap_massa = 0
massa_total_time = 0
n_voltas_massa = 0
c_massa = 0
n_massa = 0

#Process MASSA (Pilot 038)
massa_df = kart_df_final.loc[kart_df['CPiloto'] == 38]

#get pilot code
c_massa = massa_df.iloc[1,1]

#get pilot noame
n_massa = massa_df.iloc[1,2]

#get pilot best lap
best_lap_massa  = massa_df['TVolta'].min()

#get pilot number of laps
n_voltas_massa = massa_df['NVoltas'].max()

#get total time
massa_total_time = massa_df['TVolta'].sum()

#append results
massa_res_df = massa_res_df.append([c_massa,n_massa,n_voltas_massa,massa_total_time, best_lap_massa]).T

barrichello_df = pd.DataFrame()
barrichello_res_df = pd.DataFrame()
best_lap_barrichello = 0
barrichello_total_time = 0
n_voltas_barrichello = 0
c_barrichello = 0
n_barrichello = 0

#Process barrichello (Pilot 038)
barrichello_df = kart_df_final.loc[kart_df['CPiloto'] == 33]

#get pilot code
c_barrichello = barrichello_df.iloc[1,1]

#get pilot noame
n_barrichello = barrichello_df.iloc[1,2]

#get pilot number of laps
n_voltas_barrichello = barrichello_df['NVoltas'].max()

#get total time
barrichello_total_time = barrichello_df['TVolta'].sum()

#get pilot best lap
best_lap_barrichello  = barrichello_df['TVolta'].min()

#append results
barrichello_res_df = barrichello_res_df.append([c_barrichello,n_barrichello,n_voltas_barrichello,barrichello_total_time, best_lap_barrichello]).T

raikkonen_df = pd.DataFrame()
raikkonen_res_df = pd.DataFrame()
best_lap_raikkonen = 0
raikkonen_total_time = 0
n_voltas_raikkonen = 0
c_raikkonen = 0
n_raikkonen = 0

#Process raikkonen (Pilot 038)
raikkonen_df = kart_df_final.loc[kart_df['CPiloto'] == 2]

#get pilot code
c_raikkonen = raikkonen_df.iloc[1,1]

#get pilot noame
n_raikkonen = raikkonen_df.iloc[1,2]

#get pilot number of laps
n_voltas_raikkonen = raikkonen_df['NVoltas'].max()

#get total time
raikkonen_total_time = raikkonen_df['TVolta'].sum()

#get pilot best lap
best_lap_raikkonen  = raikkonen_df['TVolta'].min()

#append results
raikkonen_res_df = raikkonen_res_df.append([c_raikkonen,n_raikkonen,n_voltas_raikkonen,raikkonen_total_time, best_lap_raikkonen]).T

webber_df = pd.DataFrame()
webber_res_df = pd.DataFrame()
best_lap_webber = 0
webber_total_time = 0
n_voltas_webber = 0
c_webber = 0
n_webber = 0

#Process webber
webber_df = kart_df_final.loc[kart_df['CPiloto'] == 23]

#get pilot code
c_webber = webber_df.iloc[1,1]

#get pilot noame
n_webber = webber_df.iloc[1,2]

#get pilot number of laps
n_voltas_webber = webber_df['NVoltas'].max()

#get total time
webber_total_time = webber_df['TVolta'].sum()

#get pilot best lap
best_lap_webber  = webber_df['TVolta'].min()

#append results
webber_res_df = webber_res_df.append([c_webber,n_webber,n_voltas_webber,webber_total_time, best_lap_webber]).T

alonso_df = pd.DataFrame()
alonso_res_df = pd.DataFrame()
best_lap_alonso = 0
alonso_total_time = 0
n_voltas_alonso = 0
c_alonso = 0
n_alonso = 0

#Process alonso (Pilot 038)
alonso_df = kart_df_final.loc[kart_df['CPiloto'] == 15]

#get pilot code
c_alonso = alonso_df.iloc[1,1]

#get pilot noame
n_alonso = alonso_df.iloc[1,2]

#get pilot number of laps
n_voltas_alonso = alonso_df['NVoltas'].max()

#get total time
alonso_total_time = alonso_df['TVolta'].sum()

#get pilot best lap
best_lap_alonso  = alonso_df['TVolta'].min()

#append results
alonso_res_df = alonso_res_df.append([c_alonso,n_alonso,n_voltas_alonso,alonso_total_time, best_lap_alonso]).T

vettel_df = pd.DataFrame()
vettel_res_df = pd.DataFrame()
best_lap_vettel = 0
vettel_total_time = 0
n_voltas_vettel = 0
c_vettel = 0
n_vettel = 0

#Process vettel (Pilot 038)
vettel_df = kart_df_final.loc[kart_df['CPiloto'] == 11]

#get pilot code
c_vettel = vettel_df.iloc[1,1]


#get pilot noame
n_vettel = vettel_df.iloc[1,2]


#get pilot number of laps
n_voltas_vettel = vettel_df['NVoltas'].max()


#get total time
vettel_total_time = vettel_df['TVolta'].sum()

#get pilot best lap
best_lap_vettel  = vettel_df['TVolta'].min()

#append results
vettel_res_df = vettel_res_df.append([c_vettel,n_vettel,n_voltas_vettel,vettel_total_time, best_lap_vettel]).T

#append all processed results into one final data frame
final_results_df = final_results_df.append([massa_res_df,barrichello_res_df,raikkonen_res_df,webber_res_df, alonso_res_df,vettel_res_df])
kart_df_final = pd.concat([kart_df,new_tvolta], axis=1)


podium_df = pd.DataFrame()
#results_table['Mean recall score']=results_table['Mean recall'].astype('float64')


#sort result table by total time
final_results_df = final_results_df.sort_values(3)

#count how many rows are inside results df (therefore, how many pilots)
row_count = final_results_df.shape[0]
pos = list(range(1,row_count+1))

#create podium list
final_results_df['PosChegada'] = pos

#rename columns for final display
final_results_df.columns = ['CodigoPiloto','NomePiloto','NVoltas','TempoTotal','VoltaMaisRapida', 'PosChegada']

print (final_results_df)
#export results to csv
export_csv = final_results_df.to_csv('/home/rsjr/Dev/Kart/kart_result.csv', index = None, header=True)