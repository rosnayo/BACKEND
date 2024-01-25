def calculadora(**kwargs):
    # Função para realizar cálculos básicos.
    ope = kwargs['ope']  # Tipo de operacion
    n1 = int(kwargs.get('n1'))
    n2 = int(kwargs.get('n2'))
    if ope == 'suma':
        resultado = n1 + n2
    elif ope == 'resta':
        resultado = n1 - n2
    elif ope == 'multiplicacion':
        resultado = n1 * n2
    elif ope == 'division':
        resultado = n1 / n2
    else:
        raise ValueError("Operación no válida")
    return {'resultado': float("%.4f" % resultado)}

numero1 = input('Ingrese 1er numero: ')
numero2 = input('Ingrese 2do numero: ')
operaciones = ('suma','resta','multiplicacion','division')

for operacion in operaciones:
    resultado = calculadora(n1=numero1, n2=numero2, ope=operacion)
    print(f'La {operacion} de {numero1} y {numero2} es {resultado}')
    
    
    