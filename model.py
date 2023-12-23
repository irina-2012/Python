class PhoneBook:

    def __init__(self, path: str = 'phone_book.txt'):
        self.phone_book: list[dict[str:str]] = []
        self.path = path

    def open_book(self):
        with open(self.path, 'r', encoding='UTF-8') as file:
            data = file.readlines()  # считываем все строки с переносом строки
        for contact in data:
            contact = contact.strip().split(':')  # разделяем строки по символу ":" и убираем служебные символы
            new = {'id': contact[0],
                   'name': contact[1],
                   'phone': contact[2],
                   'comm': contact[3]}
            self.phone_book.append(new)  # считываем файл -> создаём копию и добавляем список словарей в phone_book

    def save_pb(self):
        data = []
        for contact in self.phone_book:
            data.append(':'.join([contact['id'],
                                  contact['name'],
                                  contact['phone'],
                                  contact['comm']]))  # объединяем в список каждое значение словаря по :
        data = '\n'.join(data)
        with open(self.path, 'w', encoding='UTF-8') as file:
            file.write(data)

    def get_pb(self):
        return self.phone_book

    def add_contact(self, new: dict[str, str]) -> str:  # добавляем новый контакт
        new_id = int(self.phone_book[-1].get('id')) + 1
        new['id'] = str(new_id)
        self.phone_book.append(new)
        return new.get('name')

    def search_contact(self, word: str) -> list[dict[str, str]]:
        result: list[dict[str, str]] = []
        for contact in self.phone_book:  # берём первый контакт
            for field in contact.values():  # берём каждые ЗНАЧЕНИЯ 1го контакта
                if word.lower() in field.lower():  # если значение совпало
                    result.append(contact)  # добавляем весь контакт
                    break
        return result

    def change_contact(self, new: dict, index: int) -> str:
        for contact in self.phone_book:
            if index == int(contact.get('id')):
                contact['name'] = new.get('name', contact.get('name'))
                contact['phone'] = new.get('phone', contact.get('phone'))
                contact['comm'] = new.get('comm', contact.get('comm'))
                return contact.get('name')

    def remove_contact(self, index: int) -> str:
        deleted_element = self.phone_book.pop(index - 1)
        return deleted_element.get('name')
