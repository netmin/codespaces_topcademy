class Computer:
    def __init__(self):
        self.components = {}

    def add_component(self, key, value):
        self.components[key] = value

    def __str__(self):
        return f"Computer with components: {self.components}"


class ComputerBuilder:
    def __init__(self):
        self.computer = Computer()

    def configure_processor(self, processor):
        self.computer.add_component("processor", processor)
        return self

    def configure_ram(self, ram):
        self.computer.add_component("ram", ram)
        return self

    def configure_graphics_card(self, graphics_card):
        self.computer.add_component("graphics_card", graphics_card)
        return self

    def build(self):
        return self.computer


builder = ComputerBuilder()
computer = (builder
            .configure_processor("Intel Core i7")
            .configure_ram("16GB")
            .configure_graphics_card("NVIDIA GTX 3080")
            .build())
