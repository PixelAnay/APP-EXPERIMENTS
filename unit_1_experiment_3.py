
class PaymentStrategy:
    def pay(self, amount):
        pass



class CreditCardPayment(PaymentStrategy):
    def pay(self, amount):
        print(f"Paid ₹{amount} using Credit Card")



class PayPalPayment(PaymentStrategy):
    def pay(self, amount):
        print(f"Paid ₹{amount} using PayPal")



class UPIPayment(PaymentStrategy):
    def pay(self, amount):
        print(f"Paid ₹{amount} using UPI")



class PaymentContext:
    def __init__(self, strategy):
        self.strategy = strategy

    def set_strategy(self, strategy):
        self.strategy = strategy

    def pay(self, amount):
        self.strategy.pay(amount)



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
