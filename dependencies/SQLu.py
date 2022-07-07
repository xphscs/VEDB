import sqlite3 as sql

# ------------------------------------------------------------- #
# - # SCRIPT EN DONDE SE ALMACENAN LAS INSTRUCCIONES DE SQL # - #
# ------------------------------------------------------------- #

def CreateCursor(path):

    connector = sql.connect(path)
    cursor = connector.cursor()

    return cursor

