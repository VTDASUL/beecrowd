valores = input().split()

a = float (valores[0])
b = float (valores[1])
c = float (valores[2])

A = ( a * c)/2 
B = (c**2) * 3.14159
C = ((a + b) * c)/2
D =  b**2
E = a * b

print (f'TRIANGULO: {A:.3f}') 
print(f'CIRCULO: {B:.3f}') 
print(f'TRAPEZIO: {C:.3f}') 
print(f'QUADRADO: {D:.3f}') 
print(f'RETANGULO: {E:.3f}')

# list_str = {A:'TRIANGULO: ', B:'CIRCULO: ', C:'TRAPEZIO: ', D:'QUADRADO: ', E:'RETANGULO: '}

# for stri in list_str:
#     print(f'{list_str[stri]}{stri:.3f}')