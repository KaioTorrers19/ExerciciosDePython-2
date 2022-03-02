casa = float (input('Qual é o valor da casa?:'))
salario = float (input('Qual é o salário?:'))
anos = int (input('Quantos anos de financiamento?:'))
prestacao = casa/(anos * 12)
minimo = salario * 30/100

print('-'*15)
print('Para pagar a casa de valor {} em {}  anos'.format(casa,anos), end='') 

print('a prestação será de {}'.format(prestacao))
if prestacao<= minimo:
  print('Emprestimo concedido')
else:
  print('Emprestimo negada ')
  print('-'*15)