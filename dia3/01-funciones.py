def suma(numero1,numero2):
    return numero1+numero2
s1 = suma(3,4)
s2 = suma(s1,10)
print(s2)

def suma_infinito(*args):
    resultado = 0
    for numero in args:
        resultado += numero
        return resultado
    
s3 = suma_infinito(1,2,3,4,5)
print(s3)

def login(**kwargs):
    if kwargs.get('u') == 'admin' and kwargs.get('p') == '123':
        print('BIENVENIDO!!!')
    else:
        print('ERROR DE ACCESO!!!')

print('LOGIN DE USUARIOS')
usuario = input('INGRESE USUARIO: ')
password = input('INGRESE PASSWORD: ')
login(u=usuario, p=password)

