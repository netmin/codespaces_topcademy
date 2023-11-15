import unittest


class OldSystem:
    def specific_request(self):
        return "Old system functionality"


class Adapter:
    def __init__(self, old_system):
        self.old_system = old_system

    def request(self):
        return self.old_system.specific_request()


class TestAdapterPattern(unittest.TestCase):
    def test_adapter(self):
        old_system = OldSystem()
        adapter = Adapter(old_system)
        self.assertEqual(adapter.request(), "Old system functionality")


if __name__ == "__main__":
    unittest.main()
