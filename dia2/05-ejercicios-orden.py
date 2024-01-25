# INGRESAR UNA LISTA DE 5 NUMEROS Y RETORNAR EL NUMERO MAYOR DE LA LISTA

########################################################
# OPCION 1
########################################################

def obtener_numero_mayor(lista):
    mayor = lista[0]
    for num in lista:
        if num > mayor:
            mayor = num
    return mayor

# Solicitar al usuario que ingrese una lista de 5 numeros
numeros = list(map(int, input("Ingrese una lista de 5 numeros separados por espacios: ").split()))

# Asegurar que el usuario haya ingresado exactamente 5 numeros
while len(numeros) != 5:
    print("Debe ingresar exactamente 5 numeros.")
    numeros = list(map(int, input("Ingrese una lista de 5 numeros separados por espacios: ").split()))

# Obtener y mostrar el numero mayor de la lista
numero_mayor = obtener_numero_mayor(numeros)
print("El numero mayor de la lista es:", numero_mayor)

########################################################
# OPCION 2 
########################################################
#ENTRADA
numeros = []
for contador in range(1,6):
    nuevo_numero = int(input(f'ingrese nro {contador} :'))
    numeros.append(nuevo_numero)
    
print(numeros)
#PROCESO
numero_mayor = numeros[0]
for numero in numeros:
    if(numero > numero_mayor):
        numero_mayor = numero

#SALIDA
print(f"El nro mayor es {numero_mayor} ")

numeros.sort(reverse=True)
print(numeros)
print(numeros[0])
