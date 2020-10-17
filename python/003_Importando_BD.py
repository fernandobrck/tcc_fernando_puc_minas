import csv
import psycopg2 
import re
from unicodedata import normalize
from datetime import datetime
import os
import pandas as pd

lvBarra = '\\'

#lvDirArquivo = r'D:\DATASETS\IndicadoresCompletos'
lvDirArquivo = r'D:\DATASETS\IndicadoresCompletosPorJogo'

#lvTable = '"imp_indicadores_individuais"'
lvTable = 'imp_indicadores'

############################################################################################################################
def ProcessaRegistros(pArquivo,pTabela):
    try:
        connection = psycopg2.connect("host=localhost port='5434' dbname=tcc_fernando user=fernando password=123456")
        cursor = connection.cursor()   
        csvfile = open(pArquivo,encoding='utf-8') 
        next(csvfile) 
        cursor.copy_from(csvfile, pTabela, sep=';')      
       
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
def MontarArquivos(pCaminhoArquivo,pTabela): 
    list_files = os.listdir(pCaminhoArquivo)

    for arquivo in list_files:
        lvIniTime = str(datetime.now())
        lvArquivo = pCaminhoArquivo  +lvBarra+  arquivo;
        print('Lendo arquivo ['+lvIniTime+'] ' + lvArquivo)
        
        ProcessaRegistros(lvArquivo,pTabela)
        

        lvFimTime = lvIniTime = str(datetime.now())
        print('Fim arquivo ['+lvFimTime+'] ' + lvArquivo)
        print('***********************************************************************************************************')

MontarArquivos(lvDirArquivo,lvTable);

