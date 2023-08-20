def display_page(data):
    for entry in data:
        print(entry)


def add_entry(data, entry):
    data.append(entry)
    save_to_file(data)


def edit_entry(data, index, new_entry):
    data[index] = new_entry
    save_to_file(data)


def search_entries(data, user_search_input):
    results = []
    for text in data:
        if all(word in text for word in user_search_input):
            results.append(text)
    print('Найдены следующие совпадения: \n')
    for word in results:
        print(word)


def save_to_file(data):
    with open("db.txt", "w") as file:
        for entry in data:
            file.write(entry + "\n")


def load_from_file():
    data = []
    with open("db.txt", "r") as file:
        for line in file:
            data.append(line.strip())
    return data


def main():
    data = load_from_file()

    while True:
        print("\nТелефонный справочник")
        print("1. Вывод записей")
        print("2. Добавление записи")
        print("3. Редактирование записи")
        print("4. Поиск записей")
        print("5. Помощь")
        print("6. Выход")
        choice = input("Выберите действие: ")

        if choice == "1":
            display_page(data)
        elif choice == "2":
            new_entry = input("Введите новую запись: ")
            add_entry(data, new_entry)
        elif choice == "3":
            index = int(input("Введите индекс записи для редактирования: ")) - 1
            new_entry = input("Введите новую запись: ")
            edit_entry(data, index, new_entry)
        elif choice == "4":
            user_search_input = input("Введите значения через запятую для поиска: ").split(',')
            search_entries(data, user_search_input)
        elif choice == "5":
            print('')
        elif choice == '6':
            print('Работа программы остановлена.')
            break
        else:
            print("Ошибка выбора пункта меню.")


if __name__ == "__main__":
    main()