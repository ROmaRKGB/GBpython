"""Пользователь вводит время в секундах. Переведите время в часы, минуты, секунды и
выведите в формате чч:мм:сс. Используйте форматирование строк."""
print("Задание №2")
seconds_time = int(input("Введите время в секундах "))
hour_time = (seconds_time) // 3600
minuts_time = (seconds_time) // 60
second_time = (seconds_time) % 60
print(f"Ваше время {hour_time} : {minuts_time} : {seconds_time}")