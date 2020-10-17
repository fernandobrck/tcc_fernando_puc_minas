#importando a biblioteca pandas
from scipy.stats import poisson  
import pandas as pd
import numpy as np
import math
#importando dados para uma base
#https://www.kaggle.com/adaoduque/campeonato-brasileiro-de-futebol
data = pd.read_csv("D:\DATASETS\campeonato-brasileiro-full.csv",sep=',')
#importando os dados para um data frame
df = pd.DataFrame(data)
#imprimindo data frame
#print(df.loc[1])

df_pc2013 = df[df['Data'] >= '2013-01-01 00:00:00']
#df_pc2019 = df[df['Data'] >= '2019-01-01 00:00:00']
jogos = df_pc2013.copy()
#jogos = df_pc2019.copy()

jogos['Clube 1'] = jogos['Clube 1'].astype(str).str.lower() 
jogos['Clube 2'] = jogos['Clube 2'].astype(str).str.lower() 
jogos['Vencedor'] = jogos['Vencedor'].astype(str).str.lower()
jogos['Vencedor'] = jogos['Vencedor'].replace('-','empate')


#para conferencia
#todosTimes =  pd.concat([jogos['Clube 1'].str.lower(), jogos['Clube 2'].str.lower()], axis=1, keys=['Cb'])
#todosTimesLinha = pd.Series(todosTimes['Cb'].unique())
#todosTimesLinha = todosTimesLinha.to_frame()
#todosTimesLinha.to_csv('todosTimesLinha.csv', index = False, sep = ';')

def getVitoriasTotalAteOJogo(dados, time, datajogo):
    filter1 = dados["Vencedor"].str.lower() == time
    filter2 = dados["Data"] < datajogo
    df = dados[((filter1) & (filter2))]
    vitoria = df['Vencedor'].count()
    return vitoria.astype(np.int64)

def getVitoria(dados, time, datajogo,numerojogos,posicaojogo): #posicao dentro do corte d enumero de jogos
    filter1 = dados["Clube 1"].str.lower() == time 
    filter2 = dados["Clube 2"].str.lower() == time
    filter3 = dados["Data"] < datajogo
    df = dados[(filter3) & ((filter2) | (filter1))]
    df1 = df.sort_values(by='Data', ascending=False)
    df2 = df1.iloc[0:numerojogos]
    df3 = df2.sort_values(by='Data')
    df4 = df3.iloc[0:posicaojogo]
    filter4 = df4["Vencedor"].str.lower() == time
    dw = df4[(filter4)]
    vitoria = dw['Vencedor'].count()
    return vitoria.astype(np.int64)  

def getEmpate(dados, time, datajogo,numerojogos,posicaojogo):
    filter1 = dados["Clube 1"].str.lower() == time 
    filter2 = dados["Clube 2"].str.lower() == time
    filter3 = dados["Data"] < datajogo
    df = dados[(filter3) & ((filter2) | (filter1))]
    df1 = df.sort_values(by='Data', ascending=False)
    df2 = df1.iloc[0:numerojogos]
    df3 = df2.sort_values(by='Data')
    df4 = df3.iloc[0:posicaojogo]
    filter4 = df4["Vencedor"].str.lower() == 'empate'
    dw = df4[(filter4)]
    vitoria = dw['Vencedor'].count()
    return vitoria.astype(np.int64)  


def getDerrotasTotalAteOJogo(dados, time, datajogo):
    filter1 = dados["Clube 1"].str.lower() == time 
    filter2 = dados["Clube 2"].str.lower() == time
    filter3 = dados["Data"] < datajogo
    filter4 = dados["Vencedor"].str.lower() != 'empate'
    filter5 = dados["Vencedor"].str.lower() != time
    df = dados[(((filter1)|(filter2))&(filter3)&(filter4)&(filter5))]
    vitoria = df['Vencedor'].count()
    return vitoria.astype(np.int64)



def getEmpateTotalAteOJogo(dados, time, datajogo):
    filter1 = dados["Clube 1"].str.lower() == time 
    filter2 = dados["Clube 2"].str.lower() == time
    filter3 = dados["Data"] < datajogo
    filter4 = dados["Vencedor"].str.lower() == 'empate'
    df = dados[(((filter1)|(filter2))&(filter3)&(filter4))]
    vitoria = df['Vencedor'].count()
    return vitoria.astype(np.int64)

def getJogosAteOJogo(dados, time, datajogo):
    filter1 = dados["Clube 1"].str.lower() == time 
    filter2 = dados["Clube 2"].str.lower() == time
    filter3 = dados["Data"] < datajogo 
    return (dados[(filter1) & (filter3)]["Clube 1"].count() + dados[(filter2) & (filter3)]["Clube 2"].count()).astype(np.int64)    

def getTotalGeralJogosAteOJogo(dados, datajogo):
    filter3 = dados["Data"] < datajogo 
    return (dados[(filter3)]["Clube 1"].count()).astype(np.int64)    

def getTotalJogosMandante(dados, time, datajogo):
    filter1 = dados["Clube 1"].str.lower() == time 
    filter3 = dados["Data"] < datajogo 
    return (dados[(filter1) & (filter3)]["Clube 1"].count()).astype(np.int64)    

def getTotalJogosVisitante(dados, time, datajogo):
    filter2 = dados["Clube 2"].str.lower() == time
    filter3 = dados["Data"] < datajogo 
    return (dados[(filter2) & (filter3)]["Clube 2"].count()).astype(np.int64)    


def getGpGeral (dados, time, datajogo):
    filter1 = dados["Clube 1"].str.lower() == time 
    filter2 = dados["Clube 2"].str.lower() == time
    filter3 = dados["Data"] < datajogo 
    df1 = dados[(filter3) & ((filter2) | (filter1))]

 
    gp = 0
    gc = 0
  
    for index, row in df1.iterrows():
        if (row["Clube 1"] == time):
            golsPro = row['Clube 1 Gols']
            golsCtr = row['Clube 2 Gols']
        else:
            golsPro = row['Clube 2 Gols']
            golsCtr = row['Clube 1 Gols']
        gp = (gp + golsPro)
        gc = (gc + golsCtr)
    return gp, gc


