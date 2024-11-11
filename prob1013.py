valores = input().split()
a = int(valores[0])
b = int (valores[1])
c = int ( valores[2])


maior_ab = (a + b + abs(a-b))/2
maior_de_todos = (maior_ab + c + abs(maior_ab - c))/2
print (f'{maior_de_todos:.0f} eh o maior')


# maior = max(a,b,c)
# print (f'{maior} eh o maior')



# if a > b and a > c :
#     print (f'{a} eh o maior')
# elif b > a and b > c :
#     print (f'{b} eh o maior')
# elif c > a and c > b:
#     print(f'{c} eh o maior')