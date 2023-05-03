def es_primo(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

primos = []

for i in range(1, 1001):
    if es_primo(i):
        primos.append(i)

print("Hay", len(primos), "números primos entre 1 y 1000, que son:", primos)