def getGolsMandante (dados, time, datajogo):
    filter1 = dados["Clube 1"].str.lower() == time 
    filter3 = dados["Data"] < datajogo 
    df1 = dados[(filter3) & (filter1)]
    df12 = df1.sort_values(by='Data', ascending=False)
 
    gp = 0
    gc = 0
  
    for index, row in df12.iterrows():
        if (row["Clube 1"] == time):
            golsPro = row['Clube 1 Gols']
            golsCtr = row['Clube 2 Gols']
        else:
            golsPro = row['Clube 2 Gols']
            golsCtr = row['Clube 1 Gols']
        gp = (gp + golsPro)
        gc = (gc + golsCtr)
    return gp, gc

def getGolsTodosMandante (dados, datajogo):
    filter3 = dados["Data"] < datajogo 
    df1 = dados[(filter3)]
    df12 = df1.sort_values(by='Data', ascending=False)
 
    gp = 0
    gc = 0
  
    for index, row in df12.iterrows():
        golsPro = row['Clube 1 Gols']
        golsCtr = row['Clube 2 Gols']
        gp = (gp + golsPro)
        gc = (gc + golsCtr)
    return gp, gc

def getGolsTodosVisitante (dados, datajogo):
    filter3 = dados["Data"] < datajogo 
    df1 = dados[(filter3)]
    df12 = df1.sort_values(by='Data', ascending=False)
 
    gp = 0
    gc = 0
  
    for index, row in df12.iterrows():
        golsCtr = row['Clube 1 Gols']
        golsPro = row['Clube 2 Gols']
        gp = (gp + golsPro)
        gc = (gc + golsCtr)
    return gp, gc


def getGolsVisitante (dados, time, datajogo):
    filter2 = dados["Clube 2"].str.lower() == time
    filter3 = dados["Data"] < datajogo 
    df1 = dados[(filter3) & (filter2) ]
    df12 = df1.sort_values(by='Data', ascending=False)
 
    gp = 0
    gc = 0
  
    for index, row in df12.iterrows():
        if (row["Clube 1"] == time):
            golsPro = row['Clube 1 Gols']
            golsCtr = row['Clube 2 Gols']
        else:
            golsPro = row['Clube 2 Gols']
            golsCtr = row['Clube 1 Gols']
        gp = (gp + golsPro)
        gc = (gc + golsCtr)
    return gp, gc

def getPontosGeral(dados, time, datajogo):
    filter1 = dados["Clube 1"].str.lower() == time 
    filter2 = dados["Clube 2"].str.lower() == time
    filter3 = dados["Data"] < datajogo
    df = dados[(filter3) & ((filter2) | (filter1))]
    df1 = df.sort_values(by='Data', ascending=False)
    filter4 = df1["Vencedor"].str.lower() == time
    dw = df1[(filter4)]
    vitoria = dw['Vencedor'].count()
    
    df4 = dados[(filter3) & ((filter2) | (filter1))]
    df5 = df4.sort_values(by='Data', ascending=False)
    filter5 = df5["Vencedor"].str.lower() == 'empate'
    df7 = df5[(filter5)]
    empate = df7['Vencedor'].count()

    return ((vitoria*3)+empate).astype(np.int64)

COLUNAS = [
    'ID',
    'Data_Confronto',
    'Rodada',
    'Time_Casa',
    'Time_Visitante',
    'Gol_1',
    'Gol_2',

    'Razao_Vitoria_Time_Casa',
    'Razao_Vitoria_Time_Visitante',
    
    'Razao_Derrota_Time_Casa',
    'Razao_Derrota_Time_Visitante',
    
    'Razao_Empate_Time_Casa',
    'Razao_Empate_Time_Visitante',
    
    'Media_Gols_Time_Casa',
    'Media_Gols_Time_Visitante',
    'Media_Gols_Sofrido_Time_Casa',
    'Media_Gols_Sofrido_Time_Visitante',


    'Exp_Gols_Mandante_Final',
    'Exp_Gols_Visitante_Final',
    'Forma_Mandante',
    'Forma_Visitante',
    'Elo_Mandante',
    'Elo_Visitante',
    'Exp_Vitoria', #M = Mandante// V =Visitante// E = Empate 

    'Tipo_Vencedor',#M = Mandante// V =Visitante// E = Empate 
    'Vencedor'
]

df_final = pd.DataFrame(columns=COLUNAS)

contador = 0
#para utilizar no elo
cont_atl_mg = 0
cont_amr_mg = 0
cont_atl_pr = 0
cont_atl_go = 0
cont_avai = 0
cont_bahia = 0 
cont_barueri = 0
cont_botafogo = 0
cont_ceara = 0
cont_chapecoense = 0
cont_corinthians = 0
cont_coritiba    = 0
cont_criciuma    = 0
cont_cruzeiro    = 0
cont_csa         = 0
cont_figueirense = 0
cont_flamengo    = 0
cont_fluminense  = 0
cont_fortaleza   = 0
cont_goias       = 0
cont_gremio      = 0
cont_gremio_prudente = 0
cont_guarani         = 0
cont_internacional   = 0
cont_ipatinga        = 0
cont_joinville       = 0
cont_nautico         = 0
cont_palmeiras       = 0
cont_parana          = 0
cont_ponte_preta     = 0
cont_portuguesa      = 0
cont_santacruz      = 0
cont_santo_andre     = 0
cont_santos          = 0
cont_sao_paulo       = 0
cont_sporte           = 0
cont_vasco           = 0
cont_vitoria = 0

#fim para utilizar no elo

