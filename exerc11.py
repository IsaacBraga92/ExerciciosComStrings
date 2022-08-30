# Jogo de Forca. Desenvolva um jogo da forca. O programa terá uma lista de palavras lidas de um arquivo texto e
# escolherá uma aleatoriamente. O jogador poderá errar 6 vezes antes de ser enforcado.
# Digite uma letra: A
# -> Você errou pela 1ª vez. Tente de novo!
# Digite uma letra: O A palavra é: _ _ _ _ O
# Digite uma letra: E A palavra é: _ E _ _ O
# Digite uma letra: S -> Você errou pela 2ª vez. Tente de novo!

import random

with open("palavras.txt", "r") as file:
    allText = file.read()
    palavras = list(map(str, allText.split()))

    palavra = random.choice(palavras).upper()

print('Jogo da Forca!')
print('Descubra a palavra!')

print("A palavra é: ", end='')
for letra in palavra:
    print(f'_ ', end='')

grupo_letras_da_palavra = set(palavra)
grupo_letras_digitadas = set()
erros = 0
while (not grupo_letras_da_palavra.issubset(grupo_letras_digitadas)) and erros < 7:
    print()
    print()
    letra_digitada = input("Informe uma Letra: ").upper()
    grupo_letras_digitadas.add(letra_digitada)
    if letra_digitada in grupo_letras_da_palavra:
        print("A palavra é: ", end='')
        for letra in palavra:
            if letra in grupo_letras_digitadas:
                print(f'{letra} ', end='')
            else:
                print(f'_ ', end='')
    else:
        erros += 1
        print(f'--> Erros {erros} de 6 . Tente novamente')
    print()
    print("Letras já digitadas: ", grupo_letras_digitadas)

if erros < 7:
    print("Você acertou a palavra.")
else:
    print("Você atingiu o limite de erros.")
