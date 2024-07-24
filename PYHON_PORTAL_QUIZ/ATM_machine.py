user_pin = input("\nEnter your pin: ")

if user_pin == "1234":
    print("\nWelcome to the ATM!")
    account_balance = 10000
    while True:
        print("\n1. Check Balance\n2. Deposit\n3. Withdraw\n4. Exit")
        choice = int(input("\nChoose an option: "))

        if choice == 1:
            print(f"\nYour current balance is: {account_balance}")
        elif choice == 2:
            deposit_amount = int(input("\nEnter the amount to deposit: "))
            account_balance += deposit_amount
            print(f"\nYour new balance is: {account_balance}")
        elif choice == 3:
            withdraw_amount = int(input("\nEnter the amount to withdraw: "))
            if withdraw_amount <= account_balance:
                account_balance -= withdraw_amount
                print(f"\nYour new balance is: {account_balance}")
            else:
                print(f"\nInsufficient funds to withdraw {withdraw_amount}.Your current balance is{account_balance}")
        elif choice == 4:
            print("\nThank you for using the ATM!")
            break