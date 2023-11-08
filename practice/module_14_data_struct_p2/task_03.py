class UserManager:
    def __init__(self):
        self.users = {}

    def add_user(self, username: str, password: str) -> None:
        if username in self.users:
            print("User already exists.")
        else:
            self.users[username] = password
            print("User added successfully")

    def delete_user(self, username: str) -> None:
        if username in self.users:
            del self.users[username]
            print("User deleted successfully")
        else:
            print("User does not exist.")

    def check_user(self, username: str) -> None:
        if username in self.users:
            print("User exists.")
        else:
            print("User does not exist.")

    def change_login(self, old_username: str, new_username: str) -> None:
        if old_username in self.users:
            if new_username in self.users:
                print("The new login is already taken.")
            else:
                self.users[new_username] = self.users.pop(old_username)
                print("Login changed successfully.")
        else:
            print("User does not exist.")

    def change_password(self, username: str, password: str) -> None:
        if username in self.users:
            self.users[username] = password
            print("Password changed successfully.")
        else:
            print("User does not exist.")


def user_interaction() -> None:
    user_manager = UserManager()

    while True:
        print("\nMenu:")
        print("1. Add a new user.")
        print("2. Delete an existing user.")
        print("3. Check if a user exists.")
        print("4. Change the login of an existing user.")
        print("5. Change the password of an existing user.")
        print("6. Exit.")
        choice = input("Choose an option: ")

        match choice:
            case "1":
                username = input("Enter the new username: ")
                password = input("Enter the new password: ")
                user_manager.add_user(username, password)
            case "2":
                username = input("Enter the username to delete: ")
                user_manager.delete_user(username)
            case "3":
                username = input("Enter the username to check: ")
                user_manager.check_user(username)
            case "4":
                old_username = input("Enter the current username: ")
                new_username = input("Enter the new username: ")
                user_manager.change_login(old_username, new_username)
            case "5":
                username = input("Enter the username for password change: ")
                new_password = input("Enter the new password: ")
                user_manager.change_password(username, new_password)
            case "6":
                print("Exiting the program.")
                break
            case _:
                print("Invalid option, please try again.")


if __name__ == "__main__":
    user_interaction()
