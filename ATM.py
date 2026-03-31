User = int(input("Enter a Pin "))
pin = 1234
Balance = 100000.00

if User == pin:
    print("\n1. Check balance \n2. Deposit \n3. Withdraw \n4. Exit")

    choice = int(input("Enter your choice "))

    match choice:
            case 1:
                print(f"Your Balance is: ₹{Balance:,.2f}")
            case 2:
                a = float(input("Enter amount to deposit: "))
                Balance = Balance + a
                print(f"Deposit successful! Updated balance is: ₹{Balance:,.2f}")
            case 3:
                b = float(input("Enter amount to withdraw: "))
                if Balance < b:
                    print("Insufficient balance")
                else:
                    Balance = Balance - b
                    print(f"Withdrawal successful! Updated balance is: ₹{Balance:,.2f}")
            case 4:
                print("Thank you for using ATM. Goodbye!")
    
else:
    print("Incorrect PIN. Please try again.")

