numero= int(input('Digite um numero: '))
print('='*20)
print('''Escolha um Dos numeros para Conversão:   
[ 1 ] Converter para Binário
[ 2 ] Converter para Octal
[ 3 ] Convertor para Hexadecimal''')
print('='*20)
opcao=int(input('Sua opção: '))
if opcao == 1:
  print('='*20)
  print('o numero {} convertido para binário ficará {}'.format(numero, bin(numero)[2:]))
  print('='*20)
elif opcao == 2:
    print('='*20)
    print('o numero {} convertido para Octal ficará {} '.format(numero, oct(numero)[2:]))
    print('='*20)
elif opcao == 3:
  print('='*20)
  print('o numero {} convertido para Hexadecimal ficará {}'.format(numero, hex(numero)[2:])
  )
  print('='*20)