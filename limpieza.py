import pandas as pd

def promedio(archivo):
    
    acumulador = archivo["precio"].sum()
    cantidad = archivo.shape[0]

    return round(acumulador/cantidad,0)


def establecer_promedios(archivo, diccionario):

    productos = archivo['producto'].unique()
    mapa = {producto: 0 for producto in productos}

    for i in productos:
        mapa[i] = promedio

    return mapa


archivo = pd.read_csv('ventas.csv')

promedio_precios = {}


"""se obtiene un mapa del precio de los productos, haciendolo por medio de la obtencion del promedio 
del precio de cada producto (ya que el valor varia), por lo que se obtiene los datos en el que la cantidad
y el precio si estan y se hace una sumatoria del precio y se divide por la sumatoria de las cantidades
obteniendo los promedios del precio de cada producto individualmente"""

colador_celular = (archivo['producto'] == 'Celular') & ~(archivo['cantidad'].isnull()) & ~(archivo['precio'].isnull())
colador_celular = (archivo['producto'] == 'Celular') & ~(archivo['cantidad'].isnull()) & ~(archivo['precio'].isnull())
colador_celular = (archivo['producto'] == 'Celular') & ~(archivo['cantidad'].isnull()) & ~(archivo['precio'].isnull())

filas_celular = archivo[colador_celular] 
prom_celulares = promedio(filas_celular)
productos = archivo['producto'].unique()
mapa = {producto: 0 for producto in productos}

print("promedio celulares: ",prom_celulares)
print("productos: ",mapa)


#print(registros_nulos) 

#iloc para ver una fila en especifico
#print(archivo.iloc[1000])
