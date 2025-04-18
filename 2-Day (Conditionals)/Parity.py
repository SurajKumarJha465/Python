# checking whether the given number is odd or even

# Use of boll

def main():
    num = int(input("Enter a number: "))

    if is_even(num):
        print(f"{num} is even")
    else:
        print(f"{num} is odd")

    

def is_even(x):
    if x % 2 == 0:
        return True
    else:
        return False

main()


#USING LAMBDA FUNCTION
#Pythonic way of doing the same thing

def main():

    num = int(input("What's x ? "))

    if is_even(num):
        print(f"{num} is even")
    else:
        print(f"{num} is odd")

def is_even(n):
    return True if n%2 == 0 else False # return n%2 == 0

main()

