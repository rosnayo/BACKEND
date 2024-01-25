capitales = {
    'Peru':'Lima',
    'Ecuador' : 'Quito',
    'Chile' : 'Santiago',
    'Colombia': 'Bogota',
    'Bolivia':'Sucre',
}
#recorrido por claves
for pais in capitales.keys():
    print("La capital de",pais,"es",capitales[pais])

print('*'*30)
#Recorrido por valores
for ciudad,pais in capitales.items():
    print(ciudad + " es la capital de "+pais )
    
print('*'*30)

#Recorrido por valores 2
for valor in capitales.values():
    print(valor)

print('*'*30)

#Recorrido por clave y valor
for clave,valor in capitales.items():
    print(f'La capital de {clave} es {valor}')
