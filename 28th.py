class Animal:


    name = ""
    
    def eat(self):
        print("I can eat")


class Dog(Animal):

  
    def eat(self):
        print("I like to eat bones")


labrador = Dog()


labrador.eat()