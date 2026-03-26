import pandas as pd

archivo = pd.read_csv('ventas.csv')

print(archivo)

#oberva cuantos son null en cada columna
print(archivo.isnull().sum())

print(archivo.isnull())


#sirve para iterar sobre las filas y en esa iteracion, iterar sobre las columnas 
for i, fila in archivo.iterrows():
    print(f"fila: {i}")
    for columna in archivo.columns:
        print(columna," ",fila[columna],"\n")

#se obtienen solo los que tienen null para ver que registro y columna tiene null

#es una serie con true o false siendo true si al menos hay 1 null en toda la fila (funciona como colador)
registros_nulos = archivo.isnull().any(axis=1) 
print(registros_nulos)

#nuevo dataframe pero con las filas nulas
filas_nulas = archivo[registros_nulos]
for i, fila in filas_nulas.iterrows():
    print(f"fila: {i}")
    for columna in archivo.columns:
        print(columna," ",fila[columna],"\n")


colador_celular = (archivo['producto'] == 'Celular') & ~(archivo['cantidad'].isnull()) & ~(archivo['precio'].isnull())

filas_celular = archivo[colador_celular] 

#obtener solo los productos en una lista
productos = archivo['producto'].unique().tolist()

for i, fila in filas_celular.iterrows():
    print(f"fila: {i}")
    for columna in archivo.columns:
        print(columna," ",fila[columna],"\n")

print("productos: ",productos)


print(registros_nulos) 

#iloc para ver una fila en especifico
print(archivo.iloc[1000])
