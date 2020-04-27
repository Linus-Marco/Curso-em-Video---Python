'''
Exercício Python 006:
Crie um algoritmo que leia um número
e mostre o seu dobro, triplo e raiz quadrada.
'''

n = int(input('\nDigite um número inteiro: '))
dobro = n*2
triplo = n*3
raiz = n**(1/2)

print('\nO dobro de {} é {}'.format(n, dobro))
print('O triplo de {} é {}'.format(n, triplo))
print('A raiz quadrada de {} é {:.3f}'.format(n, raiz))
