def create_credentials():
    proposed_username = input("Enter a username: ")
    try:
        with open("credentials.txt", "r") as file:
            existing_credentials = file.readlines()
    except FileNotFoundError:
        existing_credentials = []

    for line in existing_credentials:
        if line.startswith(f"{proposed_username}:"):
            print("This username is already taken. Please choose another.")
            create_credentials()
            return
    
    proposed_password = input("Enter a password (minimum 4 characters): ")

    while len(proposed_password) < 4:
        print("Password must be at least 4 characters long.")
        proposed_password = input("Enter a password (minimum 4 characters): ")

    
    with open("credentials.txt", "a") as file:
        file.write(f"{proposed_username}:{proposed_password}\n")

    print("Username and password created successfully.")

    
def login():
    proposed_username = input("Enter your username: ")
    proposed_password = input("Enter your password: ")

    try:
        with open("credentials.txt", "r") as file:
            existing_credentials = file.readlines()
    except FileNotFoundError:
        print("Credentials file not found.")
        return

    for line in existing_credentials:
        parts = line.strip().split(":")
        if len(parts) != 2:
            continue
        username, password = parts

        if username == proposed_username and password == proposed_password:
            with open("login_complete.txt", "w") as file:
                file.write("run")
            print("Login successful.")
            exit()

    print("Incorrect username or password.")

    choice = input("Press 1 to create a new username and password or 2 to try again: ")
    while choice not in {"1", "2"}:
        print("Invalid choice. Please enter either 1 or 2.")
        choice = input("Press 1 to create a new username and password or 2 to try again: ")

    if choice == "1":
        create_credentials()
    elif choice == "2":
        login()





def main():
    while True:
        print("1. Create username and password")
        print("2. Login")
        print("3. Exit program")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            create_credentials()
        elif choice == 2:
            login()
        elif choice == 3:
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == '__main__':
    main()