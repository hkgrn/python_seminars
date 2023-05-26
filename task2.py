def sum(a, b):
    if b == 0:
        return a
    else:
        return 1 + sum(a, b-1)


a = int(input("Введите число A: "))
b = int(input("Введите число B: "))

print(f'{a} + {b} = {sum(a, b)}')