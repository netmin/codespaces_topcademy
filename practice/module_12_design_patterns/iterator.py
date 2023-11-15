import unittest


class Student:
    def __init__(self, name):
        self.name = name


class Group:
    def __init__(self, students):
        self.students = students

    def __iter__(self):
        self._index = 0
        return self

    def __next__(self):
        if self._index < len(self.students):
            result = self.students[self._index]
            self._index += 1
            return result
        raise StopIteration


class TestIteratorPattern(unittest.TestCase):
    def test_iterator(self):
        group = Group([Student("Alice"), Student("Bob"), Student("Charlie")])
        students = [student.name for student in group]
        self.assertEqual(students, ["Alice", "Bob", "Charlie"])


if __name__ == "__main__":
    unittest.main()
