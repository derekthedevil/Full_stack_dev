class friend_1:
    fbike = "honda"
    fcar = "porche"

class friend_2:
    f1 = friend_1()
    f2b = f1.fbike
    f2c = f1.fcar
    
pratham = friend_2()
print(pratham.f2b)
print(pratham.f2c)