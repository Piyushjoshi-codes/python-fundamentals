#Creating a calculator using python...

print("\n\n-------Python Calculator-------\n\n")


#Operation Menu starts..
while True:

    # Checking if the two integers given are correct or if not then printing error all 
    # using try and except algorithms..
    try:

        #Asking user for two float inputs for operations.. 
        num1 = float(input("Enter the first number : "))
        num2 = float(input("Enter the second number : "))

    except ValueError:
        print(" \n Value Error! Invalid Input! \n Only integers are allowed...\n")
        continue

    print("\n\n-----Menu Options-----")
    print(" 1. Addition \n 2. Subtraction \n 3. Multiplication \n 4. Division \n 5. Modulo \n 6. Exit the program \n")

    while True:
        try:
            key = int(input("Enter the number for operation : "))
            if key not in [1, 2, 3, 4, 5, 6]:
                print(" Wrong Input! \n Try again !\n")
                continue
            break
            
        except ValueError:
            print(" Wrong Input! \n Try again !\n")


    #To check for the option to be correct..

    #Performing addition..
    if key == 1:
        print("Addition : ", num1 + num2)
        print("\n")

    
    #Performing subtraction..
    elif key == 2:
        print("Subtraction : ", num1 - num2)
        print("\n")
    
    #Performing multiplication..
    elif key == 3:
        print("Multiplication : ", num1 * num2)
        print("\n")

    #Performing division..
    elif key == 4:

        #checking if denominator is not equals to 0..
        if num2 != 0:
            print("Division : ", num1 / num2)
            print("\n")
            
        #if it is equal, show error and ask to input another number inplace of second..
        else:
            print(" Error! \n Number cannot be divided by zero\n")

            while True:
                try:
                    num3 = float(input("Enter the second number again : "))

                    if num3 == 0:
                        print(" Error! \n Number cannot be divided by zero\n")
                        continue

                    else:
                        print("Division : ", num1 / num3)
                        break
                    
                except ValueError:
                    print(" \n Value Error! Invalid Input! \n Only integers are allowed...")
            
            print("\n")

    #Performing modulo division..
    elif key == 5:

        #checking if denominator is not equals to 0..
        if num2 != 0:
            print("Modulo : ", num1 % num2)
            print("\n")
            
        #if it is equal, show error and ask to input another number inplace of second..
        else:
            print("Error! \n Number cannot be divided by zero\n")

            while True:
                try:
                    num3 = float(input("Enter the second number again : "))

                    if num3 == 0: 
                        print(" Error! \n Number cannot be divided by zero\n")
                        continue
                
                    else:
                        print("Modulo : ", num1 % num3)
                        break
                    
                except ValueError:
                    print(" \n Value Error! Invalid Input! \n Only integers are allowed...")

            print("\n") 

    #Exiting the program..
    elif key == 6:
        print("\n\n-----Thank you for using Python Calculator-----")
        break

    #If input does'nt matches the following standards, it will pass the Error for Wrong Input..
    else: 
        print(" Wrong Input \n Try again !")
        print("\n")
