import os


def find_file():
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
    find_file()
    create_files()
