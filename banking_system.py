#Creating a banking system using python... 
print("\n\n-------Welcome to the Python State Bank-------\n\n") 

#function to convert numbers into indian number system..
def format_indian(number):
    # Convert to string with no formatting
    num_str = f"{number:.2f}"
    
    # Split into whole + decimal part
    if '.' in num_str:
        whole, decimal = num_str.split('.')

    else:
        whole, decimal = num_str, ""
    
    # Reverse the digits to place commas from right side
    rev = whole[::-1]
    
    # First group of 3 digits
    groups = [rev[:3]]
    
    # Then groups of 2 digits
    for i in range(3, len(rev), 2):
        groups.append(rev[i:i+2])
    
    # Join groups with commas and reverse back
    formatted = ",".join(groups)[::-1]
    
    # Add decimal part
    return f"{formatted}.{decimal}"

#Asking for the personal details..
user_name = input("Enter the user_name: ")
while  True:
    raw_balance = input("Enter the current balance: ")

    #to replace all commas and store float numbers
    try:
        balance = float(raw_balance.replace(",", ""))
        break

    #if number contains characters or negative numbers
    except ValueError:
        print("Invalid number. \n Please try again! ")
        
#Special menu buttons for user..
while True:
    print("\n-----Menu-----")
    print(" 1. Check balance \n 2. Deposit money \n 3. Withdraw money \n 4. Exit \n ")
    key = int(input("Choose the menu option by number: "))

    #To access the menu buttons..

    #for key = 1, printing the current balance..
    if key == 1:
        print(format_indian(balance))

    #for key = 2, taking input of the amount to be deposited in the account..
    elif key == 2:

        while  True:
            raw_deposit = input("Enter the amount to be deposited: ")

            try:
                deposit_amount = float(raw_deposit.replace(",", ""))

                if deposit_amount > 0:
                    balance += deposit_amount
                    print(f"{format_indian(deposit_amount)} is to be deposited on your bank account.")
                    break

                else:
                    print("Amount must be positive.")
                break

            except ValueError:
                print("Invalid number. \n Please try again!")

    #for key = 3, taking input of the amount to be withdrawn by the user..
    elif key == 3:

        while  True:
            raw_withdraw = input("Enter the amount to be withdrawn: ")

            try:
                withdrawal_amount = float(raw_withdraw.replace(",", ""))

                if withdrawal_amount > 0:
                    if withdrawal_amount <= balance:     #amount is successfully withdrawn if there's sufficient balance in the account..
                        balance -= withdrawal_amount
                        print(f"{format_indian(withdrawal_amount)} is to be withdrawed from your bank account. \n")

                    elif withdrawal_amount >= balance:   #if not, then show not enough balance..
                        print("Not enough balance to withdraw.")

                    else:
                        print("Withdrawal is incorrect\n Try again \n ")    
                    break

                else:
                    print("Amount must be positive.")
                break

            except ValueError:
                print("Invalid number. \n Please try again!")
    
    #for kry = 4, exiting the program..
    elif key == 4:
        print("Thank you for using our bank!!")
        print("-----Exited from Python State Bank-----")
        break

    else: 
        print(f"{key} is Invalid \n Please try again!!")


