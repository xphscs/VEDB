# -------------------------------- #
# - # IMPORTACIÓN DE LIBRERÍAS # - #
# -------------------------------- # 

import dependencies.SQLu as DBu
import dependencies.TKu as TKu
import dependencies.TKgeneral as TKg

# -------------------------------#
# -     DEFINICIÓN DE LA DB    - # 
# -------------------------------#

DB_PATH = "VEDB.csv"     # path del archivo de la base de datos
DATA = DBu.CreateData(DB_PATH)
DATA_TEMP = DATA.copy()


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

    # Creación de la ventana raíz
    MainWW = TKu.Window(GUI_TITLE, WIDTH, HEIGHT, GUI_BK)

    TKu.TKg.create_main_menu(MainWW)

    # Creación principal de lista

    columns, items = DBu.df_to_data(DATA)
    MainWW.CreateList(WW_DIM, 0, 0.5, 0.75, 0.5, columns, items)


    # -- # MENÜ PRINCIPAL DE LA LISTA # -- #


    ListMenuFrame = MainWW.CreateFrame(0.75, 0.5, 0.25, 0.5)     # frame del espacio a trabajar

    # Creación del menú de mostrado de columnas

    MainWW.CreateLabel(WW_DIM, 0.35, 0.0, "Mostrar columnas", frame = ListMenuFrame)
    
    ShowVector = list()

    for colum in columns:
        ShowVector.append(True)
    
    for i, colum in enumerate(columns):

        MainWW.CreateCheckbutton(WW_DIM, (0.33 * ( i % 3 ) ), (0.1 * (i // 3)) + 0.2, ShowVector[1], colum, frame = ListMenuFrame)


    # Menu de filtrado de lista principal



    MainWW.MainLoop()


main()




