import unittest


class ListNode:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def add(self, value):
        new_node = ListNode(value)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def delete(self, value):
        if self.head and self.head.value == value:
            self.head = self.head.next
            return
        previous = self.head
        while previous and previous.next:
            if previous.next.value == value:
                previous.next = previous.next.next
                return
            previous = previous.next
        raise ValueError(f"Value {value} not found in the list.")

    def __str__(self):
        result = []
        current = self.head
        while current:
            result.append(str(current.value))
            current = current.next
        return " -> ".join(result)

    def search(self, value):
        current = self.head
        while current:
            if current.value == value:
                return True
            current = current.next
        return False

    def replace(self, old_value, new_value):
        current = self.head
        replaced = False
        while current:
            if current.value == old_value:
                current.value = new_value
                replaced = True
            current = current.next
        return replaced

    def user_interaction(self) -> None:
        # Initial input of numbers
        numbers = map(int, input("Enter numbers separated by space: ").split())
        for number in numbers:
            self.add(number)

        while True:
            print("\nMenu:")
            print("1. Add an element to the list.")
            print("2. Delete an element from the list.")
            print("3. Show the contents of the list.")
            print("4. Check if a value is in the list.")
            print("5. Replace a value in the list.")
            print("6. Exit.")

            choice = get_int_input("Choose an option: ")

            match choice:
                case 1:
                    value = get_int_input("Enter the value to add: ")
                    self.add(value)
                    print(f"{value} added to the list.")
                case 2:
                    value = get_int_input("Enter the value to delete: ")
                    try:
                        self.delete(value)
                        print(f"Value {value} deleted from the list.")
                    except ValueError as e:
                        print(e)
                case 3:
                    print("List contents: ", self)
                case 4:
                    value = get_int_input("Enter the value to check: ")
                    result = "Value found in the list." if self.search(value) else "Value not found in the list."
                    print(result)
                case 5:
                    old_value = get_int_input("Enter the value to replace: ")
                    new_value = get_int_input("Enter the new value: ")
                    if self.replace(old_value, new_value):
                        print(f"Value {old_value} replaced with {new_value}.")
                    else:
                        print("Value not found in the list.")
                case 6:
                    print("Exiting the program.")
                    break
                case _:
                    print("Invalid option, please try again.")


def get_int_input(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Please enter a valid integer.")


def main():
    linked_list = LinkedList()
    linked_list.user_interaction()


class TestLinkedList(unittest.TestCase):

    def test_add(self):
        linked_list = LinkedList()
        linked_list.add(1)
        self.assertEqual(str(linked_list), "1", "Failed to add element '1'")
        linked_list.add(2)
        self.assertEqual(str(linked_list), "1 -> 2", "Failed to add element '2'")

    def test_delete(self):
        linked_list = LinkedList()
        linked_list.add(1)
        linked_list.add(2)
        linked_list.delete(1)
        self.assertEqual(str(linked_list), "2", "Failed to delete element '1'")

    def test_search(self):
        linked_list = LinkedList()
        linked_list.add(1)
        linked_list.add(2)
        self.assertTrue(linked_list.search(1), "Search for '1' should return True")
        self.assertFalse(linked_list.search(3), "Search for '3' should return False")

    def test_replace(self):
        linked_list = LinkedList()
        linked_list.add(1)
        linked_list.add(2)
        linked_list.replace(1, 3)
        self.assertEqual(str(linked_list), "3 -> 2", "Failed to replace '1' with '3'")


if __name__ == "__main__":
    unittest.main()
