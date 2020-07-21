def Converter_mes(dia, mes, ano):
    meses = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']
    resultado = str(dia) + ' de ' + meses[mes-1] + ' ' + str(ano)
    return resultado

valor1 = int(input(('Digite o dia :')))
valor2 = int(input(('Digite o dia do mês :')))
valor3 = int(input(('Digite o ano :')))

x = Converter_mes(valor1, valor2, valor3)
print(x)