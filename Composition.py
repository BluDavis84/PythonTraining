
class Payment:
    def __init__(self,wage, comission):
        self.wage = wage
        self.comission = comission

    def salary(self):
        return (self.wage * 52) + self.comission
class Person:
    def __init__(self, name, hei, wage, comission):
        self.name = name
        self.hei = hei
        self.obj_payment = Payment(wage , comission)
    def yearly(self):
        return self.obj_payment.salary()
    

LaVance = Person("LaVance", 6.1, 1000, 25000)
Wage_year = LaVance.yearly()
print(Wage_year)

    
    #Composition is "HAS A" relationship