import unittest
from typing import Any, Optional


class DoublyListNode:
    """A node for use in a doubly_linked list."""

    def __init__(self, value: str) -> None:
        self.value: Any = value
        self.prev: Optional["DoublyListNode"] = None
        self.next: Optional["DoublyListNode"] = None


class DoublyLinkedList:
    """A doubly-linked list class"""

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
                if current == self.tail:
                    self.tail = current.prev
                return True

            current = current.next

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
            "4. Search for a value in the list.\n"
            "5. Replace a value in the list.\n"
            "6. Exit."
        )

        try:
            choice = input("Choose an option: ")
            choice = int(choice)
            if choice < 1 or choice > 6:
                raise ValueError

            if choice == 1:
                value = input("Enter the value to add: ")
                dll.add(value)
            elif choice == 2:
                value = input("Enter the value to delete: ")
                if dll.delete(value):
                    print("Value deleted from the list.")
                else:
                    print("Value not found in the list.")
            elif choice == 3:
                print(f"List contents: {dll.display()}")
            elif choice == 4:
                value = input("Enter the value to search: ")
                if dll.search(value):
                    print("Value found in the list.")
                else:
                    print("Value not in the list.")
            elif choice == 5:
                target = input("Enter the value to replace: ")
                new_value = input("Enter the new value: ")
                if dll.replace(target, new_value):
                    print(f"Value '{target}' replaced with '{new_value}'.")
                else:
                    print("Value not found in the list.")
            elif choice == 6:
                print("Exiting the program.")
                break
        except ValueError:
            print("Invalid option, please enter a number between 1 and 6.")


class TestDoublyLinkedList(unittest.TestCase):

    def test_add(self):
        dll = DoublyLinkedList()
        dll.add("a")
        self.assertEqual(dll.display(), ["a"], "Failed to add element 'a'")
        dll.add("b")
        self.assertEqual(dll.display(), ["a", "b"], "Failed to add element 'b'")

    def test_delete(self):
        dll = DoublyLinkedList()
        dll.add("a")
        dll.add("b")
        result = dll.delete("a")
        self.assertTrue(result, "Failed to delete element 'a'")
        self.assertEqual(dll.display(), ["b"], "List should contain only 'b'")

    def test_search(self):
        dll = DoublyLinkedList()
        dll.add("a")
        dll.add("b")
        self.assertTrue(dll.search("a"), "Element 'a' should be found")
        self.assertFalse(dll.search("c"), "Element 'c' should not be found")

    def test_replace(self):
        dll = DoublyLinkedList()
        dll.add("a")
        dll.add("b")
        result = dll.replace("a", "c")
        self.assertTrue(result, "Failed to replace 'a' with 'c'")
        self.assertEqual(dll.display(), ["c", "b"], "Element 'a' should be replaced with 'c'")


if __name__ == '__main__':
    unittest.main()
