#use of OR

#checks the given numbers are equals or not

x = int(input("What's x : "))
y = int(input("What's y : "))

if(x<y or x>y):
    print("x is not equal to y")
else:
    print("x is equal to y")

# much simpler approach (!=)
x = int(input("What's x : "))
y = int(input("What's y : "))
if(x!=y):
    print("x is not equal to y")
else:
    print("x is equal to y")

# in reverse too  (==)
x = int(input("What's x : "))
y = int(input("What's y : "))
if(x==y):
    print("x is equal to y")
else:
    print("x is not equal to y")

# program to check the grade of students based on their marks
# using (and)

marks = int(input("Enter your marks : "))

if(marks >=90 and marks<=100):
    print("Grade A")
elif(marks >=80 and marks<90):
    print("Grade B")
elif(marks >=70 and marks<80):
    print("Grade C")
elif(marks >= 60 and marks<70):
    print("Grade D")
else:
    print("Grade F")

#making it more consized
#PYTHONIC WAY

marks = int(input("Enter your marks : "))

if 90 <= marks <= 100:
    print("Grade A")
elif 80 <= marks < 90:
    print("Grade B")
elif 70 <= marks < 80:
    print("Grade C")
elif 60 <= marks < 70:
    print("Grade D")
else:
    print("Grade F")

