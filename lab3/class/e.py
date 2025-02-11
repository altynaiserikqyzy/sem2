<<<<<<< HEAD
class student:
    def __init__(self , name , age , faculty , score):
        self.name = name 
        self.age=age
        self.faculty=faculty
        self.score=score

    def passes(self):
        if self.score>50:
            print(f"Yes, {self.name} passes")
        else:
            print(f"No , {self.name} fails")
a = student("Altynai" , 18 , "FIT" , 70)
=======
class Account:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount}. New balance is {self.balance}.")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds.")
        else:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance is {self.balance}.")
account = Account("Alice", 100)
account.deposit(50)
account.withdraw(30)
account.withdraw(150)
>>>>>>> a979e87046c09c4d49cb61b9b82907516e898946
