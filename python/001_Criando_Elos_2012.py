#importando a biblioteca pandas
from scipy.stats import poisson  
import pandas as pd
import numpy as np
#importando dados para uma base
#https://www.kaggle.com/adaoduque/campeonato-brasileiro-de-futebol
data = pd.read_csv("D:\DATASETS\campeonato-brasileiro-full.csv",sep=',')
#importando os dados para um data frame
df = pd.DataFrame(data)
#imprimindo data frame
#print(df.loc[1])

df_pc2008_1 = df[df['Data'] >= '2012-01-01 00:00:00']
df_pc2008 = df_pc2008_1[df_pc2008_1['Data'] < '2013-01-01 00:00:00']
jogos = df_pc2008.copy()

jogos['Clube 1'] = jogos['Clube 1'].astype(str).str.lower() 
jogos['Clube 2'] = jogos['Clube 2'].astype(str).str.lower() 
jogos['Vencedor'] = jogos['Vencedor'].astype(str).str.lower()
jogos['Vencedor'] = jogos['Vencedor'].replace('-','empate')



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


def getVitoriasTotalAteOJogo(dados, time, datajogo):
    filter1 = dados["Vencedor"].str.lower() == time
    filter2 = dados["Data"] < datajogo
    df = dados[((filter1) & (filter2))]
    vitoria = df['Vencedor'].count()
    return vitoria.astype(np.int64)

def getVitoriaTipoTotalAteOJogo(dados, time, datajogo, tipo):
    if tipo == 'C':
        filter1 = dados["Clube 1"].str.lower() == time 
    else:
        filter1 = dados["Clube 2"].str.lower() == time
  
    filter2 = dados["Data"] < datajogo
    filter3 = dados["Vencedor"].str.lower() == time
    df = dados[((filter1)&(filter2)&(filter3))]
    vitoria = df['Vencedor'].count()
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

def getDerrotasTipoTotalAteOJogo(dados, time, datajogo, tipo):
    if tipo == 'C':
        filter1 = dados["Clube 1"].str.lower() == time 
    else:
        filter1 = dados["Clube 2"].str.lower() == time
    filter3 = dados["Data"] < datajogo
    filter4 = dados["Vencedor"].str.lower() != 'empate'
    filter5 = dados["Vencedor"].str.lower() != time
    df = dados[(((filter1))&(filter3)&(filter4)&(filter5))]
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

def getEmpateTipoTotalAteOJogo(dados, time, datajogo, Tipo):
    if tipo == 'C':
        filter1 = dados["Clube 1"].str.lower() == time
    else:
        filter1 = dados["Clube 2"].str.lower() == time
    filter3 = dados["Data"] < datajogo
    filter4 = dados["Vencedor"].str.lower() == 'empate'
    df = dados[(((filter1))&(filter3)&(filter4))]
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

def getUltimosJogos(dados, time, datajogo,numerojogos):
    filter1 = dados["Clube 1"].str.lower() == time 
    filter2 = dados["Clube 2"].str.lower() == time
    filter3 = dados["Data"] < datajogo
    df = dados[(filter3) & ((filter2) | (filter1))]
    df1 = df.sort_values(by='Data', ascending=False)
    df2 = df1.iloc[0:numerojogos]
    filter4 = df2["Vencedor"].str.lower() == time
    dw = df2[(filter4)]
    vitoria = dw['Vencedor'].count()
    return vitoria.astype(np.int64)

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
    'Time_Casa',
    'Time_Visitante',
    'Gol_1',
    'Gol_2',

    'Tipo_Vencedor',#M = Mandante// V =Visitante// E = Empate 
    'Elo_Mandante',
    'Elo_Visitante',
    'Validacao_Elo',
    'Vencedor'
]

df_final = pd.DataFrame(columns=COLUNAS)

contador = 0
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




