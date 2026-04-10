# # Write a program: ask for user's name and age, print 'Hello [name], you are [age] years old'

# def form(name = "what name is yours", age="please tell me the age"):
#     print(f"hello {name}, you are {age} years old")
#     return 0
# name = input("enter your name here: ")
# age = input("what is your current age: ")
# form(name,age)

# # • Write a program: calculate and print the area of a rectangle (ask for width and height)
# def area(x,y):
#    print(x*y)
    
# l=22
# b=13
# area(l,b)


# # • Write a program: convert Celsius to Fahrenheit — formula: F = C * 9/5 + 32
# def c_to_f(x):
#     f = x * 9/5 + 32
#     print(f"on coverting Celsius to Fahrenheit we get {f} ")
#     return 0

# a= int(input("Enter measured temperature in celsius: "))
# c_to_f(a)

# # Write a grade calculator: ask for a score (0-100), print the grade (A/B/C/D/F)

# def g_calculator(x):
#     if x > 100:
#         print("dont fool me around")
#     elif x >= 85:
#         print("your grade is A ")
#     elif x >= 65:
#         print("your grade is B ")
#     elif x >= 55:
#         print("your grade is c ")
#     elif x >= 33:
#         print("your grade is D ")
#     else:
#         print("you need to study hard ")
#     return 0
# a = int(input("what are your total marks: "))
# g_calculator(a)

# # • Write a program: check if a number is positive, negative, or zero

# def check(x):
#     if x==0:
#         print("The number you have entered is zero")
#     elif x < 0:
#         print("your number is negative integer")
#     else:
#         print("your number is postive integer")
#     return 0

# a = int(input("enter the number you want to check as interger"))
# check(a)

# # • Write a program: ask for age, print if person is child (<13), teen (13-17), adult (18-64), or senior (65+)

# def age(x):
#     if x > 100:
#         print("you are a absolute servivor ")
#     elif x<=13:
#         print("you are considered as child")
#     elif x>13 and x<=17:
#         print(f"you are a teenager of {x} years old")
#     elif x >=18 and x<=64:
#         print(f"you are considered as adult person of age {x}")
#     elif x >=65:
#         print("you are considered as senior")
#     return x
# a = int(input("what is your age: "))
# age(a)

# # • Write a program: print numbers 1 to 100, but print 'Fizz' for multiples of 3, 'Buzz' for multiples of 5,
# # 'FizzBuzz' for both (classic interview question)

# def Fizzbuzz():
#     i=0
#     for i in range(1,101):
#         print(i)
#         if i % 3==0 and i % 5==0:
#             print("FizzBuzz")
#         elif i% 3==0:
#             print("Buzz")
#         elif i%5==0:
#             print("Fizz")
# Fizzbuzz()

# # • Write a program: calculate the sum of all numbers from 1 to N (ask user for N)

# def calculate(*args):
#     print( sum(*args))

# n = int(input(" set the end of range: "))
# a = range(1,n)
# calculate(a)


# # • Write a program: ask user to guess a number between 1-10, keep looping until they get it right

# def guess():
#     Number = 7
    
    
#     Try = int(input("Try a number between 0 to 10: "))
#     while Try != Number:
#             print("Try again, you guessed it wrong")
#             Try = int(input("Try a number between 0 to 10: "))

#     else:
#             print("yes this is the right guess")
            
# guess()
        
# #Write a function: is_even(n) — returns True if n is even, False if odd
 
# def is_even(n):
#     if n%2==0:
#         result = True
        
#     else:
#         result = False
    
#     print (result)
        
# a = int(input("check the number is even of not: "))   
# is_even(a)

# # Write a function: calculate_bmi(weight_kg, height_m) — returns BMI and prints category

# def calculate_bmi(weight_kg, height_cm):
#     height_m = height_cm / 100 
#     bmi = (weight_kg)/ (height_m**2) 
#     print(f"Your BMI is: {bmi:.2f}")

# w = 75
# h = 176
# calculate_bmi(w,h)

# #Write a function: count_vowels(text) — returns how many vowels are in a string

# def count_vowels(text):
#     x=0
#     for i in text:
#         if i in ["a","e","i","o","u"]:
#             x=x+1
#             print(f"it contain vowels {i}")
#         else:
#             print("it dosn't contain any vowels")
            
#     return x
# a = ("aqualink")
# result = count_vowels(a)
# print(f"total vowels: {result}")

# #LeetCode #1 Two Sum — attempt it using a brute force approach (two nested loops)
# def two_sum(nums, target):
#     for i in range(len(nums)):
#         for j in range(i+1, len(nums)):
#             if nums[i] + nums[j] == target:
#                 return [i, j]

# nums = [11, 15, 2, 7]
# target = 9
# print(two_sum(nums, target))

        