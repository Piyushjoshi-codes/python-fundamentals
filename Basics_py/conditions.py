#Creating a program for grading system..
phy_marks = int(input("Enter the marks for Physics : "))
chem_marks = int(input("Enter the marks for Chemistry : "))
Python_marks = int(input("Enter the marks for Python : "))
math_marks = int(input("Enter the marks for Mathematics : "))
cpp_marks = int(input("Enter the marks for DSA in C++ : "))
attendance = int(input("Enter the total percent of attendance : "))
total_marks = phy_marks + chem_marks + Python_marks + math_marks + cpp_marks 
percent = total_marks/500 * 100
print(f"Total marks out of 500 : {total_marks}")
print(f"Total percentage : {percent}")

#using conditions to check if the student passed or failed...
if percent == 100:
    print("You have scored Excellent marks!!\n" \
    "Congratulations!\n" \
    "You Passed")
elif percent >= 90:
    print("You have scored very good marks!!\n" \
    "Congratulations\n" \
    "You Passed")
elif percent >= 80:
    print("You have scored good marks!!\n" \
    "Congratulations\n" \
    "You Passed")
elif percent >= 70:
    print("You have scored average marks but can do much better\n" \
    "Congratulations\n" \
    "You passed")
elif percent >= 0:                             #using nested if-elif-else conditions...
    if percent > 35:
        print("Congratulations\n" \
        "You passed but try better")
    elif percent <= 35:
        if attendance >= 75:
            print("You failed\n" /
                  "You are allowed for reexamination!!")
        else:
            print("You failed\n" \
            "Is being held in the same standard due to lack of attendance!!")
else:                                          #else conditions as a default condition if input is wron
    print("Wrong Input!!")