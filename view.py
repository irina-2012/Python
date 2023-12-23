import text  # Импорт модуля text
import model


def main_menu() -> int:  # Выбор пункта меню, возвращает выбранный пункт(int)
    print(text.menu)  # text - модуль, menu - объект. считывает сколько строк в menu
    while True:
        option = input(text.input_option)
        if option.isdigit() and 0 < int(option) < 9:  # Проверка на правильность выбора цифры
            return int(option)


def print_message(message: str):  # печать сообщений
    print('\n' + '=' * len(message))
    print(message)
    print('=' * len(message) + '\n')


def print_contacts(book: list[dict[str, str]], error: str):
    max_size = search_max_len_pb(book)
    if book:  # если данные заполнены
        print('\n' + '=' * (max_size + 22 * 2))
        for contact in book:
            print(f'{contact.get("id")}.{contact.get("name"):<20} | '  # по середине :^
                  f'{contact.get("phone"):<20} | '
                  f'{contact.get("comm"):<20}')
        print('=' * (max_size + 22 * 2) + '\n')
    else:
        print_message(error)


def input_contact(message) -> [dict[str, str]]:
    new = {}
    print(message)
    for key, txt in text.new_contact.items():
        value = input(txt)
        if value:
            new[key] = value  # Вводим данные с клавиатуры в каждый key
    return new


def input_index(book: list, message: str) -> int:
    while True:
        index = input(message)
        if index.isdigit() and 0 < int(index) < len(book) + 1:
            return int(index)


def confirm(message: str):
    answer = input(message + ' (y/n): ')
    if answer.lower() == 'y':
        return True
    return False


def input_search(message) -> str:
    return input(message)


def search_max_len_pb(book: list[dict[str, str]]) -> int:
    len_dict = []
    # добавление элементов словарей в лист
    for contacts in book:
        for key, value in contacts.items():
            len_dict.append([key, value])
    list_summ = []
    # поиск максимальной длины
    for contact in len_dict:
        summ = 0
        for i in contact:
            summ = summ + len(i)
        list_summ.append(summ)
    return max(list_summ)
