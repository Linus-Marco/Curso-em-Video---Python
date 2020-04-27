'''
Exercício Python 007:
Desenvolva um programa que leia
as duas notas de um aluno,
calcule e mostre a sua média.
'''

n1 = float(input('\nInforme a nota 1 do aluno: '))
n2 = float(input('Informe a nota 2 do aluno: '))
media = (n1+n2)/2

print('A média das notas {} e {} é {:.2f}'.format(n1, n2, media))
