# Рекурсия. Возведение числа x в степень y

# Рекурсивная функция
def Power(x, y):
    if y>0:
        return x * Power(x, y-1)
    else:
        return 1

# Демонстрация использования функции Power()
x = 3
y = 4
res = Power(x, y)
print("res = ", res)