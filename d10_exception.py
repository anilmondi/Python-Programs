a=int(input("Enter a number"))
try:
    b=int(input("Enter another number"))
except ValueError:
    print("Enter only numbers")
try:
    print(a/b)
except:
    print("Error occured")
finally:
    print("Welcome")
