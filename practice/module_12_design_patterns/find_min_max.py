class Logger:
    _instance = None

    def __new__(cls, output_type="screen"):
        if cls._instance is None:
            cls._instance = super(Logger, cls).__new__(cls)
            cls._output_type = output_type
        return cls._instance

    def log(self, message):
        if self._output_type == "file":
            with open("log.txt", "a") as file:
                file.write(message + "\n")
        else:
            print(message)


def read_numbers():
    numbers = input("Enter numbers separated by space: ")
    return list(map(int, numbers.split()))


def save_numbers(numbers, file_path):
    with open(file_path, "w") as file:
        for number in numbers:
            file.write(f"{number}\n")


def find_min_max(numbers):
    return min(numbers), max(numbers)


def main():
    logger = Logger(output_type="screen")  # or "file" for logging to a file
    numbers = read_numbers()
    file_path = input("Enter file path to save: ")

    logger.log(f"Numbers: {numbers}")
    save_numbers(numbers, file_path)
    logger.log(f"Numbers saved to file {file_path}")

    min_num, max_num = find_min_max(numbers)
    logger.log(f"Minimum number: {min_num}, Maximum number: {max_num}")

    # Additionally, save the min and max number to the file
    with open(file_path, "a") as file:
        file.write(f"Minimum number: {min_num}, Maximum number: {max_num}")


main()
