# #Write a program: shopping list manager — user can add items, remove items, and view the list
# lst =["shampoo", "toilet paper", "tomato", "mouse pad", "sunscreen", "potato"] 
# def view(lst):
    
#     return print(lst)

# def add(lst):
#     take=input("what do you want to add in the list? ")
#     lst.append(take)
#     print(lst)

# def remove(lst):
#     take = input("what item do you want to remove ? ")
#     lst.remove(take)
#     print(lst) 


# def change(lst):
#     get = input("What new item do you want to add instead? ")
#     rem = input(f"What item in the list do you want to replace with {get}? ")

#     i = 0
#     while i < len(lst):
#         if lst[i] == rem:
#             lst[i] = get
#             print(lst)
#             break
#         i = i + 1
# user = input("Enter 1 to view the list, Enter 2 to add item, Enter 3 to change the item, Enter 4 if you want to remove any item : ")
# if user == str(1):
#     view(lst)

# if user == str(2):
#     add(lst)
    
# if user == str(4):
#     remove(lst)
# if user == str(3):
#     change(lst)

# # Either

# shopping_list = ["shampoo", "toilet paper", "tomato", "mouse pad", "sunscreen", "potato"]

# def view_items():
#     print("\nShopping List:")
#     for item in shopping_list:
#         print("-", item)

# def add_item():
#     item = input("Enter the item you want to add: ")
#     shopping_list.append(item)
#     print(f"{item} has been added.")

# def remove_item():
#     item = input("Enter the item you want to remove: ")

#     if item in shopping_list:
#         shopping_list.remove(item)
#         print(f"{item} has been removed.")
#     else:
#         print(f"{item} is not in the shopping list.")

# print("Shopping List Manager")
# print("1. View list")
# print("2. Add item")
# print("3. Remove item")

# choice = input("Choose an option: ")

# if choice == "1":
#     view_items()
# elif choice == "2":
#     add_item()
# elif choice == "3":
#     remove_item()
# else:
#     print("Invalid option.")


        





 #• Write a function that takes a list of numbers and returns the min, max, and average

lst=[1,3,6,12,56,64]
def take(lst):
    minimum = min(lst)
    maximum = max(lst)
    average = sum(lst)/len(lst)
    return minimum,maximum,average
print(take(lst))


# • Write a function that removes all duplicates from a list

# def remove_duplicate(lst):
#     result=[]
#     for item in lst:
#         if item not in result:
#             result.append(item)
#     return result
# print(remove_duplicate([4, 2, 2, 1, 3, 3]))

# • LeetCode #26 'Remove Duplicates from Sorted Array' — solve it
nums = [0,0,1,1,5,1,2,2,3,3,4]
def non_duplicate(nums):
    nums.sort()
    left = 0 
    for right in range(1,len(nums)):
        if nums[left] != nums[right]:
            left = left+1
            nums[left]= nums[right]
    return left+1

k =non_duplicate(nums)  
print(k)
print(nums[:k])