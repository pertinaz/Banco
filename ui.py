import model

bank = model.bankAccount

def menu():
    print("BANCO FSOCIETY")
    print()
    print("1. Ingresar a la cuenta")
    print("2. Crear usuario")
    print("3. Ver información de la cuenta")
    print("4. Salir")
    print()

def mainmenu():
    menu()
    while True:
        opcion = int(input(">> "))
        if opcion == 1:
            accountNumber = int(input("Ingrese su numero de cuenta: #"))
            if bank.accountValidation(accountNumber):
                enterTheAccount()
            menu()
        elif opcion == 2:
            userCreation()
            menu()
        elif opcion == 3:
            showInfoOption()
            menu()
        elif opcion == 4:
            break
        else:
            print()
            print("Opcion invalida.")
            menu()

def submenu():
    print()
    print("1. Depositar dinero")
    print("2. Retirar dinero")
    print("3. Ver dinero disponible")
    print("4. Regresar")   
    print()

#Pending
def enterTheAccount():
    submenu()
    while True:
        opcion = int(input(">> "))
        if opcion == 1:
            amount = float(input("Cantidad a depositar: $"))
            bank.addMoney(amount)
            submenu()
        elif opcion == 2:
            amount = float(input("Cantidad a retirar: $"))
            bank.withdrawMoney(amount)
            submenu()
        elif opcion == 3:
            print(f"Dinero disponible: ${bank.currentBalance}")
            submenu()
        elif opcion == 4:
            print()
            mainmenu() 
        else: 
            print("Opcion invalida.")
            submenu()
#

def userCreation():
    print("CREACION DE UN NUEVO USUARIO")
    userName = input(("Nombre: "))
    userId = int(input("ID: "))
    accountNumber = int(input("Numero de cuenta bancaria: #"))
    currentBalance = float(input("Balance: $"))
    bank.newAccount(userName,userId,accountNumber,currentBalance)
    print("Usuario creado exitosamente.")
    print()

def showInfoOption():
    userId = int(input("Ingrese ID del usuario: "))
    print()
    bank.showUser(userId)
    print()
