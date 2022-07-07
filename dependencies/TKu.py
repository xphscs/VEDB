# --------------------------------------- #
# - # SCRIPT CON FUNCIONES DE LA GUI  # - #
# --------------------------------------- #

from tkinter import *
from tkinter.ttk import Treeview

class Window:

    # función de inicialización
    def __init__(self, title, p_width, p_height, bgc):

        self.ww = Tk()

        self.ww.title(title)
        self.ww.configure(width = p_width, height = p_height, bg = bgc)

    # función de reiniciar WW
    def MainLoop(self):

        self.ww.mainloop()

    # función para crear un botón
    def CreateButton(self, WWdim, relx, rely, text, command, bgc = "lightgray"):

        # se crea una instancia del objeto button
        TB = Button(
            self.ww, text = text, command = command, bg = bgc, bd = 2
        )

        # se pocisiona el objeto
        TB.place(x = int(WWdim[0] * relx), y = int(WWdim[1] * rely))    

    # función para crear una lista de datos
    def CreateList(self, WWdim, relx, rely, columns, data):

        # se crea la instancia del objeto de lista
        TV = Treeview(columns = columns[1::])

        # se crean las columnas de los elementos
        TV.heading("#0", text = columns[0])

        for item in columns[1::]:

            TV.heading(item, text = item)

        # se inserta la data que se tiene
        for item in data:

            TV.insert(
                "",
                END,
                text = item[0],
                values = item[1::]
            )
        
        TV.place(x = int(WWdim[0] * relx), y = int(WWdim[1] * rely))
        

    def FuncionPrueba(args):

        return



