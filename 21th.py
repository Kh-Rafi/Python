try:
    num = int(input("Enter a number: "))
    
    assert num % 2 == 0, "Not an even number!"
    reciprocal = 1 / num

except AssertionError as e:
    print(e)

except ZeroDivisionError:
    print("Cannot divide by zero!")

except ValueError:
    print("Invalid input! Please enter a number.")

else:
    print("Reciprocal:", reciprocal)