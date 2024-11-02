# # Abstraction, Encapsulation
# # Abstraction
# class car:
#     def __init__(self):
#         self.acc= False
#         self.brk=False
#         self.clutch= False
#     def start(self):
#         self.acc= True
#         self.clutch= True
#         print("Starting....")
# car1= car()
# car1.start()

# practice problem 2
class account:
    def __init__(self, bal,acc):
        self.balance= bal
        self.Account_no=acc
    # Debit
    def debit(self,amount):
        self.balance-=amount
        print("tk.", amount, "is deducted")
        print("Total Balance: ",self.get_bal())
    # Credit
    def credit(self,amount):
        self.balance+=amount
        print("tk", amount, "is added")
        print("Total Balance: ",self.get_bal())
    def get_bal(self):
        return self.balance
customer1=account(10000, 12131)
print(customer1.balance, customer1.Account_no)
customer1.debit(3232)
customer1.credit(3232)
customer1.credit(3232)
