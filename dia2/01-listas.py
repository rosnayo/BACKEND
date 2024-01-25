dias = ['lunes', 'martes', 'miercoles']
print(dias)
# Imprimir el indice del dia que se encuentra en la lista.
print(dias[-1])
#Agregar valor a una lista
dias.append('jueves')
dias.append('viernes')
print(dias)
#Eliminar un elemento de la lista
dias.pop(3)
print(dias)
del dias[2,3]
print(dias)
# del dias[0] # Elimina el primer elemento (Lunes).
# print(dias)
#Modificar un elemento de la lista
dias[0] = "domingo"
dias[1] = "lunes"
print(dias)
dias.append('martes')
dias.append('miercoles')
dias.append('jueves')
dias.append('viernes')
print(dias)
#Recorrer lista
for contador in range(len(dias)):
    print("El dia es:", dias[contador])

for dia in dias:
    print(dia)

#Ordenar la lista alfabeticamente
dias.sort()
print(dias)
#Revertir la orden de la lista
dias.reverse()
print(dias)
