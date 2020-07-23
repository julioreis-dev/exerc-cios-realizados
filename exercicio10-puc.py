lista = [2, 4, 6, 10]
soma = 0
geral = []
for n in lista:
   valor = n
   soma = valor + soma
media = soma/len(lista)
for t in lista:
    dif = abs(t - media)
    resultado = (dif, t)
    geral.append(resultado)

organizado = sorted(geral)
resultado_exercicio = organizado[0][1]
print(resultado_exercicio)