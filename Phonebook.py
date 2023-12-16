import json
phonebook = {}
print("Список доступных команд:\n\
    /load - загрузить телефонный справочник\n\
    /save - сохранить телефонный справочник\n\
    /add - добавить контакт\n\
    /all - посмотреть все контакты\n\
    /exit - выход")


def save():
    with open("phonebook.json", "w", encoding="utf-8") as pb:
        pb.write(json.dumps(phonebook, ensure_ascii=False))
    print("Ваш телефонный справочник сохранен")


def load():
    with open("phonebook.json", "r", encoding="utf-8") as pb:
        phonebook = json.load(pb)
    print("Телефонная книга загружена")


def print_book():
    print("Список всех контактов:")
    for name, values in phonebook.items():
        print(name, values)


while True:
    command = input("Введите команду ")
    if command == "/add":
        contact = input("Введите имя: ")
        phones = []
        number_of_telephones = int(input("Сколько номеров будет у контакта: "))
        for i in range(number_of_telephones):
            phone = input(f"Введите телефон №{i+1}: ")
            phones.append(phone)
        email = input("Введите почту: ")
        birthday = input("Введите день рождения: ")
        phonebook[contact] = {"phones": phones}
        if email != "":
            phonebook[contact] = {"email": email}
        if birthday != "":
            phonebook[contact] = {"birthday": birthday}
        save()
        print("Контакт добавлен")
    elif command == "/save":
        save()
    elif command == "/load":
        with open("phonebook.json", "r", encoding="utf-8") as pb:
            phonebook = json.load(pb)
        print("Телефонная книга загружена")
    elif command == "/all":
        print_book()
    elif command=="/exit":
        save()
        print("Вы вышли из телефонного справочника")
        break
    else:
        print("Введена несуществующая команда, попробуйте еще раз")


# print(phonebook["Дядя Ваня"])
# print(phonebook["Дядя Ваня"]["phones"])
# print(phonebook["Дядя Ваня"]["phones"][0])
# for name, values in phonebook.items():
#     print(name, values)
