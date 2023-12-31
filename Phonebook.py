import json


def save():
    with open("phonebook.json", "w", encoding="utf-8") as pb:
        pb.write(json.dumps(phonebook, ensure_ascii=False))
    print("Ваш телефонный справочник сохранен")

def load():
    with open("phonebook.json", "r", encoding="utf-8") as pb:
        phonebook = json.load(pb)
    print("Телефонная книга загружена")
    return phonebook

def print_book():
    print("Список всех контактов:")
    for name, values in phonebook.items():
        print_cont(name)

def print_cont(contact):
    temp_cont = phonebook[contact]
    print(f"{contact}:")
    if "phones" in temp_cont:
        print("    тел.: ", temp_cont["phones"])
    if "email" in temp_cont:
        print(f"    email: {temp_cont["email"]}")
    if "birthday" in temp_cont:
        print(f"    день рождения: {temp_cont["birthday"]}")

def add_cont():
    contact = input("Введите имя: ")
    if contact in phonebook:
        print("Контакт с таким именем уже существует")
    else:
        temp = {}
        number_of_telephones = int(input("Сколько номеров будет у контакта: "))
        if number_of_telephones > 1:
            for i in range(number_of_telephones):
                phones = []
                phone = input(f"Введите {i+1}-й номер телефона: ")
                phones.append(phone)
            temp.update({"phones": phones})
        elif number_of_telephones == 1:
            phones = input(f"Введите номер телефона: ")
            temp.update({"phones": phones})
        email = input("Введите почту: ")
        if email != "":
            temp.update({"email": email})
        birthday = input("Введите день рождения: ")
        if birthday != "":
            temp.update({"birthday": birthday})
        print(temp)
        phonebook.update({contact: temp})
        save()
        print("Контакт добавлен")

def edit_cont():
    contact = input("Введите имя контакта, который хотите изменить: ")
    if contact in phonebook:
        temp = phonebook[contact]
        print(f"Текущие данные: {contact}: {temp}")
        if "phones" in temp:
            phones = True
        else:
            phones = "False"
        number_of_telephones = input("Сколько номеров будет у контакта (для удаления введите 0, оставить как есть - ни чего не вводите): ")
        if number_of_telephones != "":
            number_of_telephones = int(number_of_telephones)
            if number_of_telephones > 1:
                for i in range(number_of_telephones):
                    phones = []
                    phone = input(f"Введите {i+1}-й номер телефона: ")
                    phones.append(phone)
                temp.update({"phones": phones})
            elif number_of_telephones == 1:
                phones = input(f"Введите номер телефона: ")
                temp.update({"phones": phones})
            elif number_of_telephones == 0 and phones == True:
                del temp["phones"]
        email = input("Введите почту (для удаления введите /del, чтобы оставить как есть - ни чего не вводите): ")
        if email == "/del":
            if "email" in temp:
                del temp["email"]
            else:
                print("Удалять нечего")
        elif email != "":
            temp.update({"email": email})
        birthday = input("Введите день рождения (для удаления введите /del, чтобы оставить как есть - ни чего не вводите): ")
        if birthday == "/del":
            if "birthday" in temp:
                del temp["birthday"]
            else:
                print("Удалять нечего")
        elif birthday != "":
            temp.update({"birthday": birthday})
        phonebook.update({contact: temp})
        print("Измененные данные: ",end="")
        print_cont(contact)
        print("Контакт изменен")
        save()
    else:
        print("Контакта с таким именем не существует")

def help():
    print(
        "Список доступных команд:\n\
        /help   - вывести список доступных команд\n\
        /load   - загрузить телефонный справочник\n\
        /save   - сохранить телефонный справочник\n\
        /find   - поиск (просмотр) контакта\n\
        /edit   - изменить контакт\n\
        /add    - добавить контакт\n\
        /del    - удалить контакт\n\
        /all    - посмотреть все контакты\n\
        /exit   - выход"
    )

help()
phonebook = load()

while True:
    command = input("Введите команду: ")
    if command == "/load":
        phonebook = load()
    elif command == "/add":
        add_cont()
    elif command == "/help":
        help()
    elif command == "/find":
        contact = input("Введите имя: ")
        if contact in phonebook:
            print_cont(contact)
        else:
            print("Контакт с таким именем не найден")
    elif command == "/save":
        save()
    elif command == "/edit":
        edit_cont()
    elif command == "/all":
        print_book()
    elif command == "/del":
        contact = input("Введите имя: ")
        if contact in phonebook:
            del phonebook[contact]
            print(f"Контакт {contact} удален")
        else:
            print("Контакт с таким именем не найден")
        save()
    elif command == "/exit":
        save()
        print("Вы вышли из телефонного справочника")
        break
    else:
        print("Введена несуществующая команда, попробуйте еще раз")