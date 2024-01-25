"""
De la siguiente lista de numeros
numeros = [1,2,3,4,5,6,7,8,9,10]

retorna una lista solo con los numeros pares
para sacar el residuo de un numero se usa %
4 % 2 = 0

"""
#ENTRADA
numeros = [1,2,3,4,5,6,7,8,9,10]
print(numeros)
#PROCESO
pares = [] #creamos una nueva lista vacia para guardar los numeros pares
for numero in numeros: #recorremos cada elemento de la lista "numeros
    if numero % 2 == 0: #si el residuo es cero entonces es
        pares.append(numero) #lo agregamos a la lista de pares
#SALIDA
print(pares)

#USANDO LIST COMPREHENSIONS
pares_v2 = [numero for numero in numeros if numero % 2 == 0]
print(pares_v2)