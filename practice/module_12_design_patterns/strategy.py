import unittest


class ArrayOperations:
    def __init__(self, strategy):
        self.strategy = strategy
        self.data = []

    def execute(self):
        return self.strategy.execute(self.data)


class DisplayStrategy:
    def execute(self, data):
        return "Displaying: " + str(data)


class ReverseStrategy:
    def execute(self, data):
        return "Reversed: " + str(data[::-1])


class FindMaxStrategy:
    def execute(self, data):
        return "Max: " + str(max(data))


class FindMinStrategy:
    def execute(self, data):
        return "Min: " + str(min(data))


class TestStrategyPattern(unittest.TestCase):
    def setUp(self):
        self.data = [3, 1, 4, 1, 5, 9, 2, 6, 5]

    def test_display_strategy(self):
        operations = ArrayOperations(DisplayStrategy())
        operations.data = self.data
        self.assertEqual(operations.execute(), "Displaying: [3, 1, 4, 1, 5, 9, 2, 6, 5]")

    def test_reverse_strategy(self):
        operations = ArrayOperations(ReverseStrategy())
        operations.data = self.data
        self.assertEqual(operations.execute(), "Reversed: [5, 6, 2, 9, 5, 1, 4, 1, 3]")

    def test_find_max_strategy(self):
        operations = ArrayOperations(FindMaxStrategy())
        operations.data = self.data
        self.assertEqual(operations.execute(), "Max: 9")

    def test_find_min_strategy(self):
        operations = ArrayOperations(FindMinStrategy())
        operations.data = self.data
        self.assertEqual(operations.execute(), "Min: 1")


if __name__ == "__main__":
    unittest.main()
