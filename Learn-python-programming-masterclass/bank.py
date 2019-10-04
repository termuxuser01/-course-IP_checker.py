from datetime import datetime

class Account:
    
    @staticmethod
    def _get_time():
        """static method that returns time to other methods"""
        return datetime.now().strftime("%m/%d/%Y %X")
    def __init__(self, name, balance):
        self.holder = name
        self.balance = balance
        self.transactions = []
        if input("is this a savings account? y/n\n").lower() == "y":

            self.savings = True
        else:
            self.savings = False

    def show_balance(self):
        print(f"your balance is: {self.balance}")

    def success_msg(self):
        print("operation successful",
        f"mew balamce is {self.balance}")


    def widraw(self):
        w = int(input("how much do you wish to widraw? "))
        if w < self.balance:
            self.balance -= w
            self.success_msg()    
            self.transactions.append((-w, Account._get_time()))
        else: 
            print("insufficient funds")
    
    def deposit(self):
        amount = int(input("enter amount to deposit: "))
        self.balance += amount
        self.success_msg()
        self.transactions.append((amount, Account._get_time()))

    def show_trans(self):
        for a,d in self.transactions:
            if a < 0:
                t = "widrawl"
            else:
                t = "deposit"
            print("transaction: {}\namount: {}\ndate: {}".format(t, a,d))


if __name__ == "__main__":
    m = Account("victor richi", 500)

    m.deposit()
    m.widraw()
    m.show_trans()