import pandas as pd

# 1) cargar archivo
archivo = pd.read_csv('ventas.csv')

# 2) mostrar 5 primeras filas
print(archivo.head())

# 3) numero de filas y columnas
print(archivo.shape)

# 4) mirar tipo de dato de cada columna

# explicacion: se escoge una row cualquiera y se recorre columa por columna
for columna in archivo.columns:
    print("valor: ",archivo.iloc[1000][columna])
    print("tipo: ",type(archivo.iloc[1000][columna]))


# 5) ver valores null

# colador de nulos que sirve como filtro
colador_nulos = archivo.isnull().any(axis=1)

# data frame colado por el filtro de solo nulls
registros_nulls = archivo[colador_nulos]

print(registros_nulls)