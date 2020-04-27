'''
Exercício Python 008:
Escreva um programa que leia um valor em metros
e o exiba convertido em centímetros e milímetros.
'''

m = float(input('\nInforme a medida em metros: '))
# c = m*100
# mm = m*1000
# print('A medida {} metros, é equivalente a {} centímetros e {} milímetros.'.format(m,c,mm))

print('\nA tabela de conversão da medida inserida é:')
print('{} m = {} km'.format(m, (m / 1000)))
print('{} m = {} hm'.format(m, (m / 100)))
print('{} m = {} dam'.format(m, (m / 10)))
print('{} m = {} m'.format(m, m))
print('{} m = {} dm'.format(m, (m * 10)))
print('{} m = {} cm'.format(m, (m * 100)))
print('{} m = {} mm'.format(m, (m * 1000)))
