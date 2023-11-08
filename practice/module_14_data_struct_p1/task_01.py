class ListNode:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def add(self, value):
        if not self.head:
            self.head = ListNode(value)
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = ListNode(value)

    def delete(self, value):
        current = self.head
        previous = None
        while current and current.value != value:
            previous = current
            current = current.next
        if previous is None:
            self.head = self.head.next
        elif current:
            previous.next = current.next
            current.next = None

    def display(self):
        elements = []
        current = self.head
        while current:
            elements.append(current.value)
            current = current.next
        return elements

    def search(self, value):
        current = self.head
        while current:
            if current.value == value:
                return True
            current = current.next
        return False

    def replace(self, old_value, new_value):
        current = self.head
        while current:
            if current.value == old_value:
                current.value = new_value
                return True
            current = current.next
        return False


def get_int_input(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Please enter a valid integer.")


def user_interaction() -> None:
    linked_list = LinkedList()

    # Initial input of numbers
    numbers = map(int, input("Enter numbers separated by space: ").split())
    for number in numbers:
        linked_list.add(number)

    while True:
        print("\nMenu:")
        print("1. Add element to the list.")
        print("2. Delete element from the list.")
        print("3. Show the contents of the list.")
        print("4. Check if a value is in the list.")
        print("5. Replace a value in the list.")
        print("6. Exit.")
        choice = get_int_input("Choose an option: ")

        match choice:
            case 1:
                value = get_int_input("Enter the value to add")
                linked_list.add(value)
                print(f"{value=} added")
            case 2:
                try:
                    value = get_int_input("Enter the value to delete: ")
                    linked_list.delete(value)
                    print(f"Value {value} deleted.")
                except Exception as e:
                    print(e)
            case 3:
                print("List contents: ", linked_list.display())
            case 4:
                value = get_int_input("Enter the value to check: ")
                if linked_list.search(value):
                    print("Value found in the list.")
                else:
                    print("Value not in the list.")
            case 5:
                old_value = get_int_input("Enter the value to replace: ")
                new_value = get_int_input("Enter the new value: ")
                if linked_list.replace(old_value, new_value):
                    print(f"Value {old_value} replaced with {new_value}.")
                else:
                    print("Value not found in the list.")
            case 6:
                print("Exiting the program.")
                break
            case _:
                print("Invalid option, please try again.")


def main():
    user_interaction()


if __name__ == "__main__":
    main()
