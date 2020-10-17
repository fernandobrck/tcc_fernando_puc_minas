import csv
import psycopg2 
import re
from unicodedata import normalize
from datetime import datetime
import os
import pandas as pd

lvBarra = '\\'

lvDirArquivo = r'D:\DATASETS\Cartola\agregados'

lvDirArquivoAux = r'D:\DATASETS\Cartola\agregados\auxiliar'

lvTable = '"imp_cartola"'

############################################################################################################################
def ProcessaRegistros(pArquivo,pTabela,pCaminhoAuxiliar):
    try:
        connection = psycopg2.connect("host=localhost port='5434' dbname=tcc_fernando user=fernando password=123456")
        cursor = connection.cursor()   
        csvfile = pd.read_csv(pArquivo ,sep=',',usecols = ['Apelido','AtletaID','ClubeID','Participou','Pontos','Preco','Rodada','ano','dia','mes'])
        #print(csvfile)
        csvfile.to_csv(pCaminhoAuxiliar +lvBarra + 'alterado.csv', index = False, sep = ',')
      
        csvImport = open(pCaminhoAuxiliar +lvBarra + 'alterado.csv',encoding='utf-8') 
        next(csvImport)    
        
        cursor.copy_from(csvImport, pTabela, sep=',', columns = ('Apelido','AtletaID','ClubeID','Participou','Pontos','Preco','Rodada','Ano','Dia','Mes'))
       
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
DROP TABLE IF EXISTS imp_cartola;
CREATE TABLE imp_cartola (
	Apelido varchar, 
	AtletaID bigint, 
	ClubeID varchar, 
	Participou boolean,
	Pontos numeric(17,2),
	Preco numeric(17,2),
	Rodada integer,
	Ano integer,
    Dia numeric,
    Mes numeric

);

'''        