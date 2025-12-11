#Creating a calculator using python...

print("\033[1;94m\n\n-------Python Calculator-------\n\n\033[0m")


#Operation Menu starts..
while True:

    # Checking if the two integers given are correct or if not then printing error all 
    # using try and except algorithms..
    try:

        #Asking user for two float inputs for operations.. 
        num1 = float(input("Enter the first number : "))
        num2 = float(input("Enter the second number : "))

    except ValueError:
        print("\033[91m\n Value Error! Invalid Input! \n Only numeric values are allowed...\n\033[0m")
        continue

    print("\033[1;38;5;214m\n\n-----Menu Options-----\033[0m")
    print("\033[93m 1. Addition \n 2. Subtraction \n 3. Multiplication \n 4. Division \n 5. Modulo \n 6. Exit the program \n\033[0m")

    while True:
        try:
            key = int(input("Enter the number for operation : "))
            if key not in [1, 2, 3, 4, 5, 6]:
                print("\033[91m Wrong Input! \n Try again !\n\033[0m")
                continue
            break
            
        except ValueError:
            print("\033[91m Wrong Input! \n Try again !\n\033[0m")


    #To check for the option to be correct..

    #Performing addition..
    if key == 1:
        print("\033[92mAddition : \033[0m", num1 + num2)
        print("\n")

    
    #Performing subtraction..
    elif key == 2:
        print("\033[92mSubtraction : \033[0m", num1 - num2)
        print("\n")
    
    #Performing multiplication..
    elif key == 3:
        print("\033[92mMultiplication : \033[0m", num1 * num2)
        print("\n")

    #Performing division..
    elif key == 4:

        #checking if denominator is not equals to 0..
        if num2 != 0:
            print("\033[92mDivision : \033[0m", num1 / num2)
            print("\n")
            
        #if it is equal, show error and ask to input another number inplace of second..
        else:
            print("\033[91mError! \n Number cannot be divided by zero\n\033[0m")

            while True:
                try:
                    num3 = float(input("Enter the second number again : "))

                    if num3 == 0:
                        print("\033[91m Error! \n Number cannot be divided by zero\n\033[0m")
                        continue

                    else:
                        print("\033[92mDivision : \033[0m", num1 / num3)
                        break
                     
                except ValueError:
                    print("\033[91m\n Value Error! Invalid Input! \n Only numeric values are allowed...\n\033[0m")            
            print("\n")

    #Performing modulo division..
    elif key == 5:

        #checking if denominator is not equals to 0..
        if num2 != 0:
            print("\033[92mModulo : \033[0m", num1 % num2)
            print("\n")
            
        #if it is equal, show error and ask to input another number inplace of second..
        else:
            print("\033[91m Error! \n Number cannot be divided by zero\n\033[0m")

            while True:
                try:
                    num3 = float(input("Enter the second number again : "))

                    if num3 == 0: 
                        print("\033[91m Error! \n Number cannot be divided by zero\n\033[0m")
                        continue
                
                    else:
                        print("\033[92mModulo : \033[0m", num1 % num3)
                        break
                    
                except ValueError:
                    print("\033[91m\n Value Error! Invalid Input! \n Only numeric values are allowed...\n\033[0m")
            print("\n") 

    #Exiting the program..
    elif key == 6:
        print("\033[1;96m\n\n-----Thank you for using Python Calculator-----\033[0m")
        break
