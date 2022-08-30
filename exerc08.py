# Palíndromo. Um palíndromo é uma seqüência de caracteres cuja leitura é idêntica se feita da direita para esquerda
# ou vice−versa. Por exemplo: OSSO e OVO são palíndromos. Em textos mais complexos os espaços e pontuação são
# ignorados. A frase SUBI NO ONIBUS é o exemplo de uma frase palíndroma onde os espaços foram ignorados. Faça um
# programa que leia uma seqüência de caracteres, mostre−a e diga se é um palíndromo ou não.
import re
from unicodedata import normalize


def normalizar_frase(s):
    """
    Remove caracteres e acentos ignoráveis
    """
    return re.sub('[^a-zA-Z0-9]+', '', normalize('NFKD', s).encode('ASCII', 'ignore').decode('ASCII')).lower()


frase = input("Digite uma palavra: ").replace(' ', '').lower()
frase = normalizar_frase(frase)
inverter = frase[::-1]
print(frase)
print(inverter)
if frase == inverter:
    print("Palíndromos")
else:
    print("Não são palíndromos")

