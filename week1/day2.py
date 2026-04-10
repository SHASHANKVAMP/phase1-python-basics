# #Write a grade calculator: ask for a score (0-100), print the grade (A/B/C/D/F)
# #• Write a program: check if a number is positive, negative, or zero
# #• Write a program: ask for age, print if person is child (<13), teen (13-17), adult (18-64), or senior (65+)

# score = int(input("What is your score out of 100: "))

# if score > 100:
#     print("Don't fool around!")
# elif score >= 90:
#     print("Your grade is A")
# elif score >= 70:
#     print("Your grade is B")
# elif score >= 55:
#     print("Your grade is C")
# else:
#     print("Your grade is F")


# check = int(input("Enter the number to be checked: "))

# if check == 0:
#     print("The number is zero")
# elif check < 0:
#     print("The number is negative")
# else:
#     print("The number is positive")

# age = int(input("Please enter your age: "))

# if age < 0 or age > 120:
#     print("Please enter a valid age")
# elif age < 13:
#     print("This person is a child")
# elif age < 18:
#     print("This person is a teen")
# elif age < 65:
#     print("This person is an adult")
# else:
#     print("This person is a senior")

# convert roman to integer
# def romtoint(s):
#     roman ={
# "I"      :      1,    
# "V"      :       5,
# "X"      :       10,
# "L"      :       50,
# "C"      :       100,
# "D"      :       500,
# "M"      :       1000
# }
#     result=0
#     for i in range(len(s)-1):
#         current = roman[s[i]]
#         next = roman[s[i+1]]
#         if current < next:      
#             result -= current
#         else:                   
#             result += current
#     result += roman[s[-1]]
#     return result

# a = "LVIII"
# print(romtoint(a))


  