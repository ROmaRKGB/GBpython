"""5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами. 
Программа должна подсчитывать сумму чисел в файле и выводить ее на экран. """

answer = input("Задание 5 (д/н)? ")
if answer == 'д':
    try:
        with open("texts/text_for_t5.txt", "w") as write_file:
            for _ in range(10):
                write_file.write(str(random.randint(1, 101)) + " ")
        with open("texts/text_for_t5.txt") as read_file:
            read_line = read_file.readline()
            print("\t" + read_line)
            res_sum = 0
            for str_number in read_line.split():
                res_sum += int(str_number)
            print(f"\tСумма: {res_sum}\n")
    except IOError:
        print("\tОшибка открытия файла!\n")