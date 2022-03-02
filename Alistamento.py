from datetime import date
atual = date.today().year
print('-' *20)
print('Alistamento Militar')
print('-'*20)
nasc = int(input('Seu ano de nascimento: '))
idade = atual - nasc

if idade < 18:
    print ('='*20)
    alistamento = 18 + idade
    print('Você ainda esta com {} anos, faltará {} anos para se alistar'.format(idade,alistamento))
    print ('=')
elif idade >18:
    print('='*20)
    alistamento = 18 - idade
    print('Você tem {} e já se alistou áh {} ano atrás'.format(idade,alistamento))
    print ('='*20)  
elif idade == 18:
    print('='*20)
    print('Você precisa se alistar imediatamente!')
    print('='*20)
