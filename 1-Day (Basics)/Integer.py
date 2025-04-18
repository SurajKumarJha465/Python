#how to handle integer in the program 
""""
x = input("What's x ? ")
y = input("What's y ? ")

z = x + y
print ("The sum of x and y is ", z)

this will provide error since through input() we always gets string as an input
so we need to convert it into integer using int() function
"""

x = int(input("What's x ? "))
y = int(input("What's y ? "))

#now we can perform arithmetic operation on x and y
z = x + y
print ("The sum of x and y is ", z)

# or we can use float() function to handle decimal number
# x = float(input("What's x ? "))
# y = float(input("What's y ? "))
# z = x + y
# print ("The sum of x and y is ", z)
