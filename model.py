class bankAccount:
    def __init__(self, accountNumber,userId,userName,currentBalance):
        self.accountNumber = accountNumber
        self.userId= userId
        self.userName = userName
        self.currentBalance = currentBalance

    def newAccount(accountList,userName,userId,accountNumber,currentBalance):    
        for account in accountList:
            if userId == account.userId:
                print("Usuario ya registrado...")
                return
        accountList.append(bankAccount(accountNumber,userId,userName,currentBalance))
      
    def ListOfAccounts(accountList):
        for account in accountList:
            print(f"Name: {account.userName}")
            print(f"ID: {account.userId}")
            print(f"Account Number: #{account.accountNumber}")
            print(f"Balance: ${account.currentBalance}")
            print()

    def showUser(accountList,userId):
        for account in accountList:
            if userId == account.userId:
                print(f"Name: {account.userName}")
                print(f"ID: {account.userId}")
                print(f"Account Number: #{account.accountNumber}")
                print(f"Balance: ${account.currentBalance}")
                return
            print("Usuario no encontrado.")
          
    def addMoney(self,amount):
        self.currentBalance += amount
        print(f"Nuevo saldo: ${self.currentBalance}")
    
    
    def withdrawMoney(self,amount):
        if amount > self.currentBalance:
            print("No hay fondos suficientes")
        else:
            self.currentBalance -= amount
            print(f"Nuevo saldo: ${self.currentBalance}")
