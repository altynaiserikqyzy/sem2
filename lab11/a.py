import psycopg2  # библиотека для работы с PostgreSQL
import csv       # для чтения CSV файлов
import sys       # для завершения работы программы в случае ошибки

# Параметры подключения к базе данных
DSN = {
    'host':     'localhost',
    'database': 'lab11',
    'user':     'postgres',
    'password': '1234',
    'port':     '5432'
}

# Функция для поиска контактов по шаблону
def search_contacts(cur):
    pat = input("Введите шаблон поиска: ").strip()
    cur.execute("SELECT * FROM search_contacts(%s)", (pat,))
    rows = cur.fetchall()
    if not rows:
        print("Совпадений не найдено.")
    else:
        print("\nID | Имя                  | Телефон")
        print("---+----------------------+---------------")
        for _id, name, phone in rows:
            print(f"{_id:2d} | {name:20s} | {phone}")
    print()

# Функция для добавления нового контакта или обновления существующего
def upsert_contact(cur, conn):
    name  = input("Имя: ").strip()
    phone = input("Телефон: ").strip()
    cur.execute("CALL upsert_contact(%s, %s)", (name, phone))
    conn.commit()
    print(f"Сохранено: {name} → {phone}\n")

# Функция для массовой вставки контактов из CSV файла
def batch_insert_from_csv(cur, conn):
    path = input("Путь к CSV файлу: ").strip()
    try:
        with open(path, newline='', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            inputs = [(r['name'], r['phone']) for r in reader]
    except Exception as e:
        print("Ошибка при чтении CSV файла:", e)
        return

    if not inputs:
        print("CSV пустой или отсутствуют заголовки 'name','phone'.")
        return

    rows_sql = ",".join("ROW(%s,%s)" for _ in inputs)
    sql = f"SELECT * FROM batch_insert_contacts(ARRAY[{rows_sql}]::contact_input[]);"
    params = [val for pair in inputs for val in pair]

    cur.execute(sql, params)
    bad = cur.fetchall()
    conn.commit()

    if bad:
        print("Некорректные записи (не добавлены/обновлены):")
        for name, phone in bad:
            print(f"{name} → {phone}")
    else:
        print("Все записи успешно добавлены/обновлены.")
    print()

# Функция для постраничного отображения контактов
def paginate_contacts(cur):
    try:
        lim    = int(input("Лимит (по умолчанию 10): ").strip() or 10)
        offset = int(input("Смещение (по умолчанию 0): ").strip() or 0)
    except ValueError:
        print("Введите корректные целые числа.")
        return

    cur.execute("SELECT * FROM paginate_contacts(%s, %s)", (lim, offset))
    rows = cur.fetchall()

    if not rows:
        print("Нет данных для отображения.")
    else:
        print(f"\nПоказано до {lim} записей начиная с позиции {offset}:")
        print("ID | Имя                  | Телефон")
        print("---+----------------------+---------------")
        for _id, name, phone in rows:
            print(f"{_id:2d} | {name:20s} | {phone}")
    print()

# Функция для удаления контактов по шаблону имени или телефона
def delete_contact(cur, conn):
    name_pat  = input("Шаблон имени (ILIKE, напр. '%Иван%') или пусто: ").strip() or None
    phone_pat = input("Шаблон телефона (ILIKE, напр. '+7701%') или пусто: ").strip() or None

    if not name_pat and not phone_pat:
        print("Нечего удалять.\n")
        return

    cur.execute("CALL delete_contact_by(%s, %s)", (name_pat, phone_pat))
    conn.commit()
    print("Удаление завершено.\n")

# Основная функция с CLI меню
def main():
    try:
        conn = psycopg2.connect(**DSN)
    except Exception as e:
        print("Не удалось подключиться к базе данных:", e)
        sys.exit(1)

    cur = conn.cursor()

    menu = """
===== Телефонная книга =====
1. Поиск контактов
2. Добавить или обновить контакт
3. Массовая вставка из CSV
4. Постраничный вывод
5. Удаление по имени или телефону
0. Выход
"""
    while True:
        print(menu)
        choice = input("Выберите опцию: ").strip()
        if choice == "1":
            search_contacts(cur)
        elif choice == "2":
            upsert_contact(cur, conn)
        elif choice == "3":
            batch_insert_from_csv(cur, conn)
        elif choice == "4":
            paginate_contacts(cur)
        elif choice == "5":
            delete_contact(cur, conn)
        elif choice == "0":
            break
        else:
            print("Неверный выбор. Попробуйте снова.\n")

    # Закрываем соединение с базой данных
    cur.close()
    conn.close()
    print("До свидания!")

# Точка входа в программу
if __name__ == "__main__":
    main()