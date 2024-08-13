class Dog():
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def sounds(self):
        return "WOOF!"
    
class Pit(Dog):
    def __init__(self, name, age):
        super().__init__(name, age)
    def food(self):
        return "beef"
    
Blu = Pit("blu", 5)
print(Blu.food())

#Inheritance works with "class". Remamber inheritance is 'IS A"