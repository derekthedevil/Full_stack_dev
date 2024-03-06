class Car:
    seater = 4 
    def __init__(self, name, brand):
        self.cname = name 
        self.cbrand = brand
        
    def changeCarName(self,new_name):
        self.cname = new_name
        # print(self.cname)
        
    @classmethod
    def changeSeatsNumber(cls,new_seats):
        cls.seater = new_seats
        # print(cls.seater)
        # print(Car.seater)
        
c1 = Car("i10","hyundai")
print(c1.cname,"before changing car name ")
c1.changeCarName("i20")
print(c1.cname,"after changing car name ")


print("before calling class method")
print(c1.seater,"printing seater value by object variable ")
print(Car.seater,"printing seater value by object name ")
c1.changeSeatsNumber(6)
print("after calling class method")
print(c1.seater,"printing seater value by object variable ")
print(Car.seater,"printing seater value by object name ")