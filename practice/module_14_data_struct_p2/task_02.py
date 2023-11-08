# priority_queue.py


class PriorityQueue:
    def __init__(self, limit=None):
        self.queue = []  # Elements will be tuples of the form (priority, item)
        self.limit = limit

    def is_empty(self) -> bool:
        return len(self.queue) == 0

    def is_full(self) -> bool:
        if self.limit:
            return len(self.queue) == self.limit
        return False  # No limit means never full

    def insert_with_priority(self, item: str, priority: int) -> None:
        if self.limit and self.is_full():
            print("Priority Queue is full. Cannot add more items.")
        else:
            self.queue.append((priority, item))
            self.queue.sort(reverse=True)  # Highest priority first

    def pull_highest_priority_element(self) -> str | None:
        if self.is_empty():
            print("Priority Queue is empty. Cannot pull an item.")
            return None
        return self.queue.pop(0)[1]  # Return item only

    def peek(self) -> str | None:
        if self.is_empty():
            print("Priority Queue is empty. Nothing to peek.")
            return None
        return self.queue[0][1]  # Return item only

    def show(self) -> None:
        if self.is_empty():
            print("Priority Queue is empty.")
        else:
            print("Priority Queue items:")
            for priority, item in self.queue:
                print(f"Item: {item}, Priority: {priority}")


def user_interaction() -> None:
    queue_limit = input(
        "Enter the maximum number of items in the priority queue (press enter for no limit): "
    )
    queue_limit = int(queue_limit) if queue_limit.isdigit() else None
    priority_queue = PriorityQueue(limit=queue_limit)

    while True:
        print("\nMenu:")
        print("1. Check if the priority queue is empty.")
        print("2. Check if the priority queue is full.")
        print("3. Add an item with priority to the priority queue.")
        print("4. Remove the highest priority item from the priority queue.")
        print("5. Peek at the highest priority item.")
        print("6. Show all items in the priority queue.")
        print("7. Exit.")
        choice = input("Choose an option: ")

        match choice:
            case "1":
                print(
                    "The priority queue is empty."
                    if priority_queue.is_empty()
                    else "The priority queue is not empty."
                )
            case "2":
                print(
                    "The priority queue is full."
                    if priority_queue.is_full()
                    else "The priority queue is not full."
                )
            case "3":
                item = input("Enter the item to add to the priority queue: ")
                priority = int(input("Enter the priority of the item (integer): "))
                priority_queue.insert_with_priority(item, priority)
                print(
                    f"Item '{item}' with priority {priority} added to the priority queue."
                )
            case "4":
                item = priority_queue.pull_highest_priority_element()
                if item is not None:
                    print(
                        f"Item '{item}' with the highest priority removed from the priority queue."
                    )
            case "5":
                item = priority_queue.peek()
                if item is not None:
                    print(f"The highest priority item is '{item}'.")
            case "6":
                priority_queue.show()
            case "7":
                print("Exiting the program.")
                break
            case _:
                print("Invalid option, please try again.")


if __name__ == "__main__":
    user_interaction()
