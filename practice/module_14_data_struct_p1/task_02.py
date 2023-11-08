from typing import Any, Optional


class DoublyListNode:
    """A node for use in a doubly_linked list."""

    def __init__(self, value: str) -> None:
        self.value: Any = value
        self.prev: Optional["DoublyListNode"] = None
        self.next: Optional["DoublyListNode"] = None


class DoublyLinkedList:
    """A single doubly-linked list class"""

    def __init__(self) -> None:
        self.head: Optional[DoublyListNode] = None
        self.tail: Optional[DoublyListNode] = None

    def add(self, value: str) -> None:
        new_node = DoublyListNode(value)
        if not self.head:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

    def delete(self, value: str) -> bool:
        current = self.head
        while current:
            if current.value == value:
                if current.prev:
                    current.prev.next = current.next
                if current.next:
                    current.next.prev = current.prev
                if current == self.head:
                    self.head = current.next
                if current.tail == self.tail:
                    self.tail = current.prev

                return True

        return False

    def display(self) -> list[Any]:
        elements = []

        current = self.head
        while current:
            elements.append(current.value)
            current = current.next

        return elements

    def search(self, value: str) -> bool:
        current = self.head
        while current:
            if current.value == value:
                return True
            current = current.next

        return False

    def replace(self, old_value: str, new_value: str) -> bool:
        current = self.head
        while current:
            if current.value == old_value:
                current.value = new_value
                return True
            current = current.next

        return False


def user_interaction() -> None:
    dll = DoublyLinkedList()

    while True:
        print(
            "\nMenu:\n"
            "1. Add element to the list.\n"
            "2. Delete element from the list.\n"
            "3. Show the contents of the list.\n"
            "4. Check if a value is in the list.\n"
            "5. Replace a value in the list.\n"
            "6. Exit."
        )
        choice = input("Choose an option: ")

        match choice:
            case "1":
                value = input("Enter the value to add: ")
                dll.add(value)
            case "2":
                value = input("Enter the value to delete: ")
                if dll.delete(value):
                    print("Value deleted from the list.")
                else:
                    print("Value not found in the list.")
            case "3":
                print(f"List contents: {dll.display()}")
            case "4":
                value = input("Enter the value to check: ")
                if dll.search(value):
                    print("Value found in the list.")
                else:
                    print("Value not in the list.")
            case "5":
                target = input("Enter the value to replace: ")
                new_value = input("Enter the new value: ")
                if dll.replace(target, new_value):
                    print(f"Value '{target}' replaced with '{new_value}'.")
                else:
                    print("Value not found in the list.")
            case "6":
                print("Exiting the program.")
                break
            case _:
                print("Invalid option, please try again.")


if __name__ == "__main__":
    user_interaction()
