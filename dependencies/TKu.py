# --------------------------------------- #
# - # SCRIPT CON FUNCIONES DE LA GUI  # - #
# --------------------------------------- #

from tkinter import *
from tkinter.ttk import Treeview, Combobox
from turtle import width

from numpy import var

GBD = 2

class Window:

    # función de inicialización
    def __init__(self, title, p_width, p_height, bgc):

        self.ww = Tk()
        self.frame = Frame(self.ww)

        self.ww.title(title)
        self.ww.configure(width = p_width, height = p_height, bg = bgc)

    # función de reiniciar WW
    def MainLoop(self):

        self.ww.mainloop()

    # función para crear un botón
    def CreateButton(self, WWdim, relx, rely, text, command, bgc = "lightgray"):

        # se crea una instancia del objeto button
        TB = Button(
            self.ww, text = text, command = command, bg = bgc, bd = GBD
        )

        # se pocisiona el objeto
        TB.place(x = int(WWdim[0] * relx), y = int(WWdim[1] * rely))    

    # función para crear una lista de datos
    def CreateList(self, WWdim, relx, rely, rwidth, rheight, columns, data):

        TV = Treeview(self.ww, columns = columns[1::])

        TV.heading("#0", text = columns[0])

        for (i, item) in enumerate(columns[1::]):

            TV.heading(item, text = item)
            TV.column(f"#{i + 1}", anchor = CENTER, stretch = NO)
        

        # se inserta la data que se tiene
        for item in data:
            
            TV.insert(
                "",
                END,
                text = item[0],
                values = item[1::]
            )
        
        TV.column("#0", stretch = NO, anchor = CENTER)

        SBy = Scrollbar(self.ww, orient = "vertical", command = TV.yview)
        SBx = Scrollbar(self.ww, orient = "horizontal")
        SBx.configure(command = TV.xview)

        TV.configure(yscroll = SBy.set)
        TV.configure(xscrollcommand = SBx.set)

        SBy.pack(side = RIGHT, fill = BOTH)
        SBx.pack(side = BOTTOM, fill = BOTH)

        TV.place(relx = relx, rely = rely)

        return TV
    
    # función para display de mensajes en la ventana
    def CreateLabel(self, WWdim, relx, rely, text):

        LB = Label(self.ww, text = text, bd = GBD)

        LB.place(x = int(WWdim[0] * relx), y = int(WWdim[1] * rely))

    # función para crear espacios de texto
    def CreateEntry(self, WWdim, relx, rely, width, height):

        ET = Entry(self.ww)
        ET.config(width = width, height = height)

        ET.place(x = int(WWdim[0] * relx), y = int(WWdim[1] * rely))

        return ET

    # función que crea check buttons
    def CreateCheckbutton(self, WWdim, relx, rely, variable):

        CB = Checkbutton(self.ww, variable = variable)

        CB.place(x = int(WWdim[0] * relx), y = int(WWdim[1] * rely))
    
    # función que crea menús en la barra superior de la ventana
    def CreateMenu(self):

        MN = Menu(self.ww, bd = GBD)

        self.ww.config(menu = MN)

        return MN 
    
    # función para crear las cascadas de los menús
    def CreateSubmenu(self, Mmenu, items, commands):

        SBM = Menu(Mmenu, tearoff = 0)

        for (item, command) in zip(items, commands):

            SBM.add_command(label = item, command = command)
        
        return SBM
    
    # función para integrar cascadas en el menú
    def MenuIntegrator(self, menu, items, submenus):

        for (item, submenu) in zip(items, submenus):

            menu.add_cascade(label = item, menu = submenu)


    # función para crear una lista desplegable
    def CreateCombobox(self, WWdim, relx, rely, values):

        CB = Combobox(self.ww, state = "readonly", values = values)

        CB.place(x = int(WWdim[0] * relx), y = int(WWdim[1] * rely))

        return CB

    def exit(self):
        self.ww.destroy()

    def FuncionPrueba(args):

        print("ACCIONADO")

        return



