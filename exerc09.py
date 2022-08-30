# Verificação de CPF. Desenvolva um programa que solicite a digitação de um número de CPF no formato xxx.xxx.xxx-xx e
# indique se é um número válido ou inválido através da validação dos dígitos verificadores edos caracteres de
# formatação.
import re


def validarCPF(numero_cpf: str) -> bool:
    numeros_cpf = [int(digito) for digito in numero_cpf if digito.isdigit()]
    if len(numeros_cpf) != 11 or len(set(numeros_cpf)) == 1:
        return False
    soma_dos_produtos = sum(a * b for a, b in zip(numeros_cpf[0:9], range(10, 1, -1)))
    primeiro_digito = (soma_dos_produtos * 10 % 11) % 10
    if numeros_cpf[9] != primeiro_digito:
        return False
    soma_dos_produtos = sum(a * b for a, b in zip(numeros_cpf[0:10], range(11, 1, -1)))
    segundo_digito = (soma_dos_produtos * 10 % 11) % 10
    if numeros_cpf[10] != segundo_digito:
        return False
    return True


cpf = input("Informe o CPF: ")
if validarCPF(cpf):
    print("CPF válido")
else:
    print("CPF inválido")

