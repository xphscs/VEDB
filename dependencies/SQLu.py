import numpy as np
import pandas as pd


# ------------------------------------------------------------- #
# - # SCRIPT EN DONDE SE ALMACENAN LAS INSTRUCCIONES DE SQL # - #
# ------------------------------------------------------------- #

# función que crea un objeto DataFrame con la base de datos del .CVS
def CreateData(path):

    return pd.read_csv(path)


# función que convierte un DataFrame a un objeto numpy para poder manejarlo como listas
def df_to_data(data):

    columns = data.columns.to_numpy()[::]
    values = data.to_numpy()[::][::]

    return columns, values



