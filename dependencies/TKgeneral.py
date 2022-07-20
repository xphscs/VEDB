import __main__ as main

from main import DATA_SHOW, ShowVector

def SaveDB():

    print("SAVING DATA...")
    main.DATA.to_csv("VEDB.csv", index = False)
    print("SAVED DATA!")


# función para crear el manú de la ventana principal
def create_main_menu(window):

    MMenu = window.CreateMenu()

    SMitems = ["archivo", "pichingo"]

    archivo_items = ["guardar cambios"]
    archivo_commands = [SaveDB]
    archivo_sub = window.CreateSubmenu(MMenu, archivo_items, archivo_commands)

    pichingo_items = ["pichingo 1", "pichingo 2", "pichingo 3"]
    pichingo_commands = [window.FuncionPrueba,window.FuncionPrueba, window.FuncionPrueba]
    pichingo_sub = window.CreateSubmenu(MMenu, pichingo_items, pichingo_commands)


    window.MenuIntegrator(MMenu, SMitems, [archivo_sub, pichingo_sub])


Q# Función para re-renderizar 

# Función que filtra por columnas la lista
def ShowColumns(DATA, DATASHOW, SHOWVECTOR):

    DATASHOW = DATA.copy()

    for i, value in enumerate(SHOWVECTOR):

        if value:
            DATASHOW.drop(DATASHOW.columns[[i]], axis = "columns")