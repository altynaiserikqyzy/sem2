filename=input("Введите имя файла: ")
try:
    with open(filename,'r',encoding="utf-8") as file:
        line_count=sum(1 for line in file)
    print("Количество строк в файле:",line_count)
except FileNotFoundError:
    print("Файл не найден.")