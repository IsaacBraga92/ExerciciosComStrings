# Conta espaços e vogais. Dado uma string com uma frase informada pelo usuário (incluindo espaços em branco), conte:
#
# quantos espaços em branco existem na frase.
# quantas vezes aparecem as vogais a, e, i, o, u.
from unicodedata import normalize

frase = input("Digite uma frase: ")
frase = normalize('NFD', frase).lower()
vogais = 'aeiou'
contador_vogais = 0
contador_espacos = 0
auxiliar = ''
for i in frase:
    if i in vogais:
        contador_vogais += 1
    elif i == ' ':
        contador_espacos += 1

print(f"Quantidade de vogais: {contador_vogais}")
print(f"Quantidade de espaços: {contador_espacos}")

