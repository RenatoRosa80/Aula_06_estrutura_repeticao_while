x = 0 # Necessarioa inicialização
while x < 3:
    print(x)
    x += 1 # Necessário incrementar

x = 0
while x < 3:
    for y in range(2):
        print(f"x={x}, y={y}")
    x  +=1
    