import pandas as pd

dron = pd.read_excel(r"G:\Trabajo\Listado_Examen_Becarias_GobCba_M02_DNT_ManejoDrones.xlsx")
robotica = pd.read_excel(r"G:\Trabajo\Calificaciones_SEU_DNT_M03_IntroRob_Becarias.xlsx")
programacion = pd.read_excel(r"G:\Trabajo\Calificaciones_M01_DNT_IntroProg_BecasGobCba_V01.xlsx")
new_lista = pd.concat([dron, robotica, programacion])
new_lista.to_excel("Nomina de becas.xlsx", index = False, sheet_name = "hoja1", header = 1)

































#df = pd.DataFrame(dron, columns = ["Beca"])
#resultado = df.to_excel("prueba.xlsx")
#todo = pd.concat([dron, robotica, programacion])
#print(robotica)
#print(progrmacion)
#print(todo)
