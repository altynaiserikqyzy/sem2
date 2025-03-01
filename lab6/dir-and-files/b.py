import os
path = input("Введите путь: ")
if os.path.exists(path):
    print("Путь существует.")
    print("Читаемый:", os.access(path, os.R_OK))
    print("Записываемый:", os.access(path, os.W_OK))
    print("Исполняемый:", os.access(path, os.X_OK))
else:
    print("Путь не существует.")
