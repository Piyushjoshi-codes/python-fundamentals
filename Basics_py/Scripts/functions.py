#function without parameters...
def greet():
    return "Good Morning!"
greet()

#function with a single parameter...
def say_hello():
    return ""

#function with multiple parameters...
def add(a, b, c):
    return a + b + c
number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))
number3 = int(input("Enter the third number: "))
add(number1, number2, number3)

#function with a condition...
def multiple(n):
    return n % 4 == 0
number = int(input("Enter the number to check if it's multiple of 4"))
if multiple(number):
    print(f"Yes, {number} is multiple of 4")
else:
    print(f"No, {number} is not the mutliple of 4: ")

#function with a loop...
def sum_even(n):
    sum_total = 0
    for i in range(2 , n + 1, 2):
        sum_total += i
    return sum_total
number_1 = int(input("Enter the number till you want to print the sum of even numers: "))
print(f"Total sum of even numbers till {number_1}: {sum_even(number_1)}")

#function to calculate for fibonacci series...
def fibonacci(n):
    a, b = 0, 1
    for i in range(n):
        print(a, end = " ")
        a, b = b, a + b
number_a = int(input("Enter the number upto to print fibonacci series: "))
fibonacci(number_a)