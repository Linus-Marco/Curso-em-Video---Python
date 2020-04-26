'''
Exercício Python 004:
Faça um programa que leia algo pelo teclado
e mostre na tela o seu tipo primitivo
e todas as informações possíveis sobre ele.
'''

n = input('\nDigite algo: ')
print('O tipo primitivo desse valor é: ', type(n))
print('É alfanumérico? ', n.isalnum())
print('É alfabético? ', n.isalpha())
print('É numérico? ', n.isnumeric())
print('Só tem espaços? ', n.isspace())
print('Está em maiúsculas? ', n.isupper())
print('Está em minúsculas? ', n.islower())
print('Está capitalizada? {}'.format(n.istitle()))
