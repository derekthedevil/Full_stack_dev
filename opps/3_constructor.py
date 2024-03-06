class Employee :
    institute = "ITvedant"
    
    def  __init__(self, name, age):
        self.name = name
        self.age = age
        print("hello python")
        
    def hello():
        print("hello")
        

e1 = Employee("raj",50)
e2 = Employee("Pratham",20)


print(e1.name,e1.age,e2.name,e2.age)
print(e1.institute,e2.institute)