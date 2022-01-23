valor = 1000.00

n1 = str(input('Informe o nome do Primeiro Ganhador: '))
n2 = str(input('Informe o nome do Segundo Ganhador: '))
n3 = str(input('Informe o nome do Terceiro Ganhador: '))

print('O Valor de cada ganhador será !!')

print('O Ganhador {} receberá o valor de R$ {:.2f} referente ao premio de R$ {}'.format(n1, (valor*0.46), valor))
print('O Ganhador {} receberá o valor de R$ {:.2f} referente ao premio de R$ {}'.format(n2, (valor*0.32), valor))
print('O Ganhador {} receberá o valor de R$ {:.2f} referente ao premio de R$ {}'.format(n3, (valor*0.22), valor))
