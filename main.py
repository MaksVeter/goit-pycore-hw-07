from contacts_bot import parse_input, add_contact, add_phone, add_birthday, get_contact_phones, get_upcoming_birthdays, get_all, show_birthday, change_phone, AddressBook


def main():
    book = AddressBook()
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, book))
        elif command == "add_phone":
            print(add_phone(args, book))
        elif command == "change":
            print(change_phone(args, book))
        elif command == "phone":
            print(get_contact_phones(args, book))
        elif command == "add-birthday":
            print(add_birthday(args, book))
        elif command == "show-birthday":
            print(show_birthday(args, book))
        elif command == "birthdays":
            print(get_upcoming_birthdays(book))
        elif command == "all":
            print(get_all(book))
        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()
