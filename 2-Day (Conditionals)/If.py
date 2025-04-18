# Understanding the working of Conditional Statements in Python
#===========================================================
# if

#here ther is repatative
x = int(input("What's x ? "))
y = int(input("What's y ? "))

if(x>y):
    print(f"{x} is greater than {y}")
if(x<y):
    print(f"{x} is less than {y}")
if(x==y):
    print(f"{x} is equal to {y}")

#more consized version of the above code
x = int(input("What's x ? "))
y = int(input("What's y ? "))

if(x>y):
    print(f"{x} is greater than {y}")
elif(x<y):
    print(f"{x} is less than {y}")
else:
    print(f"{x} is equal to {y}")