for index, row in jogos.iterrows():
    datajogo = row['Data']
    clube1 = row['Clube 1']
    clube2 = row['Clube 2']
    rodada = row['Rodada'].replace('ª Rodada','')
    Vencedor = row['Vencedor']
    gol1 = row['Clube 1 Gols']
    gol2 = row['Clube 2 Gols']
    
    indice = contador
    vitoriasAnterioresTimeCasa = getVitoriasTotalAteOJogo(jogos,clube1,datajogo)
    vitoriasAnterioresTimeFora = getVitoriasTotalAteOJogo(jogos,clube2,datajogo)
    jogosAnterioresCasa = getJogosAteOJogo(jogos,clube1, datajogo)
    jogosAnterioresFora = getJogosAteOJogo(jogos,clube2, datajogo)
    golsProGeralCasa, golsContraGeralCasa  = getGpGeral(jogos, clube1, datajogo)
    golsProGeralFora, golsContraGeralFora = getGpGeral(jogos, clube2, datajogo)
    derrotasTimeCasa = getDerrotasTotalAteOJogo(jogos,clube1,datajogo)
    derrotasTimeFora = getDerrotasTotalAteOJogo(jogos,clube2, datajogo)
    empateTimeCasa = getEmpateTotalAteOJogo(jogos,clube1,datajogo)
    empateTimeFora = getEmpateTotalAteOJogo(jogos,clube1,datajogo)
    if row['Vencedor'] == row['Clube 1']:
        Tipo_Vencedor = 'M'
    elif row['Vencedor'] == row['Clube 2']:
        Tipo_Vencedor = 'V'
    else:
        Tipo_Vencedor = 'E'


    Razao_Vitoria_Time_Casa = round((vitoriasAnterioresTimeCasa / jogosAnterioresCasa),4)
    Razao_Vitoria_Time_Visitante = round((vitoriasAnterioresTimeFora / jogosAnterioresFora ),4)
    Razao_Derrota_Time_Casa = round((derrotasTimeCasa / jogosAnterioresCasa),4)
    Razao_Derrota_Time_Visitante = round((derrotasTimeFora / jogosAnterioresFora),4)
    Razao_Empate_Time_Casa = round((empateTimeCasa / jogosAnterioresCasa),4)
    Razao_Empate_Time_Visitante = round((empateTimeFora / jogosAnterioresFora),4)


    Media_Gols_Time_Casa = round((golsProGeralCasa / jogosAnterioresCasa),4)
    Media_Gols_Time_Visitante = round((golsProGeralFora / jogosAnterioresFora),4)
    Media_Gols_Sofrido_Time_Casa = round((golsContraGeralCasa / jogosAnterioresCasa),4)
    Media_Gols_Sofrido_Time_Visitante = round((golsContraGeralFora / jogosAnterioresFora),4)

    #gm, gsm
    #Total_Gols_Feito_Mandante, Total_Gols_Sofridos_Mandante = getGolsMandante(jogos,clube1,datajogo)
    gm, gsm = getGolsMandante(jogos,clube1,datajogo)
    #gv, gsv
    #Total_Gols_Feito_Visitante, Total_Gols_Sofridos_Visitante = getGolsMandante(jogos,clube2,datajogo)
    gv, gsv = getGolsVisitante(jogos,clube2,datajogo)

    #tgm, tgsm
    #Total_Gols_Feitos_Todos_Mandantes, Total_Gols_Sofridos_Todos_Mandates = getGolsTodosMandante(jogos,datajogo)
    tgm, tgsm = getGolsTodosMandante(jogos,datajogo)
    #tgv, tgsv
    #Total_Gols_Feito_Todos_Visitante, Total_Gols_Sofridos_Todos_Visitantes = getGolsTodosVisitante(jogos,datajogo)
    tgv, tgsv = getGolsTodosVisitante(jogos,datajogo)

    #tpm
    #Total_Jogos_Como_Mandante = getTotalJogosMandante(jogos,clube1,datajogo)
    tpm = getTotalJogosMandante(jogos,clube1,datajogo)

    #tpv
    #Total_Jogos_Como_Visitante = getTotalJogosVisitante(jogos,clube2,datajogo)
    tpv = getTotalJogosVisitante(jogos,clube2,datajogo)

    #tp
    #Total_De_Partidas
    tp = getTotalGeralJogosAteOJogo(jogos,datajogo)

    
    alfa = ((gm / tpm) / (tgm / tp))
    beta = ((gsv / tpv)/(tgsv / tp))

    #expectativa gols mandante
    EGm = ((alfa * beta) * (tgm / tp))
    Exp_Gols_Mandante_Aux = EGm

    gama = ((gv / tpv)/(tgv/tp))
    omega = ((gsm/tpm)/(tgsm/tp))

    #expectativa de gols visitante
    EGv = ((gama * omega) * (tgv/tp))
    Exp_Gols_Visitante_Aux = EGv

    #expectativa gols mandante final
    
    EGm0 = poisson.pmf(0, EGm)
    EGm1 = poisson.pmf(1, EGm)
    EGm2 = poisson.pmf(2, EGm)
    EGm3 = poisson.pmf(3, EGm)
    EGm4 = poisson.pmf(4, EGm)
    EGm5 = poisson.pmf(5, EGm)
    EGm6 = poisson.pmf(6, EGm)
    EGm7 = poisson.pmf(7, EGm)

    EGmf_V = max(EGm0,EGm1,EGm2,EGm3,EGm4,EGm5,EGm6,EGm7)
    
    EGmf = 0

    if EGmf_V == EGm0:
        EGmf = 0
    elif EGmf_V == EGm1:
        EGmf = 1 
    elif EGmf_V == EGm2:
        EGmf = 2 
    elif EGmf_V == EGm3:
        EGmf = 3 
    elif EGmf_V == EGm4:
        EGmf = 4 
    elif EGmf_V == EGm5:
        EGmf = 5 
    elif EGmf_V == EGm6:
        EGmf = 6 
    elif EGmf_V == EGm7:
        EGmf = 7
    
    

    #expectativa de gols visitante
    
    EGv0 = poisson.pmf(0, EGv)
    EGv1 = poisson.pmf(1, EGv)
    EGv2 = poisson.pmf(2, EGv)
    EGv3 = poisson.pmf(3, EGv)
    EGv4 = poisson.pmf(4, EGv)
    EGv5 = poisson.pmf(5, EGv)
    EGv6 = poisson.pmf(6, EGv)
    EGv7 = poisson.pmf(7, EGv)

    EGvf_v = max(EGv0,EGv1,EGv2,EGv3,EGv4,EGv5,EGv6,EGv7)

    EGvf = 0
    if EGvf_v == EGv0:
        EGvf = 0
    elif EGvf_v == EGv1:
        EGvf = 1 
    elif EGvf_v == EGv2:
        EGvf = 2 
    elif EGvf_v == EGv3:
        EGvf = 3 
    elif EGvf_v == EGv4:
        EGvf = 4 
    elif EGvf_v == EGv5:
        EGvf = 5 
    elif EGvf_v == EGv6:
        EGvf = 6 
    elif EGvf_v == EGv7:
        EGvf = 7    

