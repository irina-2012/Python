# запуск основных команд

import view
import model
import text

phone_book = model.PhoneBook()


def start():
    while True:  # для того, что бы выбор был цикличен, до момента выбора case 8
        option = view.main_menu()
        match option:
            case 1:
                phone_book.open_book()
                view.print_message(text.open_successful)
            case 2:
                phone_book.save_pb()
                view.print_message(text.save_successful)
            case 3:
                pb = phone_book.get_pb()  # возвращает phone_book
                if pb:
                    view.print_contacts(pb, text.pb_empty)
                else:
                    view.print_message(text.error_open_file)
            case 4:
                pb = phone_book.get_pb()
                if pb:
                    contact = view.input_contact(text.input_new_contact)
                    name = phone_book.add_contact(contact)
                    view.print_message(text.new_contact_successful(name))
                else:
                    view.print_message(text.error_open_file)
            case 5:
                pb = phone_book.get_pb()
                if pb:
                    key_word = view.input_search(text.input_search)
                    result = phone_book.search_contact(key_word)
                    view.print_contacts(result, text.empty_search(key_word))
                else:
                    view.print_message(text.error_open_file)
            case 6:
                pb = phone_book.get_pb()
                if pb:
                    key_word = view.input_search(text.input_change)
                    result = phone_book.search_contact(key_word)
                    if result:
                        if len(result) != 1:  # если несколько человек
                            view.print_contacts(result, ' ')
                            current_id = view.input_search(text.input_index)
                        else:
                            current_id = int(result[0].get('id'))
                        # условия для всех
                        new_contact = view.input_contact(text.change_contact)
                        name = phone_book.change_contact(new_contact, current_id)
                        view.print_message(text.change_successful(name))
                    else:
                        view.print_message(text.empty_search(key_word))
                else:
                    view.print_message(text.error_open_file)
            case 7:
                pb = phone_book.get_pb()
                view.print_contacts(pb, text.error_open_file)
                if pb:
                    index = view.input_index(pb, text.input_index_delete)  # выбор индекса на удаление
                    if view.confirm(text.confirm_delete(pb[index - 1].get('name'))):  # если y, то удаляем
                        view.print_message(text.delete_contact_successful(phone_book.remove_contact(index)))
                    else:
                        view.print_message(text.error_delete_contact)
            case 8:
                if view.confirm(text.confirm_exit()):
                    break
