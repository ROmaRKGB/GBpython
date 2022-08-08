"""Пользователь вводит целые положительные числа. Найдите самую большую цифру в числе.
Для решения используйте цикл while и арифметические операции."""
print("Задание №4")
first_number = int(input('Введите число: '))
second_numder = int(input('Введите число: '))
third_number = int(input('Введите число: '))
four_number = int(input('Введите число: '))
i_list = [first_number, second_numder, third_number, four_number]
while i_list:
    max_number = max(i_list)
    print(f"Максимальное число {max_number}")
    break
