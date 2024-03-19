import model

bank = model.bankAccount

print("BANCO FSOCIETY")

def mainmenu():
    print("1. Ingresar a la cuenta")
    print("2. Crear usuario")
    print("3. Ver información de la cuenta")
    print("4. Salir")

    while True:
        opcion = int(input(">> "))
        if opcion == 1:
            enterTheAccount()
        elif opcion == 2:
            userCreation()
        elif opcion == 3:
            showInfoOption()
        else:
            print("Opcion invalida.")

        if opcion == 4:
            break

def enterTheAccount():
    print("1. Depositar dinero")
    print("2. Retirar dinero")
    print("3. Ver dinero disponible:")
    print("4. Regresar")   

    while True:
        mierda = int(input(">> "))
        if mierda == 1:
            amount = float(input("Cantidad a depositar: $"))
            bank.addMoney(amount)
        elif mierda == 2:
            amount = float(input("Cantidad a retirar: $"))
            bank.withdrawMoney(amount)
        elif mierda == 3:
            print(f"Dinero disponible: ${bank.currentBalance}")
        else: 
            print("Opcion invalida.")
        
        if mierda == 4:
            mainmenu()

def userCreation():
    print("CREACION DE UN NUEVO USUARIO")
    userName = input(("Nombre: "))
    userId = int(input("ID: "))
    accountNumber = int(input("Numero de cuenta bancaria: #"))
    currentBalance = float(input("Balance: $"))
    bank.newAccount(userName,userId,accountNumber,currentBalance)
    print("Usuario creado exitosamente.")

def showInfoOption():
    userId = int(input("Ingrese ID del usuario: "))
    bank.showUser(userId)
