r1 = int(input('Primeiro  segmento'))
r2 = int(input('Segundo segmento'))
r3 = int(input('terceiro segmento'))
if r1 < r2  + r3 and r2 < r1 + r3 and r3 < r1 + r2:
  print('os segmentos acima podem formar um triangulo')

if r1 == r2 == r3:
  print('Equilátero')
elif r1 != r2 != r3:
  print('Escaleno')
else:
  print('Isóceles')
else:   
print('Os segmento acima não podem formar um triangulo')
