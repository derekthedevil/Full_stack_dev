class Car :
    name = "honda"
    price = 25000
    password = 123
    
    def start_car(self,password):
        if password == self.password:
            print("car is starting ..........bruuuummmmmm")
        else :
            print("access denied ! please enter correct password")

Car()
c1 = Car()
print(c1.name)
print(c1.price)
c1.start_car(256)
c1.start_car(123)