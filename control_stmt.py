###Indentation
print("Hello")
print("Welcome")



if 5 >2  :
    print("That's true")
    print("welcome to my world")


if True:
        print("this is true")
        print("this is not good")
        print("this is also good")


if False:
        print("this is false")
        print("this is not good")
        print("this is also good")

if 5 < 2  :
    print("That's true")
    print("welcome to my world")


if True:
        print("this is true")
        print("this is not good")
        print("this is also good")


if False:
        print("this is false")
        print("this is not good")
        print("this is also good")

num = -10
if (num > 0):
    print("Number is positive")

# check if given number is in range of 10 to 20
number = 23
if ( number >= 10 and number <=20 ):
    print("Number is in range")

# check if number is positive or negative
num = 10
if (num > 0):
    print("Number is positive")
else:
    print("Number is negative")
    
# Typical Voting App
age = 20
if age >= 18:
    print("You can Vote")
else:
    print("You cannot Vote")



# conversions
data = 3.14
print(data)

int_converted_data = int(data)
print(int_converted_data)

int_converted_data_float = float(int_converted_data)
print(int_converted_data_float)

int_data = 10
int_data_to_str = str(int_data)
print(int_data_to_str)
sofia
str_data="10"
str_date_to_int= int(str_data)
print(str_date_to_int)

str_data="20"
str_date_to_int= int(str_data)
print(str_date_to_int)

# input() : used to take input from keyboard
name = input("Enter Your Name: ")
print("Welcome: "+name)

age = input("Enter Your Age: ")
age = int(age)
if age >= 18: # # TypeError: '>=' not supported between instances of 'str' and 'int'
    print("You can Vote")
else:
    print("You cannot Vote")


number = int(input("Enter Your Number: "))
print(number+2)