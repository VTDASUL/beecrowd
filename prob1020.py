idade_em_dias = int(input())

list_div = [365,30,1]
list_str = ['ano(s)', 'mes(es)', 'dia(s)']
cont = 0
for div in list_div:
    div_int = idade_em_dias //div
    idade_em_dias = idade_em_dias % div
    print(f'{div_int} {list_str[cont]}' )
    cont += 1