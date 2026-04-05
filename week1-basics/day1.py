l = int(input("Enter the length of the rectangle: "))
h = int(input("Enter the breadth of the rectangle: "))

for i in range(1, l + 1):
    for j in range(1, h + 1):
        print(f"Multiplying {i} with {j} gets area {i * j}")
        break

# Write a program: calculate and print the area of a rectangle (ask for width and height
l = int(input("enter the length of the rectangle: "))
h = int(input("enter the breadth of the rectangle: "))
print(f"the area of rectangel is {(l)*(h)}")
# Write a program: convert Celsius to Fahrenheit — formula: F = C * 9/5 + 32
c_temp = float(input("Enter the temperature in celsius here: "))
C = c_temp
print(f"the provided temperature is converted in fahrenheit which is {C * 9/5 + 32}")