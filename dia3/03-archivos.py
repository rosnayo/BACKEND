#Crear un archivo
archivo = open('alumnos.txt','w')
#Escribir en el archivo
archivo.write("Rafael Osnayo, rafaelosnayo@hotmail.com, 9999999999")
#Cerrar el archivo
archivo.close()

#Agregar a un archivo
archivo_agregar = open('alumnos.txt','a')
#Escribir en el archivo
archivo_agregar.write("\n")
archivo_agregar.write("Rocio Vega, correo@hotmail.com, 5555555555")
#Cerrar el archivo
archivo_agregar.close()

#Abrir para leer 
archivo_lectura = open ('alumnos.txt', 'r')
#Leer el contenido del archivo y guardarlo en una variable
alumnos = archivo_lectura.read()
#Imprimir solo los nombres de los alumnos
print(alumnos)
archivo_lectura.close()

