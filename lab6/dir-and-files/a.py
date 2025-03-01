import os
path = input("Введите путь к директории: ")
if not os.path.exists(path):
    print("Указанный путь не существует.")
else:
    all_items = os.listdir(path)
    directories = [d for d in all_items if os.path.isdir(os.path.join(path, d))]
    files = [f for f in all_items if os.path.isfile(os.path.join(path, f))]
    print("\nДиректории:")
    for d in directories:
        print(d)
    print("\nФайлы:")
    for f in files:
        print(f)
    print("\nВсе элементы (файлы и директории):")
    for item in all_items:
        print(item)