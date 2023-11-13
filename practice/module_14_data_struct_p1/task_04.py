import unittest


class Stack:
    def __init__(self) -> None:
        self.stack: list[int] = []

    def push(self, value: int) -> None:
        self.stack.append(value)

    def pop(self) -> int | None:
        if not self.is_empty():
            return self.stack.pop()
        else:
            print("Stack is empty. Cannot pop a value.")
            return None

    def count(self) -> int:
        return len(self.stack)

    def is_empty(self) -> bool:
        return len(self.stack) == 0

    def clear(self) -> None:
        self.stack = []

    def peek(self) -> int | None:
        if not self.is_empty():
            return self.stack[-1]
        else:
            print("Stack is empty. Nothing to peek.")
            return None


def user_interaction() -> None:
    stack = Stack()
    menu_options = [
        "Push a value to the stack.",
        "Pop a value from the stack.",
        "Count the values in the stack.",
        "Check if the stack is empty.",
        "Clear the stack.",
        "Peek the top value of the stack.",
        "Exit."
    ]

    while True:
        print("\nMenu:")
        for i, option in enumerate(menu_options, start=1):
            print(f"{i}. {option}")

        choice = input("Choose an option: ")

        match choice:
            case "1":
                value = int(input("Enter an integer value to push: "))
                stack.push(value)
                print(f"Value {value} pushed to the stack.")
            case "2":
                value = stack.pop()
                if value is not None:
                    print(f"Value {value} popped from the stack.")
            case "3":
                print(f"The stack contains {stack.count()} values.")
            case "4":
                print(
                    "The stack is empty."
                    if stack.is_empty()
                    else "The stack is not empty."
                )
            case "5":
                stack.clear()
                print("The stack has been cleared.")
            case "6":
                value = stack.peek()
                if value is not None:
                    print(f"The top value of the stack is {value}.")
            case "7":
                print("Exiting the program.")
                break
            case _:
                print("Invalid option, please try again.")


class TestStack(unittest.TestCase):

    def test_push(self):
        stack = Stack()
        stack.push(1)
        self.assertEqual(stack.peek(), 1, "Failed to push element '1'")
        stack.push(2)
        self.assertEqual(stack.peek(), 2, "Failed to push element '2'")

    def test_pop(self):
        stack = Stack()
        stack.push(1)
        stack.push(2)
        self.assertEqual(stack.pop(), 2, "Failed to pop the top element")
        self.assertEqual(stack.pop(), 1, "Failed to pop the second element")
        self.assertIsNone(stack.pop(), "Popping from empty stack should return None")

    def test_count(self):
        stack = Stack()
        stack.push(1)
        stack.push(2)
        self.assertEqual(stack.count(), 2, "Count should be 2")

    def test_is_empty(self):
        stack = Stack()
        self.assertTrue(stack.is_empty(), "Stack should be empty")
        stack.push(1)
        self.assertFalse(stack.is_empty(), "Stack should not be empty")

    def test_clear(self):
        stack = Stack()
        stack.push(1)
        stack.push(2)
        stack.clear()
        self.assertTrue(stack.is_empty(), "Stack should be empty after clearing")

    def test_peek(self):
        stack = Stack()
        stack.push(1)
        self.assertEqual(stack.peek(), 1, "Failed to peek the top element")
        stack.clear()
        self.assertIsNone(stack.peek(), "Peeking from empty stack should return None")


if __name__ == '__main__':
    unittest.main()
