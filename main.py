# -------------------------------- #
# - # IMPORTACIÓN DE LIBRERÍAS # - #
# -------------------------------- # 

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


BasicFilterPreferences = ["tipo", "material", "vendido por"]    # Lista en donde se almacenan los nombres de las columnas que se muestran en el menú de 
                                                                # filtrado básico

# ------------------------------- #
# - # FUNCIÓN MAIN DEL CÓDIGO # - #
# ------------------------------- #

def main():

    # Creación de la ventana raíz
    MainWW = TKu.Window(GUI_TITLE, WIDTH, HEIGHT, GUI_BK)

    # Crear el menú de la ventana principal
    TKg.create_main_menu(MainWW)

    columns, items = DBu.df_to_data(DATA)

    # ------------------------------------ #
    # -- # MENÚ PRINCIPAL DE LA LISTA # -- #
    # ------------------------------------ #}

    # -  MENU DE COLUMNAS  - #

    # Creación principal de lista
    MainList = MainWW.CreateList(DATA, 0.0, 0.0, 0.75, 1)

    # Creación del menú de mostrado de columnas

    SCMenuFrame = MainWW.CreateFrame(0.75, 0.0, 0.25, 0.4)     # frame del espacio a trabajar

    # Creación del menú
    MainWW.CreateLabel(WW_DIM, 0.3, 0.05, "MOSTRAR COLUMNAS", frame = SCMenuFrame)
    
    # Creación de los checkbutton para mostrar columnas
    for i, colum in enumerate(columns):
        MainWW.CreateCheckbutton(WW_DIM, (0.33  * ( i % 3 ) ), (0.08 * (i // 3)) + 0.2, MainList.columnvector[i], colum, frame = SCMenuFrame)
    
    # Botones de acción del mostrado de columnas
    MainWW.CreateButton(WW_DIM, 0.4, 0.75, "Actualizar", command = lambda: MainList.FilterColumns(), frame = SCMenuFrame, width = 0.4, height = 0.16)
    MainWW.CreateButton(WW_DIM, 0.2, 0.75, "Sel. todos", command = lambda: MainList.ColVecEdit("all"), frame = SCMenuFrame)
    MainWW.CreateButton(WW_DIM, 0.2, 0.83, "del. todos", command = lambda: MainList.ColVecEdit("none"), frame = SCMenuFrame)


    # - MENU DE FILTRADO BÄSICO - #

    LFMenuFrame = MainWW.CreateFrame(0.75, 0.4, 0.25, 0.4)

    MainWW.CreateLabel(WW_DIM, 0.35, 0.0, "FILTRADO BÄSICO", LFMenuFrame)
    




    MainWW.MainLoop()


main()