for index, row in jogos.iterrows():
    datajogo = row['Data']
    clube1 = row['Clube 1']
    clube2 = row['Clube 2']
    Vencedor = row['Vencedor']
    gol1 = row['Clube 1 Gols']
    gol2 = row['Clube 2 Gols']
    indice = contador
    if row['Vencedor'] == row['Clube 1']:
        Tipo_Vencedor = 'M'
    elif row['Vencedor'] == row['Clube 2']:
        Tipo_Vencedor = 'V'
    else:
        Tipo_Vencedor = 'E'

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

    #Rtm = valor do elo anterior
    # if rtm

    Rtm = 0 #temporario até cubrir todos os times
    Rtv = 0 #temporario até cubrir todos os times
    if cont_atl_mg == 0:
        Rt_Atletico_mg = 1000.37
    if cont_amr_mg == 0:	
        Rt_americamg =998.76
    if cont_atl_pr == 0:
        Rt_athletico_pr = 1009.25
    if cont_atl_go == 0:	
        Rt_atletico_go = 1004.28
    if cont_avai == 0:	
        Rt_avai = 999.89
    if cont_bahia == 0:	
        Rt_bahia = 997.41
    if cont_barueri == 0:
        Rt_barueri = 995.21
    if cont_botafogo == 0: 	
        Rt_botafogo = 999.45
    if cont_ceara == 0:	
        Rt_ceara = 1000.13
    if cont_chapecoense == 0:	
        Rt_chapecoense = 1000
    if cont_corinthians == 0:	
        Rt_cortinthians = 999.04
    if cont_coritiba == 0:	
        Rt_coritina = 1001.51
    if cont_criciuma == 0:	
        Rt_criciuma = 1000
    if cont_cruzeiro == 0:
        Rt_cruzeiro = 999.09
    if cont_csa == 0:	
        Rt_csa = 1000
    if cont_figueirense == 0:	
        Rt_figueirense = 1002.81
    if cont_flamengo == 0:	
        Rt_flamento = 993.93
    if cont_fluminense == 0:	
        Rt_fluminense = 1007.82
    if cont_fortaleza == 0:	
        Rt_fortaleza = 1000
    if cont_goias == 0:	
        Rt_goias = 1000.26
    if cont_gremio == 0:	
        Rt_gremio = 1001.87
    if cont_gremio_prudente == 0:	
        Rt_gremio_prudente = 995.21
    if cont_guarani == 0:	
        Rt_guarani =1000.66
    if cont_internacional == 0:	
        Rt_internacional = 999.84
    if cont_ipatinga == 0:	
        Rt_ipatinga =1000
    if cont_joinville == 0:	
        Rt_joinville = 1000
    if cont_nautico == 0:	
        Rt_nautico =1003.11
    if cont_palmeiras == 0:	
        Rt_palmeiras = 990.80
    if cont_parana == 0:	
        Rt_parana =1000
    if cont_ponte_preta == 0:	
        Rt_ponte_preta = 1003.11
    if cont_portuguesa == 0:
        Rt_portuguesa = 1003.11
    if cont_santacruz == 0:
        Rt_santacruz = 1000
    if cont_santo_andre == 0:
        Rt_santoandre = 1000.45
    if cont_santos == 0:
        Rt_santos = 995.90
    if cont_sao_paulo == 0:
        Rt_saopaulo = 998.62
    if cont_sporte == 0:
        Rt_sporte = 1003.11
    if cont_vasco == 0:
        Rt_vasco = 1000.29
    if cont_vitoria == 0:
        Rt_vitoria = 997.52
    

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
        Validacao_Elo = ' Rtm :' + str(Rtm) + ' G: ' + str(G) + ' Wm: ' + str(Wm) + ' Wpm: ' + str(Wpm) + ' Dif gols: ' +str(difGols)
    if (clube2 == 'atlético-mg'):
        Rt_Atletico_mg = Rav
        Validacao_Elo = ' Rtv :' + str(Rtv) + ' G: ' + str(G) + ' Wv: ' + str(Wv) + ' Wpv: ' + str(Wpv)+ ' Dif gols: ' +str(difGols)

    if (clube1 == 'américa-mg'):
        Rt_americamg = Ram
        Validacao_Elo = ' Rtm :' + str(Rtm) + ' G: ' + str(G) + ' Wm: ' + str(Wm) + ' Wpm: ' + str(Wpm) + ' Dif gols: ' +str(difGols)
    if (clube2 == 'américa-mg'):
        Rt_americamg = Rav
        Validacao_Elo = ' Rtv :' + str(Rtv) + ' G: ' + str(G) + ' Wv: ' + str(Wv) + ' Wpv: ' + str(Wpv)+ ' Dif gols: ' +str(difGols)
    if (clube1 == 'athlético-pr'):
        Rt_athletico_pr = Ram
        Validacao_Elo = ' Rtm :' + str(Rtm) + ' G: ' + str(G) + ' Wm: ' + str(Wm) + ' Wpm: ' + str(Wpm) + ' Dif gols: ' +str(difGols)
    if (clube2 == 'athlético-pr'):
        Rt_athletico_pr = Rav
        Validacao_Elo = ' Rtv :' + str(Rtv) + ' G: ' + str(G) + ' Wv: ' + str(Wv) + ' Wpv: ' + str(Wpv)+ ' Dif gols: ' +str(difGols)
    if (clube1 == 'atlético-go'):
        Rt_atletico_go = Ram
        Validacao_Elo = ' Rtm :' + str(Rtm) + ' G: ' + str(G) + ' Wm: ' + str(Wm) + ' Wpm: ' + str(Wpm) + ' Dif gols: ' +str(difGols)
    if (clube2 == 'atlético-go'):
        Rt_atletico_go = Rav
        Validacao_Elo = ' Rtv :' + str(Rtv) + ' G: ' + str(G) + ' Wv: ' + str(Wv) + ' Wpv: ' + str(Wpv)+ ' Dif gols: ' +str(difGols)
    if (clube1 == 'avaí'):
        Rt_avai = Ram
        Validacao_Elo = ' Rtm :' + str(Rtm) + ' G: ' + str(G) + ' Wm: ' + str(Wm) + ' Wpm: ' + str(Wpm) + ' Dif gols: ' +str(difGols)
    if (clube2 == 'avaí'):
        Rt_avai = Rav
        Validacao_Elo = ' Rtv :' + str(Rtv) + ' G: ' + str(G) + ' Wv: ' + str(Wv) + ' Wpv: ' + str(Wpv)+ ' Dif gols: ' +str(difGols)
    if (clube1 == 'bahia'):
        Rt_bahia = Ram
        Validacao_Elo = ' Rtm :' + str(Rtm) + ' G: ' + str(G) + ' Wm: ' + str(Wm) + ' Wpm: ' + str(Wpm) + ' Dif gols: ' +str(difGols)
    if (clube2 == 'bahia'):
        Rt_bahia = Rav
        Validacao_Elo = ' Rtv :' + str(Rtv) + ' G: ' + str(G) + ' Wv: ' + str(Wv) + ' Wpv: ' + str(Wpv)+ ' Dif gols: ' +str(difGols)
    if (clube1 == 'barueri'):
        Rt_barueri = Ram
        Validacao_Elo = ' Rtm :' + str(Rtm) + ' G: ' + str(G) + ' Wm: ' + str(Wm) + ' Wpm: ' + str(Wpm) + ' Dif gols: ' +str(difGols)
    if (clube2 == 'barueri'):
        Rt_barueri = Rav
        Validacao_Elo = ' Rtv :' + str(Rtv) + ' G: ' + str(G) + ' Wv: ' + str(Wv) + ' Wpv: ' + str(Wpv)+ ' Dif gols: ' +str(difGols)
    if (clube1 == 'botafogo-rj'):
        Rt_botafogo = Ram
        Validacao_Elo = ' Rtm :' + str(Rtm) + ' G: ' + str(G) + ' Wm: ' + str(Wm) + ' Wpm: ' + str(Wpm) + ' Dif gols: ' +str(difGols)
    if (clube2 == 'botafogo-rj'):
        Rt_botafogo = Rav
        Validacao_Elo = ' Rtv :' + str(Rtv) + ' G: ' + str(G) + ' Wv: ' + str(Wv) + ' Wpv: ' + str(Wpv)+ ' Dif gols: ' +str(difGols)
    if (clube1 == 'ceará'):
        Rt_ceara = Ram
        Validacao_Elo = ' Rtm :' + str(Rtm) + ' G: ' + str(G) + ' Wm: ' + str(Wm) + ' Wpm: ' + str(Wpm) + ' Dif gols: ' +str(difGols)
    if (clube2 == 'ceará'):
        Rt_ceara = Rav
        Validacao_Elo = ' Rtv :' + str(Rtv) + ' G: ' + str(G) + ' Wv: ' + str(Wv) + ' Wpv: ' + str(Wpv)+ ' Dif gols: ' +str(difGols)
    if (clube1 == 'chapecoense'):
        Rt_chapecoense = Ram
        Validacao_Elo = ' Rtm :' + str(Rtm) + ' G: ' + str(G) + ' Wm: ' + str(Wm) + ' Wpm: ' + str(Wpm) + ' Dif gols: ' +str(difGols)
    if (clube2 == 'chapecoense'):
        Rt_chapecoense = Rav
        Validacao_Elo = ' Rtv :' + str(Rtv) + ' G: ' + str(G) + ' Wv: ' + str(Wv) + ' Wpv: ' + str(Wpv)+ ' Dif gols: ' +str(difGols)
    if (clube1 == 'corinthians'):
        Rt_cortinthians = Ram
        Validacao_Elo = ' Rtm :' + str(Rtm) + ' G: ' + str(G) + ' Wm: ' + str(Wm) + ' Wpm: ' + str(Wpm) + ' Dif gols: ' +str(difGols)
    if (clube2 == 'corinthians'):
        Rt_cortinthians = Rav
        Validacao_Elo = ' Rtv :' + str(Rtv) + ' G: ' + str(G) + ' Wv: ' + str(Wv) + ' Wpv: ' + str(Wpv)+ ' Dif gols: ' +str(difGols)
    if (clube1 == 'coritiba'):
        Rt_coritina = Ram
        Validacao_Elo = ' Rtm :' + str(Rtm) + ' G: ' + str(G) + ' Wm: ' + str(Wm) + ' Wpm: ' + str(Wpm) + ' Dif gols: ' +str(difGols)
    if (clube2 == 'coritiba'):
        Rt_coritina = Rav
        Validacao_Elo = ' Rtv :' + str(Rtv) + ' G: ' + str(G) + ' Wv: ' + str(Wv) + ' Wpv: ' + str(Wpv)+ ' Dif gols: ' +str(difGols)
    if (clube1 == 'criciúma'):
        Rt_criciuma = Ram
        Validacao_Elo = ' Rtm :' + str(Rtm) + ' G: ' + str(G) + ' Wm: ' + str(Wm) + ' Wpm: ' + str(Wpm) + ' Dif gols: ' +str(difGols)
    if (clube2 == 'criciúma'):
        Rt_criciuma = Rav
        Validacao_Elo = ' Rtv :' + str(Rtv) + ' G: ' + str(G) + ' Wv: ' + str(Wv) + ' Wpv: ' + str(Wpv)+ ' Dif gols: ' +str(difGols)
    if (clube1 == 'cruzeiro'):
        Rt_cruzeiro = Ram
        Validacao_Elo = ' Rtm :' + str(Rtm) + ' G: ' + str(G) + ' Wm: ' + str(Wm) + ' Wpm: ' + str(Wpm) + ' Dif gols: ' +str(difGols)
    if (clube2 == 'cruzeiro'):
        Rt_cruzeiro = Rav
        Validacao_Elo = ' Rtv :' + str(Rtv) + ' G: ' + str(G) + ' Wv: ' + str(Wv) + ' Wpv: ' + str(Wpv)+ ' Dif gols: ' +str(difGols)
    if (clube1 == 'csa'):
        Rt_csa = Ram
        Validacao_Elo = ' Rtm :' + str(Rtm) + ' G: ' + str(G) + ' Wm: ' + str(Wm) + ' Wpm: ' + str(Wpm) + ' Dif gols: ' +str(difGols)
    if (clube2 == 'csa'):
        Rt_csa = Rav
        Validacao_Elo = ' Rtv :' + str(Rtv) + ' G: ' + str(G) + ' Wv: ' + str(Wv) + ' Wpv: ' + str(Wpv)+ ' Dif gols: ' +str(difGols)
    if (clube1 == 'figueirense'):
        Rt_figueirense = Ram
        Validacao_Elo = ' Rtm :' + str(Rtm) + ' G: ' + str(G) + ' Wm: ' + str(Wm) + ' Wpm: ' + str(Wpm) + ' Dif gols: ' +str(difGols)
    if (clube2 == 'figueirense'):
        Rt_figueirense = Rav
        Validacao_Elo = ' Rtv :' + str(Rtv) + ' G: ' + str(G) + ' Wv: ' + str(Wv) + ' Wpv: ' + str(Wpv)+ ' Dif gols: ' +str(difGols)
    if (clube1 == 'flamengo'):
        Rt_flamento = Ram
        Validacao_Elo = ' Rtm :' + str(Rtm) + ' G: ' + str(G) + ' Wm: ' + str(Wm) + ' Wpm: ' + str(Wpm) + ' Dif gols: ' +str(difGols)
    if (clube2 == 'flamengo'):
        Rt_flamento = Rav
        Validacao_Elo = ' Rtv :' + str(Rtv) + ' G: ' + str(G) + ' Wv: ' + str(Wv) + ' Wpv: ' + str(Wpv)+ ' Dif gols: ' +str(difGols)
    if (clube1 == 'fluminense'):
        Rt_fluminense = Ram
        Validacao_Elo = ' Rtm :' + str(Rtm) + ' G: ' + str(G) + ' Wm: ' + str(Wm) + ' Wpm: ' + str(Wpm) + ' Dif gols: ' +str(difGols)
    if (clube2 == 'fluminense'):
        Rt_fluminense = Rav
        Validacao_Elo = ' Rtv :' + str(Rtv) + ' G: ' + str(G) + ' Wv: ' + str(Wv) + ' Wpv: ' + str(Wpv)+ ' Dif gols: ' +str(difGols)
    if (clube1 == 'fortaleza'):
        Rt_fortaleza = Ram
        Validacao_Elo = ' Rtm :' + str(Rtm) + ' G: ' + str(G) + ' Wm: ' + str(Wm) + ' Wpm: ' + str(Wpm) + ' Dif gols: ' +str(difGols)
    if (clube2 == 'fortaleza'):
        Rt_fortaleza = Rav
        Validacao_Elo = ' Rtv :' + str(Rtv) + ' G: ' + str(G) + ' Wv: ' + str(Wv) + ' Wpv: ' + str(Wpv)+ ' Dif gols: ' +str(difGols)
    if (clube1 == 'goiás'):
        Rt_goias = Ram
        Validacao_Elo = ' Rtm :' + str(Rtm) + ' G: ' + str(G) + ' Wm: ' + str(Wm) + ' Wpm: ' + str(Wpm) + ' Dif gols: ' +str(difGols)
    if (clube2 == 'goiás'):
        Rt_goias = Rav
        Validacao_Elo = ' Rtv :' + str(Rtv) + ' G: ' + str(G) + ' Wv: ' + str(Wv) + ' Wpv: ' + str(Wpv)+ ' Dif gols: ' +str(difGols)
    if (clube1 == 'grêmio'):
        Rt_gremio = Ram
        Validacao_Elo = ' Rtm :' + str(Rtm) + ' G: ' + str(G) + ' Wm: ' + str(Wm) + ' Wpm: ' + str(Wpm) + ' Dif gols: ' +str(difGols)
    if (clube2 == 'grêmio'):
        Rt_gremio = Rav
        Validacao_Elo = ' Rtv :' + str(Rtv) + ' G: ' + str(G) + ' Wv: ' + str(Wv) + ' Wpv: ' + str(Wpv)+ ' Dif gols: ' +str(difGols)
    if (clube1 == 'grêmio prudente'):
        Rt_gremio_prudente = Ram
        Validacao_Elo = ' Rtm :' + str(Rtm) + ' G: ' + str(G) + ' Wm: ' + str(Wm) + ' Wpm: ' + str(Wpm) + ' Dif gols: ' +str(difGols)
    if (clube2 == 'grêmio prudente'):
        Rt_gremio_prudente = Rav
        Validacao_Elo = ' Rtv :' + str(Rtv) + ' G: ' + str(G) + ' Wv: ' + str(Wv) + ' Wpv: ' + str(Wpv)+ ' Dif gols: ' +str(difGols)
    if (clube1 == 'guarani'):
        Rt_guarani = Ram
        Validacao_Elo = ' Rtm :' + str(Rtm) + ' G: ' + str(G) + ' Wm: ' + str(Wm) + ' Wpm: ' + str(Wpm) + ' Dif gols: ' +str(difGols)
    if (clube2 == 'guarani'):
        Rt_guarani = Rav
        Validacao_Elo = ' Rtv :' + str(Rtv) + ' G: ' + str(G) + ' Wv: ' + str(Wv) + ' Wpv: ' + str(Wpv)+ ' Dif gols: ' +str(difGols)
    if (clube1 == 'internacional'):
        Rt_internacional = Ram
        Validacao_Elo = ' Rtm :' + str(Rtm) + ' G: ' + str(G) + ' Wm: ' + str(Wm) + ' Wpm: ' + str(Wpm) + ' Dif gols: ' +str(difGols)
    if (clube2 == 'internacional'):
        Rt_internacional = Rav
        Validacao_Elo = ' Rtv :' + str(Rtv) + ' G: ' + str(G) + ' Wv: ' + str(Wv) + ' Wpv: ' + str(Wpv)+ ' Dif gols: ' +str(difGols)
    if (clube1 == 'ipatinga'):
        Rt_ipatinga = Ram
        Validacao_Elo = ' Rtm :' + str(Rtm) + ' G: ' + str(G) + ' Wm: ' + str(Wm) + ' Wpm: ' + str(Wpm) + ' Dif gols: ' +str(difGols)
    if (clube2 == 'ipatinga'):
        Rt_ipatinga = Rav
        Validacao_Elo = ' Rtv :' + str(Rtv) + ' G: ' + str(G) + ' Wv: ' + str(Wv) + ' Wpv: ' + str(Wpv)+ ' Dif gols: ' +str(difGols)
    if (clube1 == 'joinville'):
        Rt_joinville = Ram
        Validacao_Elo = ' Rtm :' + str(Rtm) + ' G: ' + str(G) + ' Wm: ' + str(Wm) + ' Wpm: ' + str(Wpm) + ' Dif gols: ' +str(difGols)
    if (clube2 == 'joinville'):
        Rt_joinville = Rav
        Validacao_Elo = ' Rtv :' + str(Rtv) + ' G: ' + str(G) + ' Wv: ' + str(Wv) + ' Wpv: ' + str(Wpv)+ ' Dif gols: ' +str(difGols)
    if (clube1 == 'náutico'):
        Rt_nautico = Ram
        Validacao_Elo = ' Rtm :' + str(Rtm) + ' G: ' + str(G) + ' Wm: ' + str(Wm) + ' Wpm: ' + str(Wpm) + ' Dif gols: ' +str(difGols)
    if (clube2 == 'náutico'):
        Rt_nautico = Rav
        Validacao_Elo = ' Rtv :' + str(Rtv) + ' G: ' + str(G) + ' Wv: ' + str(Wv) + ' Wpv: ' + str(Wpv)+ ' Dif gols: ' +str(difGols)
    if (clube1 == 'palmeiras'):
        Rt_palmeiras = Ram
        Validacao_Elo = ' Rtm :' + str(Rtm) + ' G: ' + str(G) + ' Wm: ' + str(Wm) + ' Wpm: ' + str(Wpm) + ' Dif gols: ' +str(difGols)
    if (clube2 == 'palmeiras'):
        Rt_palmeiras = Rav
        Validacao_Elo = ' Rtv :' + str(Rtv) + ' G: ' + str(G) + ' Wv: ' + str(Wv) + ' Wpv: ' + str(Wpv)+ ' Dif gols: ' +str(difGols)
    if (clube1 == 'paraná'):
        Rt_parana = Ram
        Validacao_Elo = ' Rtm :' + str(Rtm) + ' G: ' + str(G) + ' Wm: ' + str(Wm) + ' Wpm: ' + str(Wpm) + ' Dif gols: ' +str(difGols)
    if (clube2 == 'paraná'):
        Rt_parana = Rav
        Validacao_Elo = ' Rtv :' + str(Rtv) + ' G: ' + str(G) + ' Wv: ' + str(Wv) + ' Wpv: ' + str(Wpv)+ ' Dif gols: ' +str(difGols)
    if (clube1 == 'ponte preta'):
        Rt_ponte_preta = Ram
        Validacao_Elo = ' Rtm :' + str(Rtm) + ' G: ' + str(G) + ' Wm: ' + str(Wm) + ' Wpm: ' + str(Wpm) + ' Dif gols: ' +str(difGols)
    if (clube2 == 'ponte preta'):
        Rt_ponte_preta = Rav
        Validacao_Elo = ' Rtv :' + str(Rtv) + ' G: ' + str(G) + ' Wv: ' + str(Wv) + ' Wpv: ' + str(Wpv)+ ' Dif gols: ' +str(difGols)
    if (clube1 == 'portuguesa'):
        Rt_portuguesa = Ram
        Validacao_Elo = ' Rtm :' + str(Rtm) + ' G: ' + str(G) + ' Wm: ' + str(Wm) + ' Wpm: ' + str(Wpm) + ' Dif gols: ' +str(difGols)
    if (clube2 == 'portuguesa'):
        Rt_portuguesa = Rav
        Validacao_Elo = ' Rtv :' + str(Rtv) + ' G: ' + str(G) + ' Wv: ' + str(Wv) + ' Wpv: ' + str(Wpv)+ ' Dif gols: ' +str(difGols)
    if (clube1 == 'santa cruz'):
        Rt_santacruz = Ram
        Validacao_Elo = ' Rtm :' + str(Rtm) + ' G: ' + str(G) + ' Wm: ' + str(Wm) + ' Wpm: ' + str(Wpm) + ' Dif gols: ' +str(difGols)
    if (clube2 == 'santa cruz'):
        Rt_santacruz = Rav
        Validacao_Elo = ' Rtv :' + str(Rtv) + ' G: ' + str(G) + ' Wv: ' + str(Wv) + ' Wpv: ' + str(Wpv)+ ' Dif gols: ' +str(difGols)
    if (clube1 == 'santo andré'):
        Rt_santoandre = Ram
        Validacao_Elo = ' Rtm :' + str(Rtm) + ' G: ' + str(G) + ' Wm: ' + str(Wm) + ' Wpm: ' + str(Wpm) + ' Dif gols: ' +str(difGols)
    if (clube2 == 'santo andré'):
        Rt_santoandre = Rav
        Validacao_Elo = ' Rtv :' + str(Rtv) + ' G: ' + str(G) + ' Wv: ' + str(Wv) + ' Wpv: ' + str(Wpv)+ ' Dif gols: ' +str(difGols)
    if (clube1 == 'santos'):
        Rt_santos = Ram
        Validacao_Elo = ' Rtm :' + str(Rtm) + ' G: ' + str(G) + ' Wm: ' + str(Wm) + ' Wpm: ' + str(Wpm) + ' Dif gols: ' +str(difGols)
    if (clube2 == 'santos'):
        Rt_santos = Rav
        Validacao_Elo = ' Rtv :' + str(Rtv) + ' G: ' + str(G) + ' Wv: ' + str(Wv) + ' Wpv: ' + str(Wpv)+ ' Dif gols: ' +str(difGols)
    if (clube1 == 'são paulo'):
        Rt_saopaulo = Ram
        Validacao_Elo = ' Rtm :' + str(Rtm) + ' G: ' + str(G) + ' Wm: ' + str(Wm) + ' Wpm: ' + str(Wpm) + ' Dif gols: ' +str(difGols)
    if (clube2 == 'são paulo'):
        Rt_saopaulo = Rav
        Validacao_Elo = ' Rtv :' + str(Rtv) + ' G: ' + str(G) + ' Wv: ' + str(Wv) + ' Wpv: ' + str(Wpv)+ ' Dif gols: ' +str(difGols)
    if (clube1 == 'sport'):
        Rt_sporte = Ram
        Validacao_Elo = ' Rtm :' + str(Rtm) + ' G: ' + str(G) + ' Wm: ' + str(Wm) + ' Wpm: ' + str(Wpm) + ' Dif gols: ' +str(difGols)
    if (clube2 == 'sport'):
        Rt_sporte = Rav
        Validacao_Elo = ' Rtv :' + str(Rtv) + ' G: ' + str(G) + ' Wv: ' + str(Wv) + ' Wpv: ' + str(Wpv)+ ' Dif gols: ' +str(difGols)
    if (clube1 == 'vasco'):
        Rt_vasco = Ram
        Validacao_Elo = ' Rtm :' + str(Rtm) + ' G: ' + str(G) + ' Wm: ' + str(Wm) + ' Wpm: ' + str(Wpm) + ' Dif gols: ' +str(difGols)
    if (clube2 == 'vasco'):
        Rt_vasco = Rav
        Validacao_Elo = ' Rtv :' + str(Rtv) + ' G: ' + str(G) + ' Wv: ' + str(Wv) + ' Wpv: ' + str(Wpv)+ ' Dif gols: ' +str(difGols)
    if (clube1 == 'vitória'):
        Rt_vitoria = Ram
        Validacao_Elo = ' Rtm :' + str(Rtm) + ' G: ' + str(G) + ' Wm: ' + str(Wm) + ' Wpm: ' + str(Wpm) + ' Dif gols: ' +str(difGols)
    if (clube2 == 'vitória'):
        Rt_vitoria   = Rav
        Validacao_Elo = ' Rtv :' + str(Rtv) + ' G: ' + str(G) + ' Wv: ' + str(Wv) + ' Wpv: ' + str(Wpv)+ ' Dif gols: ' +str(difGols)

##########################################################################    
    df_final.at[index,'Data_Confronto'] = datajogo
    df_final.at[index,'ID'] = indice
    df_final.at[index,'Time_Casa'] = clube1
    df_final.at[index,'Time_Visitante'] = clube2
    df_final.at[index, 'Gol_1'] = gol1 
    df_final.at[index, 'Gol_2'] = gol2
   
    df_final.at[index,'Tipo_Vencedor'] = Tipo_Vencedor
    df_final.at[index,'Elo_Mandante'] = Ram
    df_final.at[index,'Elo_Visitante'] = Rav
    df_final.at[index,'Validacao_Elo'] = Validacao_Elo
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
        cont_santa_cruz = cont_santa_cruz + 1
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

df_final.to_csv('ELO_2012.csv', index = False, sep = ';')

