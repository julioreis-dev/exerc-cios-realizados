def triangular(numero):
    return numero+1

numero_informado = int(input('digite um numero?'))
x=triangular(numero_informado)

for t in range (1, x):
    for n in range(1, t+1):
        print(t, end='')
    print('')