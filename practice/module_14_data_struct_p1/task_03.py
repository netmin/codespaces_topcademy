import unittest
from collections import deque


class Stack:
    def __init__(self, size: int):
        self.size = size
        self.stack = deque([], maxlen=size)

    def push(self, value: int):
        if self.is_full():
            raise OverflowError("Stack is full. Cannot push another value.")
        self.stack.append(value)

    def pop(self) -> int:
        if self.is_empty():
            raise IndexError("Stack is empty. Cannot pop a value.")
        return self.stack.pop()

    def count(self) -> int:
        return len(self.stack)

    def is_empty(self) -> bool:
        return len(self.stack) == 0

    def is_full(self) -> bool:
        return len(self.stack) == self.size

    def clear(self):
        self.stack.clear()

    def peek(self) -> int:
        if self.is_empty():
            raise IndexError("Stack is empty. Nothing to peek.")
        return self.stack[-1]


def user_interaction():
    stack_size = int(input("Enter the fixed size for the stack: "))
    stack = Stack(stack_size)

    while True:
        print("\nMenu:")
        print("1. Push a value to the stack.")
        print("2. Pop a value from the stack.")
        print("3. Count the values in the stack.")
        print("4. Check if the stack is empty.")
        print("5. Check if the stack is full.")
        print("6. Clear the stack.")
        print("7. Peek the top value of the stack.")
        print("8. Exit.")
        choice = input("Choose an option: ")

        match choice:
            case "1":
                value = int(input("Enter an integer value to push: "))
                try:
                    stack.push(value)
                    print(f"Value {value} pushed to the stack.")
                except OverflowError as oe:
                    print(oe)
            case "2":
                try:
                    value = stack.pop()
                    print(f"Value {value} popped from the stack.")
                except IndexError as ie:
                    print(ie)
            case "3":
                print(f"The stack contains {stack.count()} values.")
            case "4":
                print(
                    "The stack is empty."
                    if stack.is_empty()
                    else "The stack is not empty."
                )
            case "5":
                print(
                    "The stack is full."
                    if stack.is_full()
                    else "The stack is not full."
                )
            case "6":
                stack.clear()
                print("The stack has been cleared.")
            case "7":
                try:
                    value = stack.peek()
                    print(f"The top value of the stack is {value}.")
                except IndexError as ie:
                    print(ie)
            case "8":
                print("Exiting the program.")
                break
            case _:
                print("Invalid option, please try again.")


class TestStack(unittest.TestCase):

    def test_push(self):
        stack = Stack(2)
        stack.push(1)
        self.assertEqual(stack.peek(), 1, "Failed to push element '1'")
        stack.push(2)
        self.assertEqual(stack.peek(), 2, "Failed to push element '2'")
        with self.assertRaises(OverflowError):
            stack.push(3)

    def test_pop(self):
        stack = Stack(2)
        stack.push(1)
        stack.push(2)
        self.assertEqual(stack.pop(), 2, "Failed to pop the top element")
        self.assertEqual(stack.pop(), 1, "Failed to pop the second element")
        with self.assertRaises(IndexError):
            stack.pop()

    def test_count(self):
        stack = Stack(3)
        stack.push(1)
        stack.push(2)
        self.assertEqual(stack.count(), 2, "Count should be 2")

    def test_is_empty(self):
        stack = Stack(1)
        self.assertTrue(stack.is_empty(), "Stack should be empty")
        stack.push(1)
        self.assertFalse(stack.is_empty(), "Stack should not be empty")

    def test_is_full(self):
        stack = Stack(1)
        self.assertFalse(stack.is_full(), "Stack should not be full")
        stack.push(1)
        self.assertTrue(stack.is_full(), "Stack should be full")

    def test_clear(self):
        stack = Stack(2)
        stack.push(1)
        stack.push(2)
        stack.clear()
        self.assertTrue(stack.is_empty(), "Stack should be empty after clearing")

    def test_peek(self):
        stack = Stack(1)
        stack.push(1)
        self.assertEqual(stack.peek(), 1, "Failed to peek the top element")
        stack.clear()
        with self.assertRaises(IndexError):
            stack.peek()


if __name__ == '__main__':
    unittest.main()
