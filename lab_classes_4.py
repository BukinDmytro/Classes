#4 не доробив (

class BankAccount:
    def __init__(self, balance,owner):
        self.balance = balance
        self.owner = owner
        if self.balance < 0:
            print("Якась фігня,баланс не може бути мінусовим")
    def deposit(self):
        print(self.balance + 1000)
    def withdraw(self):
        print(self.balance - 500)

babki = BankAccount(2000 , "Dima")
babki.deposit() - babki.withdraw()