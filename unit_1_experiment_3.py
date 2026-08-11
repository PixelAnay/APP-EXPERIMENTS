# Strategy Pattern - Configurable Payment Processing System

# Strategy Interface
class PaymentStrategy:
    def pay(self, amount):
        pass


# Concrete Strategy 1
class CreditCardPayment(PaymentStrategy):
    def pay(self, amount):
        print(f"Paid ₹{amount} using Credit Card")


# Concrete Strategy 2
class PayPalPayment(PaymentStrategy):
    def pay(self, amount):
        print(f"Paid ₹{amount} using PayPal")


# Concrete Strategy 3
class UPIPayment(PaymentStrategy):
    def pay(self, amount):
        print(f"Paid ₹{amount} using UPI")


# Context Class
class PaymentContext:
    def __init__(self, strategy):
        self.strategy = strategy

    def set_strategy(self, strategy):
        self.strategy = strategy

    def pay(self, amount):
        self.strategy.pay(amount)


# Main Program
print("Payment Methods")
print("1. Credit Card")
print("2. PayPal")
print("3. UPI")

choice = int(input("Enter your choice: "))
amount = float(input("Enter payment amount: ₹"))

if choice == 1:
    strategy = CreditCardPayment()
elif choice == 2:
    strategy = PayPalPayment()
elif choice == 3:
    strategy = UPIPayment()
else:
    print("Invalid Choice!")
    exit()

payment = PaymentContext(strategy)
payment.pay(amount)
