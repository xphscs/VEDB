import numpy as np
import pandas as pd

from tkinter import BooleanVar


# ------------------------------------------------------------- #
# - # SCRIPT EN DONDE SE ALMACENAN LAS INSTRUCCIONES DE SQL # - #
# ------------------------------------------------------------- #

# función que crea un objeto DataFrame con la base de datos del .CVS
def CreateData(path):
    """
    Función que lee un archivo .csv y devuelve un objeto pandas.DataFrame con
    su información
    """
    return pd.read_csv(path)


# función que convierte un DataFrame a un objeto numpy para poder manejarlo como listas
def df_to_data(data):
    """
    Función que convierte los datos de un pandas.DataFrame a dos np.arrays, el 
    primero con las columnas y el segundo con arrays de los datos de las diferentes
    columnas por cada entrada del DataFrame
    """

    columns = data.columns.to_numpy()[::]
    values = data.to_numpy()[::][::]

    return columns, values

def GetColumnValues(data, column):
    """
    Función que devuelve todos los posibles valores de la columna 
    pasada como argumento
    """

    CValues = set()

    for i in data.index:
        CValues.add(data[column][i])

    return CValues


def CreateFilterDic(data):
    """
    Función que crea e diccionario de filtro, cuyas keys son los nombres de cada columna
    """
    FilterDic = dict()

    for column in data.columns:

        values = GetColumnValues(data, column):




