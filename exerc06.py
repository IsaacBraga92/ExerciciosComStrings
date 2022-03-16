# Data por extenso. Faça um programa que solicite a data de nascimento (dd/mm/aaaa) do usuário e imprima a data com o
# nome do mês por extenso.
#
# Data de Nascimento: 29/10/1973
# Você nasceu em  29 de Outubro de 1973.
def mes_por_extenso(dia, mes, ano):
    meses = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho',
             'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']
    mes_extenso = ''
    i = 0
    mes = int(mes)
    while mes - 1 != i:
        i += 1
        if mes - 1 == i:
            mes_extenso = meses[i]
            break
    return f"{dia} de {mes_extenso} de {ano}"


data = '29/10/1973'
d, m, a = data.split('/')
print (mes_por_extenso(d,m,a))
