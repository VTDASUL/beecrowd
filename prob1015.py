x = input().split()
y = input().split()

x1, y1 = float(x[0]), float(x[1])
x2, y2 = float(y[0]), float(y[1])

distancia = (((x2 - x1)**2) + ((y2 - y1)**2))**(1/2)

print(f'{distancia:.4f}')

