# --------------------------------------- #
# - # SCRIPT CON FUNCIONES DE LA GUI  # - #
# --------------------------------------- #

from cgitb import text
from tkinter import *
from tkinter.ttk import Treeview, Combobox
from turtle import width

from numpy import var

import dependencies.TKgeneral as TKg

GBD = 2

class TKList:

    # Función de inicialiación
    def __init_(self, root):
        return

class Window:

    # función de inicialización
    def __init__(self, title, p_width, p_height, bgc):

        self.ww = Tk()
        self.frame = Frame(self.ww)

        # self.ww.resizable(False, False)

        self.ww.title(title)
        self.ww.configure(width = p_width, height = p_height, bg = bgc)

    # función de reiniciar WW
    def MainLoop(self):

        self.ww.mainloop()

    def CreateFrame(self, relx, rely, relwidth, relheight):

        frame = Frame(self.ww)
        frame.place(relx = relx, rely = rely, relwidth = relwidth, relheight = relheight)

        return frame

    # función para crear un botón
    def CreateButton(self, WWdim, relx, rely, text, command, bgc = "lightgray", frame = None):

        if frame == None:

            Wframe = self.frame
        else:
            Wframe = frame

        # se crea una instancia del objeto button
        TB = Button(
            Wframe, text = text, command = command, bg = bgc, bd = GBD
        )

        # se pocisiona el objeto
        TB.place(relx = relx, rely = rely)    

    # función para crear una lista de datos
    def CreateList(self, WWdim, relx, rely, rwidth, rheight, columns, data, frame = None):

        if frame ==None:
            Wframe = self.frame
        else:
            Wframe = frame

        TVFrame = Frame(self.ww)
        TVFrame.place(relwidth = rwidth, relheight = rheight, relx = relx, rely = rely)

        TV = Treeview(TVFrame, columns = [f"#{i}" for i in range(columns.size)], show = "headings")

        # TV.heading("#1", text = columns[0])
        for (i, item) in enumerate([columns[0]] + columns.tolist()):

            TV.heading(f"#{i}", text = item)
            TV.column(f"#{i}", anchor = CENTER, stretch = NO)
        

        # se inserta la data que se tiene
        for item in data:

            item = item.tolist()
            
            TV.insert(
                "",
                END,
                iid = None,
                text = item[0],
                values = item[1::],
            )
        
        # TV.column("#0", stretch = NO, anchor = CENTER)

        SBy = Scrollbar(TVFrame, orient = "vertical", command = TV.yview)
        SBx = Scrollbar(TVFrame, orient = "horizontal")
        SBx.configure(command = TV.xview)

        TV.configure(yscroll = SBy.set)
        TV.configure(xscrollcommand = SBx.set)

        SBy.pack(side = RIGHT, fill = BOTH)
        SBx.pack(side = BOTTOM, fill = BOTH)

        TV.pack(side = LEFT, fill = BOTH)

        return TV
    
    # función para display de mensajes en la ventana
    def CreateLabel(self, WWdim, relx, rely, text, frame = None):

        if frame == None:

            Wframe = self.frame
        else:
            Wframe = frame

        LB = Label(Wframe, text = text, bd = GBD)

        LB.place(relx = relx, rely = rely)

    # función para crear espacios de texto
    def CreateEntry(self, WWdim, relx, rely, width, height, frame = None):

        if frame == None:

            Wframe = self.frame
        else:
            Wframe = frame

        ET = Entry(Wframe)
        ET.config(width = width, height = height)

        ET.place(relx = relx, rely = rely)

        return ET

    # función que crea check buttons
    def CreateCheckbutton(self, WWdim, relx, rely, variable, text,frame = None):

        if frame == None:
            Wframe = self.frame
        else:
            Wframe = frame

        CB = Checkbutton(Wframe, variable = variable, text = text)

        CB.place(relx = relx, rely = rely)

        return CB
    
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
    def CreateCombobox(self, WWdim, relx, rely, values, frame = None):

        if frame == None:

            Wframe = self.frame
        else:
            Wframe = frame

        CB = Combobox(self.ww, state = "readonly", values = values)

        CB.place(relx = relx, rely = rely)

        return CB

    def exit(self):
        self.ww.destroy()

    def FuncionPrueba(args):

        print("ACCIONADO")

        return





