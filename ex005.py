'''
Exercício Python 005:
Faça um programa que leia um número Inteiro
e mostre na tela o seu sucessor e seu antecessor.
'''

n = int(input("\nFavor informe um número inteiro: "))
na = n - 1
ns = n + 1
print('\nNúmero digitado: {}\nAntecessor: {}\nSucessor: {}'.format(n, na, ns))