#alfa(i) = gm/tpm / tgm/tp
#beta = gsv/tpv / tgsv/tp
#gama = gv/tpv / tgv/tp
#omega = gsm/tpm / tgsm/tp

#EGm expectativa de gols MANDANTE: EGm = ALFA * BETA * (TGM/TP)
#EGv expectativa de gols VISITANTE: EGv = GAMA * OMEGA * (TGV/TP)

# poisson de EGm x poisson de EGv

    #expectativa de vitoria
    if EGmf > EGvf:
        Exp_Vitoria = 'M'
    elif EGmf < EGvf:
        Exp_Vitoria = 'V'
    else:
        Exp_Vitoria = 'E'

    ####ELO APLICADO AO FUTEBOL
    #ocorrido
    if Tipo_Vencedor == 'M':
        Wm = 1.0
        Wv = 0.0
    elif Tipo_Vencedor == 'V':
        Wm = 0.0
        Wv = 1.0
    else:
        Wm = 0.5
        Wv = 0.5
    
    #expectativa
    if Exp_Vitoria == 'E':
        Wpm = 0.5
        Wpv = 0.5
    elif Exp_Vitoria == 'M':
        Wpm = 1.0
        Wpv = 0.0
    else:
        Wpm = 0.0
        Wpv = 1.0
    difGols = gol1 - gol2
    difGols = abs(difGols)

    if difGols <= 1:
        G = 1.0
    elif difGols ==2:
        G = 1.5
    else:
        G = ((difGols + 11.00 ) / 8.00)
    ##########################################################################################################
    if cont_atl_mg == 0:
        Rt_Atletico_mg  = 996.80
    if cont_amr_mg == 0:	
        Rt_americamg  = 1001.02
    if cont_atl_pr == 0:
        Rt_athletico_pr  = 1001.02
    if cont_atl_go == 0:	
        Rt_atletico_go  = 1007.82
    if cont_avai == 0:	
        Rt_avai  = 1001.02
    if cont_bahia == 0:	
        Rt_bahia  = 1002.58
    if cont_barueri == 0:
        Rt_barueri  = 1001.02
    if cont_botafogo == 0: 	
        Rt_botafogo  = 998.46
    if cont_ceara == 0:	
        Rt_ceara  = 1001.02
    if cont_chapecoense == 0:	
        Rt_chapecoense  = 1001.02
    if cont_corinthians == 0:	
        Rt_cortinthians  = 1004.23
    if cont_coritiba == 0:	
        Rt_coritina  = 1001.71
    if cont_criciuma == 0:	
        Rt_criciuma  = 1001.02
    if cont_cruzeiro == 0:
        Rt_cruzeiro  = 997.27
    if cont_csa == 0:	
        Rt_csa  = 1001.02
    if cont_figueirense == 0:	
        Rt_figueirense  = 1001.85
    if cont_flamengo == 0:	
        Rt_flamento  = 995.34
    if cont_fluminense == 0:	
        Rt_fluminense  = 1002.06
    if cont_fortaleza == 0:	
        Rt_fortaleza  = 1001.02
    if cont_goias == 0:	
        Rt_goias  = 1001.02
    if cont_gremio == 0:	
        Rt_gremio  = 1001.70
    if cont_gremio_prudente == 0:	
        Rt_gremio_prudente  = 1001.02
    if cont_guarani == 0:	
        Rt_guarani  = 1001.02
    if cont_internacional == 0:	
        Rt_internacional  = 994.97
    if cont_ipatinga == 0:	
        Rt_ipatinga  = 1001.02
    if cont_joinville == 0:	
        Rt_joinville  = 1001.02
    if cont_nautico == 0:	
        Rt_nautico  = 1004.19
    if cont_palmeiras == 0:	
        Rt_palmeiras  = 993.74
    if cont_parana == 0:	
        Rt_parana  = 1001.02
    if cont_ponte_preta == 0:	
        Rt_ponte_preta  = 998.99
    if cont_portuguesa == 0:
        Rt_portuguesa  = 1001.69
    if cont_santacruz == 0:
        Rt_santacruz  = 1001.02
    if cont_santo_andre == 0:
        Rt_santoandre  = 1001.02
    if cont_santos == 0:
        Rt_santos  = 998.92
    if cont_sao_paulo == 0:
        Rt_saopaulo  = 1000.10
    if cont_sporte == 0:
        Rt_sporte  = 1005.59
    if cont_vasco == 0:
        Rt_vasco  = 996.38
    if cont_vitoria == 0:
        Rt_vitoria  = 1001.02
    

    if (clube1 == 'atlético-mg'):
        Rtm = Rt_Atletico_mg
    if (clube2 == 'atlético-mg'):
        Rtv = Rt_Atletico_mg
    if (clube1 == 'américa-mg'):
        Rtm = Rt_americamg
    if (clube2 == 'américa-mg'):
        Rtv = Rt_americamg
    if (clube1 == 'athlético-pr'):
        Rtm = Rt_athletico_pr
    if (clube2 == 'athlético-pr'):
        Rtv = Rt_athletico_pr
    if (clube1 == 'atlético-go'):
        Rtm = Rt_atletico_go
    if (clube2 == 'atlético-go'):
        Rtv = Rt_atletico_go
    if (clube1 == 'avaí'):
        Rtm = Rt_avai
    if (clube2 == 'avaí'):
        Rtv = Rt_avai
    if (clube1 == 'bahia'):
        Rtm = Rt_bahia
    if (clube2 == 'bahia'):
        Rtv = Rt_bahia
    if (clube1 == 'barueri'):
        Rtm = Rt_barueri
    if (clube2 == 'barueri'):
        Rtv = Rt_barueri
    if (clube1 == 'botafogo-rj'):
        Rtm = Rt_botafogo
    if (clube2 == 'botafogo-rj'):
        Rtv = Rt_botafogo
    if (clube1 == 'ceará'):
        Rtm = Rt_ceara
    if (clube2 == 'ceará'):
        Rtv = Rt_ceara
    if (clube1 == 'chapecoense'):
        Rtm = Rt_chapecoense
    if (clube2 == 'chapecoense'):
        Rtv = Rt_chapecoense
    if (clube1 == 'corinthians'):
        Rtm = Rt_cortinthians
    if (clube2 == 'corinthians'):
        Rtv = Rt_cortinthians
    if (clube1 == 'coritiba'):
        Rtm = Rt_coritina
    if (clube2 == 'coritiba'):
        Rtv = Rt_coritina
    if (clube1 == 'criciúma'):
        Rtm = Rt_criciuma
    if (clube2 == 'criciúma'):
        Rtv = Rt_criciuma
    if (clube1 == 'cruzeiro'):
        Rtm = Rt_cruzeiro
    if (clube2 == 'cruzeiro'):
        Rtv = Rt_cruzeiro
    if (clube1 == 'csa'):
        Rtm = Rt_csa
    if (clube2 == 'csa'):
        Rtv = Rt_csa
    if (clube1 == 'figueirense'):
        Rtm = Rt_figueirense
    if (clube2 == 'figueirense'):
        Rtv = Rt_figueirense
    if (clube1 == 'flamengo'):
        Rtm = Rt_flamento
    if (clube2 == 'flamengo'):
        Rtv = Rt_flamento
    if (clube1 == 'fluminense'):
        Rtm = Rt_fluminense
    if (clube2 == 'fluminense'):
        Rtv = Rt_fluminense
    if (clube1 == 'fortaleza'):
        Rtm = Rt_fortaleza
    if (clube2 == 'fortaleza'):
        Rtv = Rt_fortaleza
    if (clube1 == 'goiás'):
        Rtm = Rt_goias
    if (clube2 == 'goiás'):
        Rtv = Rt_goias
    if (clube1 == 'grêmio'):
        Rtm = Rt_gremio
    if (clube2 == 'grêmio'):
        Rtv = Rt_gremio
    if (clube1 == 'grêmio prudente'):
        Rtm = Rt_gremio_prudente
    if (clube2 == 'grêmio prudente'):
        Rtv = Rt_gremio_prudente
    if (clube1 == 'guarani'):
        Rtm = Rt_guarani
    if (clube2 == 'guarani'):
        Rtv = Rt_guarani
    if (clube1 == 'internacional'):
        Rtm = Rt_internacional
    if (clube2 == 'internacional'):
        Rtv = Rt_internacional
    if (clube1 == 'ipatinga'):
        Rtm = Rt_ipatinga
    if (clube2 == 'ipatinga'):
        Rtv = Rt_ipatinga
    if (clube1 == 'joinville'):
        Rtm = Rt_joinville
    if (clube2 == 'joinville'):
        Rtv = Rt_joinville
    if (clube1 == 'náutico'):
        Rtm = Rt_nautico
    if (clube2 == 'náutico'):
        Rtv = Rt_nautico
    if (clube1 == 'palmeiras'):
        Rtm = Rt_palmeiras
    if (clube2 == 'palmeiras'):
        Rtv = Rt_palmeiras
    if (clube1 == 'paraná'):
        Rtm = Rt_parana
    if (clube2 == 'paraná'):
        Rtv = Rt_parana
    if (clube1 == 'ponte preta'):
        Rtm = Rt_ponte_preta
    if (clube2 == 'ponte preta'):
        Rtv = Rt_ponte_preta
    if (clube1 == 'portuguesa'):
        Rtm = Rt_portuguesa
    if (clube2 == 'portuguesa'):
        Rtv = Rt_portuguesa
    if (clube1 == 'santa cruz'):
        Rtm = Rt_santacruz
    if (clube2 == 'santa cruz'):
        Rtv = Rt_santacruz
    if (clube1 == 'santo andré'):
        Rtm = Rt_santoandre
    if (clube2 == 'santo andré'):
        Rtv = Rt_santoandre
    if (clube1 == 'santos'):
        Rtm = Rt_santos
    if (clube2 == 'santos'):
        Rtv = Rt_santos
    if (clube1 == 'são paulo'):
        Rtm = Rt_saopaulo
    if (clube2 == 'são paulo'):
        Rtv = Rt_saopaulo
    if (clube1 == 'sport'):
        Rtm = Rt_sporte
    if (clube2 == 'sport'):
        Rtv = Rt_sporte
    if (clube1 == 'vasco'):
        Rtm = Rt_vasco
    if (clube2 == 'vasco'):
        Rtv = Rt_vasco
    if (clube1 == 'vitória'):
        Rtm = Rt_vitoria
    if (clube2 == 'vitória'):
        Rtv = Rt_vitoria
 

    Ram = Rtm + G * (Wm - Wpm)
    
    Rav = Rtv + G * (Wv - Wpv) 

    Validacao_Elo = 0

    
    if (clube1 == 'atlético-mg'):
        Rt_Atletico_mg = Ram
         
    if (clube2 == 'atlético-mg'):
        Rt_Atletico_mg = Rav
         

    if (clube1 == 'américa-mg'):
        Rt_americamg = Ram
         
    if (clube2 == 'américa-mg'):
        Rt_americamg = Rav
         
    if (clube1 == 'athlético-pr'):
        Rt_athletico_pr = Ram
         
    if (clube2 == 'athlético-pr'):
        Rt_athletico_pr = Rav
         
    if (clube1 == 'atlético-go'):
        Rt_atletico_go = Ram
         
    if (clube2 == 'atlético-go'):
        Rt_atletico_go = Rav
         
    if (clube1 == 'avaí'):
        Rt_avai = Ram
         
    if (clube2 == 'avaí'):
        Rt_avai = Rav
         
    if (clube1 == 'bahia'):
        Rt_bahia = Ram
         
    if (clube2 == 'bahia'):
        Rt_bahia = Rav
         
    if (clube1 == 'barueri'):
        Rt_barueri = Ram
         
    if (clube2 == 'barueri'):
        Rt_barueri = Rav
         
    if (clube1 == 'botafogo-rj'):
        Rt_botafogo = Ram
         
    if (clube2 == 'botafogo-rj'):
        Rt_botafogo = Rav
         
    if (clube1 == 'ceará'):
        Rt_ceara = Ram
         
    if (clube2 == 'ceará'):
        Rt_ceara = Rav
         
    if (clube1 == 'chapecoense'):
        Rt_chapecoense = Ram
         
    if (clube2 == 'chapecoense'):
        Rt_chapecoense = Rav
         
    if (clube1 == 'corinthians'):
        Rt_cortinthians = Ram
         
    if (clube2 == 'corinthians'):
        Rt_cortinthians = Rav
         
    if (clube1 == 'coritiba'):
        Rt_coritina = Ram
         
    if (clube2 == 'coritiba'):
        Rt_coritina = Rav
         
    if (clube1 == 'criciúma'):
        Rt_criciuma = Ram
         
    if (clube2 == 'criciúma'):
        Rt_criciuma = Rav
         
    if (clube1 == 'cruzeiro'):
        Rt_cruzeiro = Ram
         
    if (clube2 == 'cruzeiro'):
        Rt_cruzeiro = Rav
         
    if (clube1 == 'csa'):
        Rt_csa = Ram
         
    if (clube2 == 'csa'):
        Rt_csa = Rav
         
    if (clube1 == 'figueirense'):
        Rt_figueirense = Ram
         
    if (clube2 == 'figueirense'):
        Rt_figueirense = Rav
         
    if (clube1 == 'flamengo'):
        Rt_flamento = Ram
         
    if (clube2 == 'flamengo'):
        Rt_flamento = Rav
         
    if (clube1 == 'fluminense'):
        Rt_fluminense = Ram
         
    if (clube2 == 'fluminense'):
        Rt_fluminense = Rav
         
    if (clube1 == 'fortaleza'):
        Rt_fortaleza = Ram
         
    if (clube2 == 'fortaleza'):
        Rt_fortaleza = Rav
         
    if (clube1 == 'goiás'):
        Rt_goias = Ram
         
    if (clube2 == 'goiás'):
        Rt_goias = Rav
         
    if (clube1 == 'grêmio'):
        Rt_gremio = Ram
         
    if (clube2 == 'grêmio'):
        Rt_gremio = Rav
         
    if (clube1 == 'grêmio prudente'):
        Rt_gremio_prudente = Ram
         
    if (clube2 == 'grêmio prudente'):
        Rt_gremio_prudente = Rav
         
    if (clube1 == 'guarani'):
        Rt_guarani = Ram
         
    if (clube2 == 'guarani'):
        Rt_guarani = Rav
         
    if (clube1 == 'internacional'):
        Rt_internacional = Ram
         
    if (clube2 == 'internacional'):
        Rt_internacional = Rav
         
    if (clube1 == 'ipatinga'):
        Rt_ipatinga = Ram
         
    if (clube2 == 'ipatinga'):
        Rt_ipatinga = Rav
         
    if (clube1 == 'joinville'):
        Rt_joinville = Ram
         
    if (clube2 == 'joinville'):
        Rt_joinville = Rav
         
    if (clube1 == 'náutico'):
        Rt_nautico = Ram
         
    if (clube2 == 'náutico'):
        Rt_nautico = Rav
         
    if (clube1 == 'palmeiras'):
        Rt_palmeiras = Ram
         
    if (clube2 == 'palmeiras'):
        Rt_palmeiras = Rav
         
    if (clube1 == 'paraná'):
        Rt_parana = Ram
         
    if (clube2 == 'paraná'):
        Rt_parana = Rav
         
    if (clube1 == 'ponte preta'):
        Rt_ponte_preta = Ram
         
    if (clube2 == 'ponte preta'):
        Rt_ponte_preta = Rav
         
    if (clube1 == 'portuguesa'):
        Rt_portuguesa = Ram
         
    if (clube2 == 'portuguesa'):
        Rt_portuguesa = Rav
         
    if (clube1 == 'santa cruz'):
        Rt_santacruz = Ram
         
    if (clube2 == 'santa cruz'):
        Rt_santacruz = Rav
         
    if (clube1 == 'santo andré'):
        Rt_santoandre = Ram
         
    if (clube2 == 'santo andré'):
        Rt_santoandre = Rav
         
    if (clube1 == 'santos'):
        Rt_santos = Ram
         
    if (clube2 == 'santos'):
        Rt_santos = Rav
         
    if (clube1 == 'são paulo'):
        Rt_saopaulo = Ram
         
    if (clube2 == 'são paulo'):
        Rt_saopaulo = Rav
         
    if (clube1 == 'sport'):
        Rt_sporte = Ram
         
    if (clube2 == 'sport'):
        Rt_sporte = Rav
         
    if (clube1 == 'vasco'):
        Rt_vasco = Ram

    if (clube2 == 'vasco'):
        Rt_vasco = Rav

    if (clube1 == 'vitória'):
        Rt_vitoria = Ram
        
    if (clube2 == 'vitória'):
        Rt_vitoria   = Rav
        
    ##########################################################################################################
    # forma mandante
    forma_mandante_ultimojogo = 0
    forma_mandante_ultimojogo = (getVitoria(jogos,clube1,datajogo,1,1)) * 3
    if forma_mandante_ultimojogo == 0:
        forma_mandante_ultimojogo = getEmpate(jogos,clube1,datajogo,1,1)

    forma_mandante_penultimojogo = 0
    forma_mandante_penultimojogo = (getVitoria(jogos,clube1,datajogo,2,1)) * 3
    if forma_mandante_penultimojogo == 0:
        forma_mandante_penultimojogo = getEmpate(jogos,clube1,datajogo,2,1)

    forma_mandante_antepenultimojogo = 0
    forma_mandante_antepenultimojogo = (getVitoria(jogos,clube1,datajogo,3,1)) * 3
    if forma_mandante_antepenultimojogo == 0:
        forma_mandante_antepenultimojogo = getEmpate(jogos,clube1,datajogo,3,1)

    forma_mandante = (forma_mandante_ultimojogo * 3) + (forma_mandante_penultimojogo * 2) + (forma_mandante_antepenultimojogo)

    # forma visitante
    forma_visitante_ultimojogo = 0
    forma_visitante_ultimojogo = (getVitoria(jogos,clube2,datajogo,1,1)) * 3
    if forma_visitante_ultimojogo == 0:
        forma_visitante_ultimojogo = getEmpate(jogos,clube2,datajogo,1,1)

    forma_visitante_penultimojogo = 0
    forma_visitante_penultimojogo = (getVitoria(jogos,clube2,datajogo,2,1)) * 3
    if forma_visitante_penultimojogo == 0:
        forma_visitante_penultimojogo = getEmpate(jogos,clube1,datajogo,2,1)

    forma_visitante_antepenultimojogo = 0
    forma_visitante_antepenultimojogo = (getVitoria(jogos,clube2,datajogo,3,1)) * 3
    if forma_visitante_antepenultimojogo == 0:
        forma_visitante_antepenultimojogo = getEmpate(jogos,clube2,datajogo,3,1)

    forma_visitante = (forma_visitante_ultimojogo * 3) + (forma_visitante_penultimojogo * 2) + (forma_visitante_antepenultimojogo)


    

