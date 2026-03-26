import pandas as pd

#obtiene un dataframe y en la columna precio hace la sumatoria
#luego obtiene el numero de filas y retorna la sumatoria / numero de filas

def promedio(archivo):
    
    acumulador = archivo["precio"].sum()
    cantidad = archivo.shape[0]

    #se redondea con 0 decimales
    return round(acumulador/cantidad,0)

"""
    obtiene una lista de productos (los productos que hay en el dataframe original)
    luego en una lista guarda los "coladores" que realmente son filtros que
    funcionan asi: archivo[el colador], obteniendo del archivo original solmente las filas
    que cumplan con el filtro. El filtro es una serie con true o false si cumple la 
    condicion, por eso al pasarlo asi: archivo[colador] el archivo nuevo con el colador
    es simplemente un nuevo archivo con filas en la que en la serie (el colador) en 
    esa fila tiene true
"""
def colador_productos(productos):
    coladores = []

    for i in productos:

        #filtro: si el producto es i y tanto la cantidad como precio NO son null, la fila es true
        colador = (archivo['producto'] == i) & ~(archivo['cantidad'].isnull()) & ~(archivo['precio'].isnull())
        coladores.append(colador)

    return coladores

"""
    obtiene los coladores o series y los usa como filtros en el archivo original
    para posteriormente guardarlo en una lista con los dataframes limpios.
    En este caso es cada producto con las filas precio y cantidad completos
"""

def productos_colados(coladores):
    dataFramesLimpios = []

    for i in coladores:
        dataFramesLimpios.append(archivo[i])

    return dataFramesLimpios

"""
    finalmente se logra hacer promedios teniendo la confianza de no tener ningun
    null en la columna precio y columna cantidad, siendo capaces de usar con
    confianza la funcion de promedio explicada arriba par asi establecer mapa con
    el promedio de precios de cada producto con el fin de poner precios en la columna
    precios donde el campo es null
"""

def establecer_mapa_promedios(dataFramesLimpios, productos):
    mapa = {producto: 0 for producto in productos}

    for i in range(len(dataFramesLimpios)):
        mapa[productos[i]] = promedio(dataFramesLimpios[i])

    return mapa

archivo = pd.read_csv('ventas.csv')

"""se obtiene un mapa del precio de los productos, haciendolo por medio de la obtencion del promedio 
del precio de cada producto (ya que el valor varia), por lo que se obtiene los datos en el que la cantidad
y el precio si estan y se hace una sumatoria del precio y se divide por la sumatoria de las filas
obteniendo los promedios del precio de cada producto individualmente"""

#array con cada producto que existe en el dataframe archivo
productos = archivo['producto'].unique()
coladores = colador_productos(productos)
dataFramesLimpios = productos_colados(coladores)
mapa = establecer_mapa_promedios(dataFramesLimpios, productos)

print(mapa)

"""
    cogemos columna por columna del dataframe original
    si precio y cantidad es null, se elimina esa fila
    si precio es null se pone el promedio del precio del producto
    si la cantidad es null se pone 1
    si nomnbre es null se pone un string que dice: indefinido
    si la ciudad es null tambien se pone: indefinido
    en fecha intercambiamos los / por -
    finalmente cambiamos el tipo de datos de float a int en la columna cantidad
"""

for i, filas in archivo.iterrows():
    for columna in archivo.columns:
        if filas[columna]