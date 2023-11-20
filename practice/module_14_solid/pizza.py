class Pizza:
    def __init__(self, name):
        self.name = name
        self.toppings = []

    def add_topping(self, topping):
        self.toppings.append(topping)

    def get_description(self):
        toppings_description = ', '.join(self.toppings) if self.toppings else 'without toppings'
        return f"Pizza '{self.name}' with toppings: {toppings_description}"


class Order:
    def __init__(self):
        self.pizzas = []
        self.status = "In Progress"

    def add_pizza(self, pizza):
        self.pizzas.append(pizza)

    def calculate_total(self):
        # More complex logic for calculating cost can be added here
        return 100 * len(self.pizzas)

    def complete_order(self):
        self.status = "Completed"
        return f"Order completed. Total cost: {self.calculate_total()} rub."


class Payment:
    @staticmethod
    def process_payment(amount):
        print(f"Payment of {amount} rub. successfully processed.")


class Report:
    @staticmethod
    def generate_sales_report(orders):
        total_sales = sum(order.calculate_total() for order in orders)
        print(f"Total sales volume: {total_sales} rub.")


# Creating pizzas
margherita = Pizza("Margherita")
margherita.add_topping("Mozzarella")
margherita.add_topping("Tomatoes")

pepperoni = Pizza("Pepperoni")
pepperoni.add_topping("Pepperoni")
pepperoni.add_topping("Mozzarella")

# Creating an order
order = Order()
order.add_pizza(margherita)
order.add_pizza(pepperoni)

# Payment process
Payment.process_payment(order.calculate_total())

# Completing the order
print(order.complete_order())

# Generating a report
Report.generate_sales_report([order])
