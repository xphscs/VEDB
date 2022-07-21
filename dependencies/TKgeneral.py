import __main__ as main

def SaveDB():
    """
    Función que guarda la base de datos modificada.
    """

    print("SAVING DATA...")
    main.DATA.to_csv("VEDB.csv", index = False)
    print("SAVED DATA!")


# función para crear el manú de la ventana principal
def create_main_menu(window):
    """
    Función que crea el menú (barra menú) de la ventana principal.
    """

    MMenu = window.CreateMenu()

    SMitems = ["archivo", "pichingo"]

    archivo_items = ["guardar cambios"]
    archivo_commands = [SaveDB]
    archivo_sub = window.CreateSubmenu(MMenu, archivo_items, archivo_commands)

    pichingo_items = ["pichingo 1", "pichingo 2", "pichingo 3"]
    pichingo_commands = [window.FuncionPrueba,window.FuncionPrueba, window.FuncionPrueba]
    pichingo_sub = window.CreateSubmenu(MMenu, pichingo_items, pichingo_commands)


    window.MenuIntegrator(MMenu, SMitems, [archivo_sub, pichingo_sub])


