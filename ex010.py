'''
Exercício Python 010:
Crie um programa que leia
quanto dinheiro em reais uma pessoa tem na carteira
e mostre quantos dólares ela pode comprar.
'''

dreal = float(input('\nInforme quantos reais você possui em sua carteira: '))
dolar = float(input('Informe a cotação do dólar atual: '))
ddolar = dreal/dolar

print('\nVocê pode comprar US$ {:.2f} com R$ {:.2f}.'.format(ddolar, dreal))
