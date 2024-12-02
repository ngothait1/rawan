import time
print("hello this my final project ")
 
user_name = input("what is your name? ")

print("hi " + user_name + ", nice to meet you")

print("this is a special calculator, i would need two numbers from you")

first_number    = float(input("First Number: "))
second_number   = float(input("Second Number: "))

print("Thank you for putting in your numbers, " + str(int(first_number)) + " and " + str(int(second_number)))

even_odd1 = first_number % 2 == 0
if even_odd1:
    even_odd1 = "even"
else:
     even_odd1 = "odd"

print("I can see that the first number is " + even_odd1)

even_odd2 = second_number % 2 == 0
if even_odd2:
    even_odd2 = "even"
else:
     even_odd2 = "odd"

print("And the second number is " + even_odd2)

if even_odd1 == even_odd2:  
    if even_odd1 == "odd":
        both = "odd"
    elif even_odd1 == "even":
        both = "even"
    print("So both of them are " + both)
else:
    print("So one of them is " + even_odd1 + " and the other is " + even_odd2)

operator = input("operator ( +, -, *, /): ")

if operator == '+':
    result = str(int(first_number)) + "  +  " + str(int(second_number)) + "  =  " + str(int(first_number + second_number))
elif operator == '-':
    result = str(int(first_number)) + "  -  " + str(int(second_number)) + "  =  " + str(int(first_number - second_number))
elif operator == '*':
    result = str(int(first_number)) + "  *  " + str(int(second_number)) + "  =  " + str(int(first_number * second_number))
elif operator == '/':
    if second_number != 0:
        result =str(first_number) + "  /  " + str(second_number) + "  =  " + str(first_number/second_number)
        decimal_or_int = input("Would you like the result to be an integer? (y/n): ")
        if decimal_or_int == "y":
            result = str(int(first_number)) + "  /  " + str(int(second_number)) + "  =  " + str(int(first_number / second_number))
    else:
        result = "Error: num_2 is zero \nAn error had occured , please try again"
        
else:
    result = "Error: " + "Operator " + operator + " is not supported \nAn error had occured , please try again" 

print(result)
print("Thank you " + user_name + " for using the calculator on " + time.ctime())
