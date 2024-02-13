marks = [99,45,35,95]
for mark in marks :
    if mark < 80 :
        pass
    else :
        print(mark)
        
prices = [99,199,299,99,399,199]
for price in prices :
    if price ==199 :
        print("i am skipping this price")
        break
    else:
        print("add to cart")
        
        
        
prices = [99,199,299,99,399,199]
for price in prices :
    if price ==199 :
        print("i am skipping this price")
        continue
    else:
        print("add to cart")