capitales = {
    'Peru':'Lima',
    'Ecuador' : 'Quito',
    'Chile' : 'Santiago',
    'Colombia': 'Bogota',
    'Bolivia':'Sucre',
}
print(capitales)
print(capitales.values())  #Imprime los valores de la diccionario
#Acceder a un elemento por su clave (llave)
ciudad=capitales['Peru']
print("La ciudad capital de Perú es: ",ciudad)

pais = input('ingrese el pais: ')
if pais in capitales:
    capital = capitales[pais]
    print ("La ciudad capital de",pais,"es: ",capital)
    print (f'La capital del {pais} es {capital}')
    eliminar_capital = input('Desea eliminar la capital? (si/no): ')
    if eliminar_capital == "si":
        capitales.pop(pais,'No existe')
        print(capitales)       
else:
    print ('No se encontro la capital de {país}')
    nueva_capital = input(f'Ingrese la capital de {pais} ')
    capitales.update({pais:nueva_capital})
    print(capitales)