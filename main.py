# -------------------------------- #
# - # IMPORTACIÓN DE LIBRERÍAS # - #
# -------------------------------- # 

import dependencies.SQLu as SQLu
import dependencies.TKu as TKu

# -------------------------------#
# -     DEFINICIÓN DE LA DB    - # 
# -------------------------------#

DB_PATH = "VEDB.sqlite"     # path del archivo de la base de datos

DBc = SQLu.CreateCursor(DB_PATH)    # creo el cursor de la base de datos

# --------------------------------#
# -     DEFINICIÓN DE LA GUI    - # 
# --------------------------------#

GUI_TITLE = "VE DataBase"   # título de la inferfaz

WIDTH = 1280    # propiedades de pantalla
HEIGHT = 720
WW_DIM = (WIDTH, HEIGHT)

GUI_BK = "lightgray"

# ------------------------------- #
# - # FUNCIÓN MAIN DEL CÓDIGO # - #
# ------------------------------- #

def main():

    # creo la ventana raíz
    MainWW = TKu.Window(GUI_TITLE, WIDTH, HEIGHT, GUI_BK)

    MainWW.CreateList(WW_DIM, 0.25, 0.25, ["x", "y", "z"], [[1, 2, 3], [4, 5, 6]])

    MainWW.MainLoop()

main()




