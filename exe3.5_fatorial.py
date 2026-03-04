def fatorial(n):
    mult = 1
    for i in range(n, 0 , -1):
        mult *= i
    return mult

print(fatorial(9))
print(fatorial(8))
print(fatorial(7))
print(fatorial(6))
print(fatorial(5))

