from datetime import date
atual = date.today().year
print('='*20)
print('CLASSIFICAÇÂO DOS ATLÈTAS')
print('='*20)
ano = int(input('Qual é o ano de nascimento do atleta? '))
classificacao = atual - ano
if classificacao <=9: 
  print('='*20)
  print('O atleta tem {} anos e é da classificação Mirim'.format(classificacao))
  print('='*20)
elif classificacao <=14:
  print('='*20)
  print ('o atleta tem {} anos e é da classificação Infantil'.format(classificacao)) 
  print('='*20)
elif classificacao <=19:
  print('='*20)
  print('o atleta tem {} anos e é da classificação Júnior'.format(classificacao))
  print('='*20)
elif classificacao <=25:
  print('='*20)
  print('o atleta tem {} anos e é da classificação Sênior'.format(classificacao))
  print('='*20)
elif classificacao >25:
  print('='*20)
  print('O atleta tem {} anos e é da classificação Master'.format(classificacao))
  print('='*20)




