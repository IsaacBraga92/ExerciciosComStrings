# Nome ao contrário em maiúsculas. Faça um programa que permita ao usuário digitar o seu nome e em seguida mostre o
# nome do usuário de trás para frente utilizando somente letras maiúsculas. Dica: lembre−se que ao informar o nome o
# usuário pode digitar letras maiúsculas ou minúsculas.

nome = input("Digite um nome: ")

print(f"O nome digitado foi: {nome}")
nome = nome.upper()
inverter_letras = ''.join(reversed(nome))
print(f"Nome invertido por letras: {inverter_letras}")
inverter_palavras = ' '.join(reversed(nome.split()))
print(f"Nome invertido por palavras: {inverter_palavras}")


