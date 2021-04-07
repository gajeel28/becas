import pandas as pd

df_dron = pd.read_excel(r"C:\Users\20361433069\Desktop\becas\Listado Examen Becarias GobCba M02_DNT_ManejoDrones (1).xlsx")
df_robotica = pd.read_excel(r"C:\Users\20361433069\Desktop\becas\Calificaciones SEU_DNT_M03_IntroRob_Becarias.xlsx")
df_programacion = pd.read_excel(r"C:\Users\20361433069\Desktop\becas\Calificaciones M01_DNT_IntroProg_BecasGobCba_V01 (1).xlsx")

df_dron['Beca'] = 'Manejo de dron'
df_robotica['Beca'] = 'Robotica'
df_programacion['Beca'] = 'Programacion'

new_lista = pd.concat([df_dron, df_robotica, df_programacion])
new_lista.to_excel("Nomina de becas.xlsx", index = False, sheet_name = "hoja1", header = 1)






























#new_dron = pd.concat([df_dron, df_1], axis = 1, sort = False) # se agrega la columna beca en la lista de dron
#new_robotica = pd.concat([df_robotica, df_2], axis = 1, sort = False)# se agrega la columna beca a la lista robo
#new_programacion = pd.concat([df_programacion, df_3], axis = 1, sort = False) # se agrega beca a la lista programacion
#df = pd.DataFrame(dron, columns = ["Beca"])
