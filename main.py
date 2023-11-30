def Task1(year):
    if year % 4 == 0:
        return True
    return False

def Task2(year, month):
    if not (1 <= month <= 12):
        return None

    months_length = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    if month == 2:
        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
            return 29
    return months_length[month - 1]

print(Task2(2020, 2))  # 29 (високосний рік)
print(Task2(2021, 2))  # 28
print(Task2(2023, 4))  # 30
print(Task2(2023, 13)) # None (некоректний номер місяця)

def Task3(year, month, day):
    if not (1 <= month <= 12):
        return None

    # Довжина кожного місяця
    months_length = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    # Перевірка на високосний рік
    if month == 2 and ((year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)):
        months_length[1] = 29

    if not (1 <= day <= months_length[month-1]):
        return None

    return sum(months_length[:month-1]) + day

print(Task3(2023, 1, 1))   # 1
print(Task3(2020, 2, 29)) # 60 (високосний рік)
print(Task3(2021, 3, 1))  # 60
print(Task3(2023, 12, 31))# 365
print(Task3(2023, 2, 30)) # None (такого дня немає у лютому)
print(Task3(2023, 13, 1)) # None (некоректний номер місяця)

def Task4(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i**2 <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

# Тест функціЇ
print(Task4(2))  # True
print(Task4(7))  # True
print(Task4(8))  # False
print(Task4(25)) # False
print(Task4(29)) # True

def Task5L(liters_per_100km):
    # Конвертація з л/100км в милі/галон
    # 1 миль = 1609.344 метрів
    # 1 галон = 3.785411784 літрів
    miles_per_gallon = 100 / (liters_per_100km / 3.785411784 / 1609.344)
    return miles_per_gallon

def Task5M(miles_per_gallon):
    # Конвертація з миль/галон в л/100км
    # 1 миль = 1609.344 метрів
    # 1 галон = 3.785411784 літрів
    liters_per_100km = 3.785411784 * 100 / (miles_per_gallon * 1609.344)
    return liters_per_100km

# Приклади використання функцій:
liters_per_100km = 8.5
miles_per_gallon = 30

converted_miles_per_gallon = Task5L(liters_per_100km)
converted_liters_per_100km = Task5M(miles_per_gallon)

print(f"{liters_per_100km} л/100км = {converted_miles_per_gallon} миль/галон")
print(f"{miles_per_gallon} миль/галон = {converted_liters_per_100km} л/100км")


def is_a_triangle(a, b, c):
    # Перевіряє, чи можна побудувати трикутник зі заданими сторонами a, b, c
    if a + b > c and a + c > b and b + c > a:
        return True
    else:
        return False

def Task6(a, b, c):
    # Перевіряє, чи є трикутник прямокутним зі сторонами a, b, c
    if is_a_triangle(a, b, c):
        # Використовуємо теорему Піфагора для перевірки прямокутності
        if a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2:
            return True
    return False

# Приклади використання функції is_a_right_triangle:
a = 3
b = 4
c = 5
print(Task6(a, b, c))  # Виведе True, бо це прямокутний трикутник

a = 3
b = 4
c = 6
print(Task6(a, b, c))  # Виведе False, бо це не прямокутний трикутник