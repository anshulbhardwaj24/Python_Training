class Bank:
    # class variables
    no_of_Acc = 0
    int_rate = 0.03

    def __init__(self,name,balance):
        # instance variables
        self.name = name
        self.balance = balance
        Bank.no_of_Acc += 1

    def add(self,amount):
        self.balance += amount

    def reeduce(self,amount):
        self.balance -= amount

    # regular methods automatically pass the instance as first arg
    def pay(self,to,amount):
        to.add(amount)
        self.reeduce(amount)
        self.Pay_Interest(self,to,amount)

    def Pay_Interest(self,Sender,Reciver,amount):
        Sender.balance  += float(amount * self.int_rate)
        Reciver.balance += float(amount * self.int_rate)

    #it takes class as the first argument
    @classmethod
    def create_Acc_str(cls,Acc_str):
        name,balance = Acc_str.split('-')
        return cls(name,balance)
    
    #it dont pass the class or instance automatically
    @staticmethod
    def Date():
        pass

    # Getter i.e., where ever a value is changed and it we try to access these atribute of the user
    @property
    def nameBalance(self):
       return self.name + 'has' + str(self.balance)
    
    # Setter - to set the new name of user
    @nameBalance.setter
    def nameBalance(self,name):
        self.name = name

    # to delete name when ever nameBalance is deleted
    @nameBalance.deleter
    def nameBalance(self):
        self.name=''
        self.balance=0

    def CheckBalance(self):
        return '{} has {}'.format(self.name,self.balance)



class Current_Acc(Bank):
    int_rate = 0.01

    def __init__(self, name, balance,business):
        super().__init__(name, balance)
        self.Business = business

    # when ever the instance is printed like print(acc1.__repr__()) then this will run
    # it return the developer friendly string represtation of obj
    def __repr__(self):
        return "Current_Acc('{}',{},'{}')".format(self.name,self.balance,self.Business)

     # when ever the instance is printed like print(acc1.__str__()) or print(acc1) then this will run
    # it return the user friendly string represtation of obj
    def __str__(self):
        return "'{}' has {} with Business type of {}".format(self.name,self.balance,self.Business)

# Parent Class Opp
acc1 = Bank('Anshul',500)
acc2 = Bank('Vishwa',500)
        
acc1.pay(acc2,50)

print(acc1.CheckBalance())
print(acc2.CheckBalance())
print(Bank.no_of_Acc)

# Child Class Opp.
acc3 = Current_Acc('Tanishq',600,"textile")
acc4 = Current_Acc('Abhishek',600,"e-commerce")

acc3.pay(acc4,50)
print(acc3.CheckBalance())
print(acc4.CheckBalance())

# Magical method or dunders
print(acc3)

# 
print(isinstance(acc3,Current_Acc))
print(issubclass(Current_Acc,Bank))


# using getter
print(acc1.nameBalance)
acc1.nameBalance = "Rajat"
print(acc1.nameBalance)
print(acc1.name)
del acc1.nameBalance
print(acc1.nameBalance)
print(acc1.name)