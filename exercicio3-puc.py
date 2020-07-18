def Calcular(a, b, c):
    x = a + b + c
    y = a * b * c
    return x, y

valor1 = int(input('Digite o primeiro valor?'))
valor2 = int(input('Digite o segundo valor?'))
valor3 = int(input('Digite o terceiro valor?'))
resultado = Calcular(valor1, valor2, valor3)
print(resultado)