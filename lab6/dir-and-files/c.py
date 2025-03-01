import os
path=input("Введите путь: ")
if os.path.exists(path):
    print("Путь существует.")
    print("Имя файла:",os.path.basename(path))
    print("Директория:",os.path.dirname(path))
else:
    print("Путь не существует.")