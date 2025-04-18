# working of while loop

i = 3

while i!=0:
    print("Hello")
    i -= 1

#if we want any i/p with certain condition then we can use infinite while loop

while True:
    i = int(input("Enter a number: "))
    if i<0:
        continue
    elif i>=0:
        break
for _ in range(i):
    print("Hello3")

# implementing while loop using function

def main():
    number = get_number()
    display(number)

def get_number():
    while True:
        num = int(input("What's number : "))
        if num < 0:
            print("Sorry, try again.")
            continue
        else:
            return num

def display(n):
    for _ in range(n):
        print("Hello4")

main()





# working of for loop with list

for i in [1,2,3,4,5]:
    print("Hello")

#using range()

for i in range(5):
    print("Hello")

# PYTHONIC WAY OF WRITING FOR LOOP

for _ in range(5):
    print("Hello")