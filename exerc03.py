# Nome na vertical. Faça um programa que solicite o nome do usuário e imprima-o na vertical.
#
# F
# U
# L
# A
# N
# O

nome = 'FULANO'
# Duas opções:

print(*nome, sep='\n')
print('-'*20)
for x in nome:
    print(x)
