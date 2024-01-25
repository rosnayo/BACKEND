"""
crear un programa que ingrese un numero y cree un cuadrado con * en base al numero
ingresado

ejemplo : num = 5
resultado:

* * * * * 
*       *
*       *
*       *
* * * * *
"""
#ENTRADA
bandera = "si"
while(bandera == "si"):
    lado = int(input("Ingrese el lado del cuadrado : "))
    #PROCESO
    for contador in range(lado):
        #SALIDA
        if(contador == 0 or contador == (lado-1)):
            print('* ' * lado)
        else:
            print('*' + ('  ' * (lado-2)) + ' *')
    
    bandera = input("¿desea continuar?")


# 2DA FORMA
"""
# Definir el tamaño del lado del cuadrado
n = int(input("Ingresa un número para crear un cuadrado de asteriscos: "))

# Crear el cuadrado con asteriscos
for i in range(n):
    for j in range(n):
        if i in [0, n-1] or j in [0, n-1]:
            print(" *", end="")
        else:
            print("  ", end="")
    print()

"""