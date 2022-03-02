cont = 0
soma = 0
while True:
    n =int(input('Informe um valor para somar [Digite o numero 999 para parar]:  '))
    if n == 999:
        break
    cont += 1
    soma += n
print('os {} numeros somados darão {}'.format(cont, soma))