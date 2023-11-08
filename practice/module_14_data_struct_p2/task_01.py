class Queue:
    def __init__(self, limit=None):
        self.queue = []
        self.limit = limit

    def is_empty(self) -> bool:
        return len(self.queue) == 0

    def is_full(self) -> bool:
        if self.limit:
            return len(self.queue) == self.limit

        return False

    def enqueue(self, item: str) -> None:
        if self.limit and self.is_full():
            print("Queue is full. Cannot add more items")
        else:
            self.queue.append(item)

    def dequeue(self) -> str | None:
        if self.is_empty():
            print("Queue is empty. Cannot dequeue an item.")
            return None
        else:
            self.queue.pop(0)

    def show(self) -> None:
        if self.is_empty():
            print("Queue is empty.")
        else:
            print("Queue items: " + " ".join(self.queue))


def user_interaction() -> None:
    queue_limit = input(
        "Enter the maximum number of items in the queue (press enter for no limit): "
    )
    queue_limit = int(queue_limit) if queue_limit.isdigit() else None
    queue = Queue(limit=queue_limit)

    while True:
        print("\nMenu:")
        print("1. Check if the queue is empty.")
        print("2. Check if the queue is full.")
        print("3. Add an item to the queue.")
        print("4. Remove an item from the queue.")
        print("5. Show all items in the queue.")
        print("6. Exit.")
        choice = input("Choose an option: ")

        match choice:
            case "1":
                print(
                    "The queue is empty."
                    if queue.is_empty()
                    else "The queue is not empty."
                )
            case "2":
                print(
                    "The queue is full."
                    if queue.is_full()
                    else "The queue is not full."
                )
            case "3":
                item = input("Enter the item to add to the queue: ")
                queue.enqueue(item)
                print(f"Item '{item}' added to the queue.")
            case "4":
                item = queue.dequeue()
                if item is not None:
                    print(f"Item '{item}' removed from the queue.")
            case "5":
                queue.show()
            case "6":
                print("Exiting the program.")
                break
            case _:
                print("Invalid option, please try again.")


if __name__ == "__main__":
    user_interaction()
