import sorter

known_commands = ("add", "change", "phone", "show", "hello", "help", "sort")
exit_commands = ("goodbye", "close", "exit", ".")

def main():
    # Main function for user iteraction
    while True:
        input_text = input(">>>")
        if input_text == "":
            print(f"Empty input!")
            continue  # Repeat wait for input
        input_command = (input_text.split()[0].lower())
        if input_command in exit_commands:
            print(f"Goodbye!")
            break
        elif input_command in known_commands:
            print(f"Known command")
            if input_command == "sort":
                sorter.main(input_text)
        else:
            print(f"Don't know this command")


if __name__ == "__main__":
    print("Start program")
    main()