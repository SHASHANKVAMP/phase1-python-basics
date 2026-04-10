# #Write a program: print numbers 1 to 100, but print 'Fizz' for multiples of 3,
# #  'Buzz' for multiples of 5,'FizzBuzz' for both (classic interview question)

# for i in range(0,101):
#     if i%3==0 and i%5==0:
#         print("FizBuzz")
#     elif i % 3 == 0:
#         print("FIzz")
#     elif i%5 == 0:
#         print("buzz")
#     else:
#         print(i)

# #Write a program: calculate the sum of all numbers from 1 to N (ask user for N)
# a = int(input("enter the number that will be the end of range: "))
# t = 0
# for i in range(1,a):
#     t = t + i
# print(t)

# #Write a program: ask user to guess a number between 1-10, keep looping until they get it right
# guess = 0
# number =7
# while guess!= number:
#     guess = int(input("try a number between 1-10:"))
    
#     if guess == number:
#         print("you guessed it right")

#     else:
#         print ("try again")

# # what if there are only three tries to guess
# Try = 0
# number =7
# while Try <3:
#     Try = Try+ 1
#     if guess!= number:
#         guess =int(input("try the number : "))
#         print(f" number of attempt are {Try}")
#     elif guess == number:
#         print("yes this is the wright guess")
#     else:
#         print("try again")


# nums = [11,15,2,7]
# target = 9

# for i in range(len(nums)):
#     for j in range(i+1,len(nums)):
#         if nums[i]+nums[j] == target:
#             print("correct")
#         else:
#             print(" move next")
   


   
