print('Gerador de PA')
print('-=-' * 20)
primeiro =  int(input('Primeiro termo: '))
razao =  int(input(' Razão: '))
termo = primeiro
cont = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont <= total:

        print('{} >'.format(termo), end=' ')
        termo += razao
        cont += 1
    print('Pausa')
    mais = int(input('Quantos termos você quer mostrar mais? '))
print('Progresso finalizado com {} termos'.format(total))