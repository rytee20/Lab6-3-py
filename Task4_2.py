import os
import threading
from time import perf_counter


def what_file():
    while True:
        try:
            file_to_find = str(input("Ведите название файла который хотите найти: "))
            right = 0
            while right == 0:
                while file_to_find.find(".") == -1:
                    right -= 1
                    file_to_find = str(input("Название не содержит расширения\n"
                                             "Ведите название файла который хотите найти: "))
                while file_to_find.find("/") != -1 or file_to_find.find(":") != -1 or file_to_find.find("*") != -1 or \
                        file_to_find.find("?") != -1 or file_to_find.find("?") != -1 or file_to_find.find("<") != -1 or \
                        file_to_find.find(">") != -1 or file_to_find.find("|") != -1 or file_to_find.find("+") != -1 or \
                        file_to_find.find("\\") != -1 or file_to_find.find("\"") != -1:
                    right -= 1
                    file_to_find = str(input("Название содержит недопустимые символы\n"
                                             "Ведите название файла который хотите найти: "))
                while len(file_to_find) == 1:
                    right -= 1
                    file_to_find = str(input("Название не может состоять из одного символа\n"
                                             "Ведите название файла который хотите найти: "))
                if right == 0:
                    right = 1
                else:
                    right = 0
            break
        except ValueError:
            print("Вы ввели неверно")

    return file_to_find


def find_file(file_to_find):

    count = 0
    for _, _, files in os.walk(os.getcwd()):
        for filename in files:
            if filename == file_to_find:
                count += 1
                print("Такой файл есть в директории")
    if count == 0:
        print("Нет такого файла")


def find_amount_files(dic):
    _, _, files = next(os.walk(dic))
    return len(files)


def create_files():
    folder_iter = list(os.walk(os.getcwd()))
    for current_folder, _, _ in folder_iter:
        filename = "size.txt"
        amount=str(find_amount_files(current_folder))
        with open(os.path.join(current_folder, filename), "w") as f:
            f.write(amount)


if __name__ == '__main__':
    filename=what_file()

    t1 = threading.Thread(target=find_file, args=(filename,))
    t2 = threading.Thread(target=create_files, args=())

    tic = perf_counter()
    t1.start()
    t2.start()

    t1.join()
    t2.join()
    tac = perf_counter()

    print(f"Вычисление заняло {tac - tic:0.4f} секунд")
    
    #Вычисление заняло 1.4126 секунд
