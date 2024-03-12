''''
result = None
try:
    x = int(input("Enter frist Number :"))
    y = int(input("Enter second Number :"))
    result = x//y
except ZeroDivisionError:
    print("cant be devided by zero")
except ValueError:
    print("please enter only numbers")
print(result)
hello
'''


