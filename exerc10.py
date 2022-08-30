import random

with open("palavras.txt", "r") as file:
    allText = file.read()
    palavras = list(map(str, allText.split()))

    palavra = random.choice(palavras)
    print(palavra)