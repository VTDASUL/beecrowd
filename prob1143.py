quant_line = int(input())

for line in range(1, quant_line + 1):
    print(line, (line)**2, (line * ((line)**2)))
    line += 1