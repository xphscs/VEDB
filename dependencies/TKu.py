# --------------------------------------- #
# - # SCRIPT CON FUNCIONES DE LA GUI  # - #
# --------------------------------------- #

from cgitb import text
from tkinter import *
from tkinter.ttk import Treeview, Combobox

from numpy import var

import dependencies.TKgeneral as TKg
import dependencies.SQLu as DBu

GBD = 2

class TKList:
    """
    Clase cuyo atributo principal es un objeto TreeView de TKinter, 
    con funciones adicionales para que esta instancia "self.wwlist" 
    se comporte como lo esperado en la aplicación
    """

    # Función de inicialiación, sólo crea las variables locales, no renderiza la lista
    def __init__(self, root, data, posargs, dimargs):
        """
        Función que inicializa la clase. Esta función SÓLO GUARDA LOS DATOS DE LA LISTA
        Y VARIABES NECESARIAS PARA SU CORRECTO FUNCIONAMIENTO. Finalmente llama al método
        CreateList, que se encarga de crear la lista en base a los atributos.
        """
        
        self.data_backup = data     # backup de la data en caso que no se quieran guardar cambios
        self.data = data.copy()     # data a utilizat y modificar

        self.root = root    # Objeto Tk padre del frame 
        self.frame = Frame(self.root)   # Frame en donde se renderiza la lista
        self.frame.place(relwidth = dimargs[0], relheight = dimargs[1], relx = posargs[0], rely = posargs[1])

        # Vector que guarda valores booleanos acerca de las columnas que tienen que ser mostradas
        self.columnvector = [BooleanVar(value = True) for x in data.columns]

        # Ya al haber amacenado toda la información necesario de la lista, se llama a la función
        # CreateList para que esta cree la lista en la ventana padre
        self.wwlist = self.CreateList()


    def CreateList(self):
        """
        Función que crea la lista en la ventana padre. La lista como tal es un objeto
        tk.Treeview el cual es modificado para parecer una lista tabular. 
        """

        columns, items = DBu.df_to_data(self.data)  # Con la data guardada, se convierte ésta a tipos leíbles por tk.Treeview
                                                    # para luego ser utilizados

        # Se crea el objeto Treeview
        TV = Treeview(self.frame, columns = [f"#{i}" for i in range(columns.size)], show = "headings")

        # Se añaden las columnas con su respectivo nombre
        for (i, item) in enumerate([columns[0]] + columns.tolist()):
            
            TV.heading(f"#{i}", text = item)
            TV.column(f"#{i}", anchor = CENTER, stretch = NO, width = 150)
        

        # se inserta la data que se tiene
        for item in items:

            item = item.tolist()
            
            TV.insert(
                "",
                END,
                iid = None,
                values = item,
            )
        
        # Se agregan las dos scrollbars, tanto vertical como horizontal
        SBy = Scrollbar(self.frame, orient = "vertical", command = TV.yview)
        SBx = Scrollbar(self.frame, orient = "horizontal")
        SBx.configure(command = TV.xview)

        TV.configure(yscroll = SBy.set)
        TV.configure(xscrollcommand = SBx.set)

        SBy.pack(side = RIGHT, fill = BOTH)
        SBx.pack(side = BOTTOM, fill = BOTH)

        TV.pack(side = LEFT, fill = BOTH)

        
        return TV   # Se retorna el objeto Treeview en caso que se necesite su instancia después


    def FilterColumns(self):
        """
        Función que filtra las columnas a mostrar en la lista de acuerdo al columvector de la lista.
        Lo único que hace es cambiar el ancho de cada columna inactiva
        """

        for i, val in enumerate(self.columnvector):

            if not val.get():
                self.wwlist.column(f"#{i + 1}", width = 0)
            else:
                self.wwlist.column(f"#{i + 1}", width = 150)


    def ColVecEdit(self, option):
        """
        Función llamada por los botones de menú "MOSTRAR COLUMNAS". Esta función selecciona o deselecciona
        todos los elementos del columvector.
        """

        if option == "all":

            for val in self.columnvector:

                val.set(True)
        
        elif option == "none":

            for val in self.columnvector:

                val.set(False)


class Window:
    """
    Clase de ventana. En esta se encuentran los atributos básicos de la ventana Tkinter
    pero se le añaden métodos para facilitar la creación de widgets necesarios en la
    para la ventana. 
    """

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
    def CreateButton(self, WWdim, relx, rely, text, command, bgc = "lightgray", frame = None, width = 0.2, height = 0.08):

        if frame == None:

            Wframe = self.frame
        else:
            Wframe = frame

        # se crea una instancia del objeto button
        TB = Button(
            Wframe, text = text, command = command, bg = bgc, bd = GBD
        )

        # se pocisiona el objeto
        TB.place(relx = relx, rely = rely, relwidth = width, relheight = height)

    

    def CreateList(self, data, relx, rely, relwidth, relheight):

        TVlist = TKList(self.ww, data, (relx, rely), (relwidth, relheight))

        return TVlist
    
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




"""
FUNCIONES QUE FUNCIONABAN PERO QUE MODIFIQUÉ POR ESTÉTICA

# función para crear una lista de datos
    def CreateList1(self, WWdim, relx, rely, rwidth, rheight, columns, data, frame = None):

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
        
"""
