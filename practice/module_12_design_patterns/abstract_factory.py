class AbstractFactory:
    def create_product_a(self):
        raise NotImplemented


class ConcreteFactory(AbstractFactory):
    def create_product_a(self):
        return ProductA1()

    def create_product_b(self):
        return ProductB1()


class ProductA1:
    ...


class ProductB1:
    ...


def test_concrete_factory_creation():
    factory = ConcreteFactory()

    assert isinstance(factory, AbstractFactory), "ConcreteFactory is not an instance of AbstractFactory"


def test_product_creation_by_factory():
    factory = ConcreteFactory()

    product_a = factory.create_product_a()
    product_b = factory.create_product_b()

    assert isinstance(product_a, ProductA1), "ProductA is not created by ConcreteFactory"
    assert isinstance(product_b, ProductB1), "ProductB is not created by ConcreteFactory"


test_concrete_factory_creation()
test_product_creation_by_factory()
