class mammal:
    def mammal_info(self):
        print("Mammal can gice direct birth.")
class wingedanimal:
    def wingleanimalinfo(self):
        print("Winged animal can flap.")

class bat (mammal,wingedanimal):
    pass

b1=bat()

b1.mammal_info()
b1.wingleanimalinfo()