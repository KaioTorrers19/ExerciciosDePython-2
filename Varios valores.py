n= 0
cont = 0
soma = 0
n = int(input('Digite um numero  [999]  para finalizar:  '))
while n != 999:
    soma += n
    cont += 1
    n = int(input('Digite um numero  [999]  para finalizar:  '))
print('você digitou {} numeros e a soma de todos dará {} '.format(cont, soma))