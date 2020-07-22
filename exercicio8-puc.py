def Definir(numero):
    if (numero % 2 == 0):
        return 'Par'
    else:
        return 'Impar'

valor = int(input('Digite um numero: '))
x = Definir(valor)
print(x)