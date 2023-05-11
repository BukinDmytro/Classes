#4

class Bank:
    def __init__(self,customer,balancee):
        self.customer = customer
        self.balancee = balancee
class BankAccount:
    def __init__(self,customers,balance):
        self.customers = customers
        self.balance = balance
    def get_total_balance(self,balancee,balance):
        a = balancee + balance
        return a

name0 = Bank("Dima" , 10000)
name1 = Bank("Max" , 1500)
name2 = Bank("Edik" , 2500)


print(f"Client: {name0.customer} , Balance : {name0.balancee} UAH")
print(f"Client: {name1.customer} , Balance : {name1.balancee} UAH")
print(f"Client: {name2.customer} , Balance : {name2.balancee} UAH")

name_new = BankAccount("Ronnie" , 500)
print(f"New client : {name_new.customers} , Balance : {name_new.balance} UAH")

print(f"Total balance of all clients : {name_new.get_total_balance(balancee = 14000 , balance = 500)} UAH")