##########################################################################    
    if math.isnan(Razao_Vitoria_Time_Casa):
        Razao_Vitoria_Time_Casa = 0
    if math.isnan(Razao_Empate_Time_Casa):
        Razao_Empate_Time_Casa = 0
    if math.isnan(Razao_Derrota_Time_Casa):
        Razao_Derrota_Time_Casa = 0
    if math.isnan(Media_Gols_Time_Casa):
        Media_Gols_Time_Casa = 0
    if math.isnan(Media_Gols_Sofrido_Time_Casa):
        Media_Gols_Sofrido_Time_Casa = 0

    if math.isnan(Razao_Vitoria_Time_Visitante):
        Razao_Vitoria_Time_Visitante = 0
    if math.isnan(Razao_Empate_Time_Visitante):
        Razao_Empate_Time_Visitante = 0
    if math.isnan(Razao_Derrota_Time_Visitante):
        Razao_Derrota_Time_Visitante = 0
    if math.isnan(Media_Gols_Time_Visitante):
        Media_Gols_Time_Visitante = 0
    if math.isnan(Media_Gols_Sofrido_Time_Visitante):
        Media_Gols_Sofrido_Time_Visitante = 0      

    if math.isinf(Razao_Empate_Time_Visitante):
        Razao_Empate_Time_Visitante = 0      

    df_final.at[index,'Data_Confronto'] = datajogo
    df_final.at[index,'Rodada'] = rodada
    df_final.at[index,'ID'] = indice
    df_final.at[index,'Time_Casa'] = clube1
    df_final.at[index,'Time_Visitante'] = clube2
    df_final.at[index, 'Gol_1'] = gol1 
    df_final.at[index, 'Gol_2'] = gol2
    df_final.at[index,'Razao_Vitoria_Time_Casa'] = round(Razao_Vitoria_Time_Casa,4)
    df_final.at[index,'Razao_Vitoria_Time_Visitante'] = round(Razao_Vitoria_Time_Visitante,4)
    df_final.at[index,'Razao_Derrota_Time_Casa'] = round(Razao_Derrota_Time_Casa,4)
    df_final.at[index,'Razao_Derrota_Time_Visitante'] = round(Razao_Derrota_Time_Visitante,4)
    df_final.at[index,'Razao_Empate_Time_Casa'] = round(Razao_Empate_Time_Casa,4)
    df_final.at[index,'Razao_Empate_Time_Visitante'] = round(Razao_Empate_Time_Visitante,4)
    df_final.at[index,'Media_Gols_Time_Casa'] = round(Media_Gols_Time_Casa,4)
    df_final.at[index,'Media_Gols_Time_Visitante'] = round(Media_Gols_Time_Visitante,4)
    df_final.at[index,'Media_Gols_Sofrido_Time_Casa'] = round(Media_Gols_Sofrido_Time_Casa,4)
    df_final.at[index,'Media_Gols_Sofrido_Time_Visitante'] = round(Media_Gols_Sofrido_Time_Visitante,4)
    df_final.at[index, 'Forma_Mandante'] = forma_mandante
    df_final.at[index, 'Forma_Visitante'] = forma_visitante
    df_final.at[index,'Elo_Mandante'] = Ram
    df_final.at[index,'Elo_Visitante'] = Rav


    df_final.at[index,'Exp_Gols_Mandante_Final'] = EGmf
    df_final.at[index,'Exp_Gols_Visitante_Final'] = EGvf
    df_final.at[index,'Exp_Vitoria'] = Exp_Vitoria

    df_final.at[index,'Tipo_Vencedor'] = Tipo_Vencedor

    df_final.at[index,'Vencedor'] = Vencedor

    contador = contador + 1

    if (clube1 == 'atlético-mg' or clube2 == 'atlético-mg'):
        cont_atl_mg = cont_atl_mg + 1
    if (clube1 == 'américa-mg' or clube2 == 'américa-mg'):
        cont_amr_mg = cont_amr_mg + 1
    if (clube1 == 'athlético-pr' or clube2 == 'athlético-pr'):
        cont_atl_pr = cont_atl_pr + 1
    if (clube1 == 'atlético-go' or clube2 == 'atlético-go'):
        cont_atl_go = cont_atl_go + 1
    if (clube1 == 'avaí' or clube2 == 'avaí'):
        cont_avai = cont_avai + 1 
    if (clube1 == 'bahia' or clube2 == 'bahia'):
        cont_bahia = cont_bahia + 1
    if (clube1 == 'barueri' or clube2 == 'barueri'):
        cont_barueri = cont_barueri + 1
    if (clube1 == 'botafogo-rj' or clube2 == 'botafogo-rj'):
        cont_botafogo = cont_botafogo + 1
    if (clube1 == 'ceará' or clube2 == 'ceará'):
        cont_ceara = cont_ceara + 1
    if (clube1 == 'chapecoense' or clube2 == 'chapecoense'):
        cont_chapecoense = cont_chapecoense + 1
    if (clube1 == 'corinthians' or clube2 == 'corinthians'):
        cont_corinthians = cont_corinthians + 1
    if (clube1 == 'coritiba' or clube2 == 'coritiba'):
        cont_coritiba = cont_coritiba + 1 
    if (clube1 == 'criciúma' or clube2 == 'criciúma'):
        cont_criciuma = cont_criciuma + 1
    if (clube1 == 'cruzeiro' or clube2 == 'cruzeiro'):
        cont_cruzeiro = cont_cruzeiro + 1 
    if (clube1 == 'csa' or clube2 == 'csa'):
        cont_csa = cont_csa + 1
    if (clube1 == 'figueirense' or clube2 == 'figueirense'):
        cont_figueirense = cont_figueirense + 1
    if (clube1 == 'flamengo' or clube2 == 'flamengo'):
        cont_flamengo = cont_flamengo + 1
    if (clube1 == 'fluminense' or clube2 == 'fluminense'):
        cont_fluminense = cont_fluminense + 1
    if (clube1 == 'fortaleza' or clube2 == 'fortaleza'):
        cont_fortaleza = cont_fortaleza + 1 
    if (clube1 == 'goiás' or clube2 == 'goiás'):
        cont_goias = cont_goias + 1
    if (clube1 == 'grêmio' or clube2 == 'grêmio'):
        cont_gremio = cont_gremio + 1
    if (clube1 == 'grêmio prudente' or clube2 == 'grêmio prudente'):
        cont_gremio_prudente = cont_gremio_prudente + 1
    if (clube1 == 'guarani' or clube2 == 'guarani'):
        cont_guarani = cont_guarani + 1
    if (clube1 == 'internacional' or clube2 == 'internacional'):
        cont_internacional = cont_internacional + 1
    if (clube1 == 'ipatinga' or clube2 == 'ipatinga'):
        cont_ipatinga = cont_ipatinga + 1
    if (clube1 == 'joinville' or clube2 == 'joinville'):
        cont_joinville = cont_joinville + 1
    if (clube1 == 'náutico' or clube2 == 'náutico'):
        cont_nautico = cont_nautico + 1
    if (clube1 == 'palmeiras' or clube2 == 'palmeiras'):
        cont_palmeiras = cont_palmeiras + 1
    if (clube1 == 'paraná' or clube2 == 'paraná'):
        cont_parana = cont_parana + 1
    if (clube1 == 'ponte preta' or clube2 == 'ponte preta'):
        cont_ponte_preta = cont_ponte_preta + 1
    if (clube1 == 'portuguesa' or clube2 == 'portuguesa'):
        cont_portuguesa = cont_portuguesa + 1
    if (clube1 == 'santa cruz' or clube2 == 'santa cruz'):
        cont_santacruz = cont_santacruz + 1
    if (clube1 == 'santo andré' or clube2 == 'santo andré'):
        cont_santo_andre = cont_santo_andre + 1
    if (clube1 == 'santos' or clube2 == 'santos'):
        cont_santos = cont_santos + 1
    if (clube1 == 'são paulo' or clube2 == 'são paulo'):
        cont_sao_paulo = cont_sao_paulo + 1
    if (clube1 == 'sport' or clube2 == 'sport'):
        cont_sporte = cont_sporte + 1
    if (clube1 == 'vasco' or clube2 == 'vasco'):
        cont_vasco = cont_vasco + 1
    if (clube1 == 'vitória' or clube2 == 'vitória'):
        cont_vitoria = cont_vitoria + 1

    print(contador)

print(df_final)



df_final_tocsv = df_final[df_final['Data_Confronto'] >= '2014-01-01 00:00:00']


df_final_tocsv.to_csv('Dados_Tratados_completo_v2.csv', index = False, sep = ';')

