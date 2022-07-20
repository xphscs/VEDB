# -------------------------------- #
# - # IMPORTACIÓN DE LIBRERÍAS # - #
# -------------------------------- # 

from pickle import FALSE
import dependencies.SQLu as DBu
import dependencies.TKu as TKu
import dependencies.TKgeneral as TKg


# --------------------------------#
# -     DEFINICIÓN DE LA GUI    - # 
# --------------------------------#

GUI_TITLE = "VE DataBase"   # título de la inferfaz

WIDTH = 1280    # propiedades de pantalla
HEIGHT = 720
WW_DIM = (WIDTH, HEIGHT)

GUI_BK = "lightgray"


# -------------------------------#
# -     DEFINICIÓN DE LA DB    - # 
# -------------------------------#

DB_PATH = "VEDB.csv"     # path del archivo de la base de datos

DATA = DBu.CreateData(DB_PATH)  # DB con la que se ejecutarán los cambios
DATA_BACKUP = DATA.copy()   # BackUp de la DB en caso que no se quieran guardar cambios algunos
DATA_SHOW = DATA.copy()     # DB que se mostrará en la lista principal


# ------------------------------- #
# - # FUNCIÓN MAIN DEL CÓDIGO # - #
# ------------------------------- #

def main():

    # Creación de la ventana raíz
    MainWW = TKu.Window(GUI_TITLE, WIDTH, HEIGHT, GUI_BK)

    # Crear el menú de la ventana principal
    TKg.create_main_menu(MainWW)

    columns, items = DBu.df_to_data(DATA)

    # -- # MENÜ PRINCIPAL DE LA LISTA # -- #

    # Creación principal de lista
    MainList = MainWW.CreateList(DATA, 0.0, 0.5, 0.75, 0.5)

    ListMenuFrame = MainWW.CreateFrame(0.75, 0.5, 0.25, 0.5)     # frame del espacio a trabajar

    # Creación del menú de mostrado de columnas

    MainWW.CreateLabel(WW_DIM, 0.25, 0.05, "MOSTRAR COLUMNAS", frame = ListMenuFrame)
    
    for i, colum in enumerate(columns):
        MainWW.CreateCheckbutton(WW_DIM, (0.33  * ( i % 3 ) ), (0.08 * (i // 3)) + 0.2, MainList.columnvector[i], colum, frame = ListMenuFrame)
    

    MainWW.CreateButton(WW_DIM, 0.4, 0.75, "Actualizar", command = lambda: MainList.FilterColumns(), frame = ListMenuFrame, width = 0.4, height = 0.16)
    MainWW.CreateButton(WW_DIM, 0.2, 0.75, "Sel. todos", command = lambda: MainList.ColVecEdit("all"), frame = ListMenuFrame)
    MainWW.CreateButton(WW_DIM, 0.2, 0.83, "del. todos", command = lambda: MainList.ColVecEdit("none"), frame = ListMenuFrame)


    # Menu de filtrado de lista principal



    MainWW.MainLoop()


main()




