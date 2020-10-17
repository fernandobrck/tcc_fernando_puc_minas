import csv
import psycopg2 
import re
from unicodedata import normalize
from datetime import datetime
import os
import pandas as pd

lvBarra = '\\'

lvDirArquivo = r'D:\DATASETS\Cartola\agregados2018'

lvDirArquivoAux = r'D:\DATASETS\Cartola\agregados2018\auxiliar'

lvTable = '"imp_cartola_2"'

############################################################################################################################
def ProcessaRegistros(pArquivo,pTabela,pCaminhoAuxiliar):
    try:
        connection = psycopg2.connect("host=localhost port='5434' dbname=tcc_fernando user=fernando password=123456")
        cursor = connection.cursor()   
        csvfile = pd.read_csv(pArquivo ,sep=',',usecols = ['atletas.apelido','atletas.rodada_id','atletas.pontos_num','atletas.preco_num','atletas.clube.id.full.name'])
        
        csvfile.to_csv(pCaminhoAuxiliar +lvBarra + 'alterado.csv', index = False, sep = ',')
      
        csvImport = open(pCaminhoAuxiliar +lvBarra + 'alterado.csv',encoding='utf-8') 
        next(csvImport)    
        
        cursor.copy_from(csvImport, pTabela, sep=',', columns = ('apelido','rodada','pontos','preco','clube'))
       
        connection.commit()              
    except (Exception, psycopg2.Error) as error :
        print ("Erro: ", error)
    finally:
        cursor.close()
        connection.close()
        print('Registros inseridos com sucesso '+str(datetime.now()))  
############################################################################################################################

############################################################################################################################
############################################################################################################################
def MontarArquivos(pCaminhoArquivo,pTabela,pCaminhoAuxiliar): 
    list_files = os.listdir(pCaminhoArquivo)

    for arquivo in list_files:
        lvIniTime = str(datetime.now())
        lvArquivo = pCaminhoArquivo  +lvBarra+  arquivo;
        print('Lendo arquivo ['+lvIniTime+'] ' + lvArquivo)
        
        ProcessaRegistros(lvArquivo,pTabela,pCaminhoAuxiliar)
        

        lvFimTime = lvIniTime = str(datetime.now())
        print('Fim arquivo ['+lvFimTime+'] ' + lvArquivo)
        print('***********************************************************************************************************')

MontarArquivos(lvDirArquivo,lvTable,lvDirArquivoAux);

'''
create table imp_cartola_2(
	apelido varchar,
	rodada integer,
	pontos numeric(17,2),
	preco numeric (17,2),
	clube varchar)
'''        