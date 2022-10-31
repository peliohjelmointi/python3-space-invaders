#class variables

class Vehicle:
    wheels = 4

class Auto(Vehicle):    
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model
        #self.wheels = 5

skoda = Auto("Skoda","Superb")
print(skoda.wheels) #4
Vehicle.wheels = 5 #kaikille jotka perivät
print(Vehicle.wheels) #5
print(skoda.wheels) #5