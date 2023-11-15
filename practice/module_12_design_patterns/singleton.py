class Singleton:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Singleton, cls).__new__(cls)

        return cls._instance


def test_singleton_identify():
    singleton1 = Singleton()
    singleton2 = Singleton()

    assert singleton1 is singleton2, "Singleton instances are not the same"


def test_singleton_state():
    singleton1 = Singleton()
    singleton1.data = "Singleton data"
    singleton2 = Singleton()

    assert singleton2.data == "Singleton data", "Singleton state is not share"


test_singleton_identify()
test_singleton_state()
