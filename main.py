def display_page(page_size, selected_page, data):
    # Вывод всех записей в справочнике по страницам
    start_index = (selected_page - 1) * page_size
    end_index = start_index + page_size
    for entry in data[start_index:end_index]:
        print(entry)


def add_entry(data, entry):
    # Добавление записи в справочник
    data.append(entry)
    save_to_file(data)


def edit_entry(data, index, new_entry):
    # Изменение записи в справочнике
    data[index] = new_entry
    save_to_file(data)


def search_entries(data, user_search_input):
    # Поиск совпадений внутри справочника
    results = []
    for text in data:
        if all(word in text for word in user_search_input):
            results.append(text)
    print('Найдены следующие совпадения: \n')
    for word in results:
        print(word)


def save_to_file(data):
    # Сохранение данных справочника
    with open("db.txt", "w") as file:
        for entry in data:
            file.write(entry + "\n")


def load_from_file():
    # Загрузка справочника в память
    data = []
    with open("db.txt", "r") as file:
        for line in file:
            data.append(line.strip())
    return data


def main():
    # Основная функция main
    data = load_from_file()
    page_size: int = 5
    number_of_lines = len(data)
    amount_of_pages: int = -(-number_of_lines // page_size)

    while True:
        print("\nТелефонный справочник\n")
        print("1. Вывод записей")
        print("2. Добавление записи")
        print("3. Редактирование записи")
        print("4. Поиск записей")
        print("5. Помощь")
        print("6. Выход")
        choice = input("Выберите действие: ")

        # Вывод записей по страницам
        if choice == "1":
            print(f'В данный момент в справочнике {number_of_lines} записей')
            print(f'Количество доступных страниц: {amount_of_pages}')
            selected_page = int(input('Введите необходимую страницу: '))
            display_page(page_size, selected_page, data)
        # Добавление записи в справочник
        elif choice == "2":
            new_entry = input("Введите новую запись: ")
            add_entry(data, new_entry)
        # Редактирование записи в справочнике
        elif choice == "3":
            index = int(input("Введите индекс записи для редактирования: ")) - 1
            new_entry = input("Введите новую запись: ")
            edit_entry(data, index, new_entry)
        # Поиск записей в справочнике
        elif choice == "4":
            user_search_input = input("Введите значения через запятую для поиска: ").split(',')
            search_entries(data, user_search_input)
        # Вывод текста помощи
        elif choice == "5":
            print('Это телефонный справочник.\nВсе данные в нем хранятся в следующем виде:'
                  '\nФамилия, имя, отчество, название организации, телефон рабочий, телефон личный.')
        # Стоп
        elif choice == '6':
            print('Работа программы остановлена.')
            break
        else:
            print("Ошибка выбора пункта меню.")


if __name__ == "__main__":
    main()
