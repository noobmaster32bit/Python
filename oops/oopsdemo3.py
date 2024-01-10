class Bank:
    ac_num:int
    name:str
    ac_type:str
    ifsc_code:str
    branch:str
    balance:int

    def create_account(self,ac_num,name,ac_type,ifsc_code,branch,balance):
        self.ac_num=ac_num
        self.name=name
        self.ac_type=ac_type
        self.ifsc_code=ifsc_code
        self.branch=branch
        self.balance=balance

    def deposit(self,amount):
        self.balance+=amount
        print("Your available balance is Rs.", self.balance)

    def withdraw(self,amount):
        if amount>self.balance:
            print("Insufficient balance")
        else:
            self.balance-=amount
            print(self.balance)

    def get_balance(self):
        print("Your remaining balance is :", self.balance)

account1=Bank()
account1.create_account(1234567 , "akshay", "Savings", "IDIB00K098", "Kakkanad", 0)
account1.deposit(2000)
account1.withdraw(500)
account1.get_balance()


