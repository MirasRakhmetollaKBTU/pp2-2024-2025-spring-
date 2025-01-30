class Accaunt:
    def __init__(self, owner, balance = 0):
        self.owner  = owner
        self.balance = balance
    def deposit(self, cash):
        self.balance += cash
        return self.balance
    def info(self):
        print(f"{self.owner} : {self.balance}")
    def withdraw(self, minus):
        if minus <= self.balance:
            self.balance -= minus
            return f"{self.owner} : {self.balance}"
        else:
            return f"{self.owner} has not enough money. Your balance : {self.balance}, you still need {minus - self.balance}"


person1 = Accaunt("Bogach", 9999999)
person2 = Accaunt("Nebogach")
person3 = Accaunt("Sredny", 100)

person1.deposit(1000)
person2.deposit(100)
person3.deposit(500)

person1.info()
person2.info()
person3.info()

print(person1.withdraw(1999))
print(person2.withdraw(5000))
print(person3.withdraw(600))

person1.info()
person2.info()
person3.info()
