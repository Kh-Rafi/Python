
def add_all(*numbers):
    return sum(numbers)


print(add_all(1, 2, 3, 4))   



def greet(**words):
    for key, value in words.items():
        print(f"{key}: {value}")


greet(name="John", greeting="Hello")