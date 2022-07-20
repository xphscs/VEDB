import pandas as pd
import random

columnas = ["etiqueta", "tipo", "nombre", "índice", "material", "piedra prin", 
            "piedra sec", "kilates P1", "kilates P2", "costo", "precio", 
            "estado", "vendido a", "vendido por", "vendido el",  "ganancia"]

data = pd.DataFrame(columns = columnas)



AN_counter = 1
PUL_counter = 1
AR_counter = 1
DIJ_counter = 1

tipos = ["ANILLO", "PULSERA", "ARETES", "DIJE"]
materiales = ["ORO AMARILLO", "ORO BLANCO", "PLATA", "PLATINO"]
nombres = ["pichingo", "solitario", "carre", "crusster"]
piedras = ["ESMERALDA", "DIAMANTES", "ZIRCON"]
estados = ["VENDIDO", "EN INVENTARIO"]
vendedores = ["GABRIELA", "LUISA", "SANTIAGO"]

data.columns = columnas

for i in range(150):

    tipo = random.choice(tipos)
    material = random.choice(materiales)

    nombre = f"{tipo} {random.choice(nombres)}"

    piedra_prin = random.choice(piedras)
    kilate_prin = random.randint(0, 10)

    piedra_sec = random.choice(piedras) if bool(random.getrandbits(1)) else "NA"
    kilate_sec = random.randint(0, 10) if piedra_sec != "NA" else "NA"

    costo = random.randint(100, 500)
    precio = random.randint(costo + int(costo / 3), costo * 3)

    estado = random.choice(estados)

    v_precio = "NA"
    v_vendedor = "NA"
    v_fecha = "NA"
    ganancia = "NA"

    if estado == "VENDIDO":

        v_precio = random.randint(costo + int(costo / 3), precio)
        v_vendedor = random.choice(vendedores)
        v_fecha = f"{random.randint(1, 31)}/{random.randint(1, 12)}/{random.randint(19, 22)}"
        ganancia = v_precio - costo
    
    etiqueta = None
    indice = None

    if tipo == "ANILLO":

        etiqueta = f"AN-{AN_counter}"
        indice = AN_counter 

        AN_counter += 1

    elif tipo == "PULSERA":

        etiqueta = f"PUL-{PUL_counter}"
        indice = PUL_counter

        PUL_counter += 1

    elif tipo == "ARETES":

        etiqueta = f"AR-{AR_counter}"
        indice = AR_counter

        AR_counter += 1
    
    else:

        etiqueta = f"DIJ-{DIJ_counter}"
        indice = DIJ_counter

        DIJ_counter += 1

    
    data_dic = {"etiqueta": etiqueta, "tipo": tipo, "nombre": nombre, "índice": indice, "material": material,
            "piedra prin": piedra_prin, "piedra sec": piedra_sec, "kilates P1": kilate_prin,
            "kilates P2": kilate_sec, "costo": costo, "precio": precio, "estado": estado, "vendido a": v_precio, 
            "vendido por": v_vendedor, "vendido el": v_fecha,  "ganancia": ganancia}

    data = data.append(data_dic, ignore_index = True)


data.to_csv("VEDB.csv", index = False )
    







