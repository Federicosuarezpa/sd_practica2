import lithops
import pandas as panda
from io import StringIO

import pandas as pd
from lithops import Storage
from lithops import FunctionExecutor
import os
from dotenv import load_dotenv

################################################################
#   Estudiante: Federico Suárez Palavecino                     #
#   Correo: federicohernan.suarez@estudiants.urv.cat           #
################################################################

#################   Variables con los nombres de los ficheros del IBM Cloud    #################

load_dotenv()
csv_file1 = os.getenv('CSV_FILE1')
csv_file2 = os.getenv('CSV_FILE2')
csv_file3 = os.getenv('CSV_FILE3')
obj_storage = os.getenv('OBJ_STORAGE')


def processCsv(null):
    storage = Storage()
    data = storage.get_object(obj_storage, csv_file2)
    data_format = str(data[0:-1], 'utf-8')
    database = pd.read_csv(StringIO(data_format))
    first_database = database[
        ['TipusCasData', 'ComarcaDescripcio', 'MunicipiCodi', 'MunicipiDescripcio', 'NumCasos']].copy()

    data = storage.get_object(obj_storage, csv_file1)
    data_format = str(data[0:-1], 'utf-8')
    database = pd.read_csv(StringIO(data_format))
    second_database = database[
        ['Data', 'Defuncions diàries', 'Altes diàries', 'Total de defuncions', 'Total d\'altes', ]].copy()
    second_database.rename(
        columns={'Data': 'TipusCasData', 'Defuncions diàries': 'DefuncionsDiaries', 'Altes diàries': 'AltesDiaries',
                 'Total de defuncions': 'TotalDefuncions',
                 'Total d\'altes': 'TotalAltes'}, inplace=True)

    database_result = pd.merge(left=first_database, right=second_database, how='left', left_on='TipusCasData',
                               right_on='TipusCasData')

    database_result.to_csv('database.csv', index=False)
    database = open('database.csv', 'r')
    storage.put_object(obj_storage, 'database.csv', database.read())
    database.close()


if __name__ == '__main__':
    fexec = lithops.FunctionExecutor(runtime_memory=2048)
    fexec.call_async(processCsv, "None")
    fexec.wait()
