def Mostrar_status(numero):
    if numero > 0:
        return 'P'
    elif numero < 0:
        return 'N'
    else:
        return'0'

valor = int(input('Digite um numero?'))
x = Mostrar_status(valor)
print(x)