# Tamanho de strings. Faça um programa que leia 2 strings e informe o conteúdo delas seguido do seu comprimento.
# Informe também se as duas strings possuem o mesmo comprimento e são iguais ou diferentes no conteúdo.
#    Compara duas strings
#    String 1: Brasil Hexa 2006
#    String 2: Brasil! Hexa 2006!
#    Tamanho de "Brasil Hexa 2006": 16 caracteres
#    Tamanho de "Brasil! Hexa 2006!": 18 caracteres
#    As duas strings são de tamanhos diferentes.
#    As duas strings possuem conteúdo diferente.

string1 = "Brasil"
string2 = "Bras1l"
print(f"{string1}, de tamanho: {len(string1)} caracteres.")
print(f"{string2}, de tamanho: {len(string2)} caracteres.")

if len(string1) == len(string2):
    print("Strings de tamanhos iguais!!!")
else:
    print("Strings de tamanhos diferentes!!!")

if string1 is string2:
    print("As strings tem o mesmo conteúdo.")
else:
    print("As strings não possuem o mesmo conteúdo.")