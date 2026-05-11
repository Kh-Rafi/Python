class SuperClass:

    def super_method(self):
        print("Super Class method called")

class DerivedClass1(SuperClass):
    def derived1_method(self):
        print("Derived class 1 method called")

class DerivedClass2(DerivedClass1):

    def derived2_method(self):
        print("Derived class 2 method called")

d2 = DerivedClass2()

d2.super_method()  

d2.derived1_method()  

d2.derived2_method()  