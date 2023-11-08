class Stack:
    def __init__(self, size: int) -> None:
        self.size = size
        self.stack: list[int] = []

    def push(self, value: int) -> None:
        if not self.is_full():
            self.stack.append(value)
        else:
            print("Stack is full. Cannot push another value.")

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

    def is_full(self) -> bool:
        return len(self.stack) == self.size

    def clear(self) -> None:
        self.stack = []

    def peek(self) -> int | None:
        if not self.is_empty():
            return self.stack[-1]
        else:
            print("Stack is empty. Nothing to peek.")
            return None


def user_interaction() -> None:
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
                if stack.is_full():
                    print("Stack is already full.")
                else:
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
                print(
                    "The stack is full."
                    if stack.is_full()
                    else "The stack is not full."
                )
            case "6":
                stack.clear()
                print("The stack has been cleared.")
            case "7":
                value = stack.peek()
                if value is not None:
                    print(f"The top value of the stack is {value}.")
            case "8":
                print("Exiting the program.")
                break
            case _:
                print("Invalid option, please try again.")


if __name__ == "__main__":
    user_interaction()
