print("Задание №7")
a = 2
b = 3
count = 0
while a <= (b + (b/10)):
    count += 1
    print(f"{count}-й день: {a}")
    a = a*1.1
print(f"На {count} день спортсмен достиг результата не менее {b} км.")