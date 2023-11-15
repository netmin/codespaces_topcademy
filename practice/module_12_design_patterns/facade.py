import unittest


class SubsystemOne:
    def operation_one(self):
        return "Operation 1 from Subsystem One"


class SubsystemTwo:
    def operation_two(self):
        return "Operation 2 from Subsystem Two"


class Facade:
    def __init__(self):
        self.subsystem_one = SubsystemOne()
        self.subsystem_two = SubsystemTwo()

    def operation(self):
        return self.subsystem_one.operation_one() + ", " + self.subsystem_two.operation_two()


class TestFacadePattern(unittest.TestCase):
    def test_facade(self):
        facade = Facade()
        self.assertEqual(facade.operation(), "Operation 1 from Subsystem One, Operation 2 from Subsystem Two")


if __name__ == "__main__":
    unittest.main()
