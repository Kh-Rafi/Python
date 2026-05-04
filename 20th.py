try:
    even_number=[1,2,4,5,6]
    print(even_number[2])
except ZeroDivisionError:
    print("Denominator can not be 0.")
except IndexError:
    print("Out of Index.")