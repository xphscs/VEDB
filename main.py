# -------------------------------- #
# - # IMPORTACIÓN DE LIBRERÍAS # - #
# -------------------------------- # 

import dependencies.SQLu as DBu
import dependencies.TKu as TKu

# -------------------------------#
# -     DEFINICIÓN DE LA DB    - # 
# -------------------------------#

DB_PATH = "VEDB.csv"     # path del archivo de la base de datos

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

    TKu.create_main_menu(MainWW)

    columns = list(range(30))
    items = [ list(range(i, i + 30)) for i in range(50)]

    MainWW.CreateList(WW_DIM, 0, 0.5, 0.75, 0.5, columns, items)

    MainWW.MainLoop()


main()




