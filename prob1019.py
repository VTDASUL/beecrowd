tempo_segundo = int(input())

list_result = []
list_divs = [3600, 60, 1]
for div in list_divs:
    div_int = tempo_segundo // div
    tempo_segundo = tempo_segundo % div
    list_result.append(div_int)

print(f'{list_result[0]}:{list_result[1]}:{list_result[2]}')