def degree(a, b):
    if b == 0:
        return 1
    else:
        return a * degree(a, b - 1)


a = int(input("Введите число A: "))
b = int(input("Введите число B: "))

print(f'{a} в степени {b} = {degree(a, b)}')
