User = int(input("Enter a Pin "))
pin = 1234
Balance = 10000

if User == pin:
    print("\n1. Check balance \n2. Deposit \n3. Withdraw \n4. Exit")

    choice = int(input("Enter your choice "))

    match choice:
            case 1:
                print("Your Balance is:", Balance)
            case 2:
                a = int(input("Enter amount to deposit: "))
                Balance = Balance + a
                print("Deposit successful! Updated balance is:", Balance)
            case 3:
                b = int(input("Enter amount to withdraw: "))
                if Balance < b:
                    print("Insufficient balance")
                else:
                    Balance = Balance - b
                    print("Withdrawal successful! Upadted balance is:", Balance)
            case 4:
                print("Thank you for using ATM. Goodbye!")
    
else:
    print("Incorrect PIN. Please try again.")
