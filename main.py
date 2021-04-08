import pandas as pd
ruta = r"C:\Users\20361433069\Desktop\becas"
df_dron = pd.read_excel(ruta +"\Listado Examen Becarias GobCba M02_DNT_ManejoDrones (1).xlsx")
df_robotica = pd.read_excel(ruta +"\Calificaciones SEU_DNT_M03_IntroRob_Becarias.xlsx")
df_programacion = pd.read_excel(ruta +"\Calificaciones M01_DNT_IntroProg_BecasGobCba_V01 (1).xlsx")


df_dron['Beca'] = 'Manejo de dron'
df_robotica['Beca'] = 'Robotica'
df_programacion['Beca'] = 'Programacion'

df_new_lista = pd.concat([df_dron, df_robotica, df_programacion])
df_new_lista1 = df_new_lista.iloc[:, 0:5]
print(df_new_lista1)
df_new_lista1.to_excel("Nomina de becas.xlsx", index = False, sheet_name = "hoja1", header = 1)
df_suma = df_new_lista.shape
print('La cantidad es: ',df_suma)

#viendo la cantidad de veces que se repiten
df_frecuencia = df_new_lista1.groupby(['DNI']).count()
df_frecuencia.to_excel('Frecuencia que se repiten.xlsx', index = False, sheet_name ='Hoja1', header = 1)

#tratando de armar un excel para que muestre la colum "dni" y la cantidad de veces que se repiten
df_dni = df_new_lista1['DNI']
df_frec = pd.merge(df_dni, df_frecuencia, left_on = 'DNI', right_on= 'DNI')
df_frec1 = df_frec.iloc[:, 0:3]
print(df_frec1)
df_frec1.to_excel('Cantidad que se repiten.xlsx', index = False, sheet_name = 'Hoja1', header = 1)
df_suma1 = df_frecuencia.shape
print=(df_suma1)

#df_gaston = df_frec.pivot_table('DNI', 'Nombre')
#print(df_gaston)

























#solo muestra la lista filtrada con los repetidos
#df_lis_filtrada = df_new_lista1.drop_duplicates(subset=['DNI'])
#df_lis_filtrada.to_excel('Lista Filtrada.xlsx', index = False, sheet_name = 'Hoja1', header = 1)
#new_dron = pd.concat([df_dron, df_1], axis = 1, sort = False) # se agrega la columna beca en la lista de dron
#new_robotica = pd.concat([df_robotica, df_2], axis = 1, sort = False)# se agrega la columna beca a la lista robo
#new_programacion = pd.concat([df_programacion, df_3], axis = 1, sort = False) # se agrega beca a la lista programacion
#df = pd.DataFrame(dron, columns = ["Beca"])

