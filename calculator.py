#Creating a calculator using python...
\
#Asking user for two float inputs for operations.. 
print("\n\n-------Python Calculator-------\n\n")
num1 = float(input("Enter the first number : "))
num2 = float(input("Enter the second number : "))

#Operation Menu starts..
while True:
    print("-----Menu Options-----\n")
    print(" 1. Addition \n 2. Subtraction \n 3. Multiplication \n 4. Division \n 5. Modulo \n 6. Exit the program \n")
    key = int(input("Enter the number for operation : "))

    #To check for the option to be correct..

    #Performing addition..
    if key == 1:
        num3 = num1 + num2
        print("Addition : ", num3)

    #Performing subtraction..
    elif key == 2:
        num3 = num1 - num2
        print("Subtraction : ", num3)
    
    #Performing multiplication..
    elif key == 3:
        num3 = num1 * num2
        print("Multiplication : ", num3)

    #Performing division..
    elif key == 4:

        #checking if denominator is not equals to 0..
        if num2 != 0:
            num3 = num1 / num2
            print("Division : ", num3)
            
        #if it is equal show error and ask to input another number inplace of second..
        else:
            print("Error \n Number cannot be divided by zero\n")
            num4 = int(input("Enter the second number again : "))
            num3 = num1 / num4
            print("Division : ", num3)

    #Performing modulo division..
    elif key == 5:

        #checking if denominator is not equals to 0..
        if num2 >= 0:
            num3 = num1 % num2
            print("Modulo : ", num3)
            
        #if it is equal show error and ask to input another number inplace of second..
        else:
            print("Error \n Number cannot be divided by zero\n")
            num4 = int(input("Enter the second number again : "))
            num3 = num1 / num4
            print("Division : ", num3)
    #Exiting the program..
    elif key == 6:
        print("\n\n-----Thank you for using Python Calculator-----")
        break
    #If input does'nt matches the following standards, it will pass the Error for Wrong Input..
    else: 
        print("Wrong Input \n Try again !")
