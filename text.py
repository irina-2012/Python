# модуль для импорта текста

menu = '''\nГлавное меню:
1. Открыть файл
2. Сохранить файл
3. Показать контакты
4. Добавить контакт
5. Найти контакт
6. Изменить контакт
7. Удалить контакт
8. Выход\n'''

input_option = 'Выберите пункт меню: '
open_successful = 'Телефонная книга открыта!'
save_successful = 'Изменения сохранены'
pb_empty = 'Телефонная книга пуста или не открыта'
input_new_contact = 'Введите данные нового контакта: '

new_contact = {'name': 'Введите Имя/Фамилию: ',
               'phone': 'Введите номер телефона: ',
               'comm': 'Введите комментарий: '}

error_delete_contact = 'Вы передумали удалять'
input_change = 'Какой контакт будем менять?: '
input_index = 'Введите индекс контакта: '
change_contact = 'Введите новые данные или оставьте пустым, что бы не менять: '
error_open_file = 'Книга пуста или не открыта!'
input_index_delete = 'Введите индекс контакта, который хотите удалить: '
input_search = 'Введите искомое значение: '


def change_successful(name: str) -> str:
    return f'Контакт {name} успешно изменён!'


def new_contact_successful(name: str) -> str:
    return f'Контакт {name} успешно добавлен'


def delete_contact_successful(name: str) -> str:
    return f'Контакт {name} успешно удален!'


def confirm_delete(name: str) -> str:
    return f'Вы точно хотите удалить {name}?'


def confirm_exit() -> str:
    return f'Вы всё сохранили и хотите выйти?'


def empty_search(word) -> str:
    return f'Контакты, содержащие слово "{word}" не найдены'



