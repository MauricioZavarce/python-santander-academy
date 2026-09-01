# While and Break
contador = 0

while True:

    print(contador)
    contador += 1

    if contador == 5:
        break
# continue

for i in range(10):
    if i % 2 == 0:
        continue
    print(i)