#Concepts related to float like round, formating numbers eg : 1,00,000

x = float(input("What's x ? "))
y = float(input("What's y ? "))

z = x/y
#to round the number to 2 decimal places
z = round(z, 2)

#using f stirng formatting to round the number
print(f"{z:.2f}")

"""
to format the number to 2 decimal places and add a comma as thousand separator
"""
a = 1000*1000
print(f"{a:,}")