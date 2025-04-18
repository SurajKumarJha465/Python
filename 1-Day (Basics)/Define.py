#we use def keyword to define the function by our own

def hello():
    print("Hello,")

name = input("Enter your name: ")
hello()
print(name)

# function with argument
def hello(to):
    print("Hello, " + to)

name = input("What's your name: ")
hello(name)

#function with defult argument
def hello(to = "World"):
    print("Hello, " + to)

#we can call this function with or without argument
hello()
#we pass the argument 
name = input("What's your name: ")
hello(name)

#function with argument and return value
def main():
    num = int(input("Enter a number: "))
    print(f"{num} square is : " , square(num))

def square(n):
    return n * n # n**2 is also correct
                 # pow(n,2)

#calling the main function
main()