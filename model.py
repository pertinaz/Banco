class bankAccount:
    accountList = []
    def __init__(self, accountNumber,userId,userName,currentBalance):
        self.accountNumber = accountNumber
        self.userId= userId
        self.userName = userName
        self.currentBalance = currentBalance

        bankAccount.accountList.append(self)

    @classmethod
    def newAccount(cls,userName,userId,accountNumber,currentBalance):    
        for account in cls.accountList:
            if userId == account.userId:
                print("Usuario ya registrado...")
                return
        cls.accountList.append(bankAccount(accountNumber,userId,userName,currentBalance))
                
    @classmethod
    def ListOfAccounts(cls):
        for account in cls.accountList:
            print(f"Name: {account.userName}")
            print(f"ID: {account.userId}")
            print(f"Account Number: #{account.accountNumber}")
            print(f"Balance: ${account.currentBalance}")
            print()

    @classmethod
    def showUser(cls,userId):
        for account in cls.accountList:
            if userId == account.userId:
                print(f"Name: {account.userName}")
                print(f"ID: {account.userId}")
                print(f"Account Number: #{account.accountNumber}")
                print(f"Balance: ${account.currentBalance}")
                return
            print("Usuario no encontrado.")


    # METODOS PRIVAODS
    @classmethod        
    def accountValidation(cls,accountNumber):
        if not cls.accountList:
            print("No se encuentra la información.")
        else:
            accountFound = False
            for account in cls.accountList:   
                if accountNumber == account.accountNumber:
                    print(f"Bienvenido {account.userName}")
                    accountFound = True
            if not accountFound:
                print("Numero de cuenta incorrecto.") 
                    

    def addMoney(self,amount):
        self.currentBalance += amount
        print(f"Nuevo saldo: ${self.currentBalance}")
    

    def withdrawMoney(self,amount):
        if amount > self.currentBalance:
            print("No hay fondos suficientes")
        else:
            self.currentBalance -= amount
            print(f"Nuevo saldo: ${self.currentBalance}")
