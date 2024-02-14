name = "pratham" 
print(name[0])
print(name[-1])
# print(name[10])

for i in name:
    print(i,end=" ")
    

print()

i = 0 
while(i<len(name)):
    print(name[i],end=",")
    i += 1
    
    


name= "mahabharat"
print(name[::])
print(name[0:len(name):1])
print(name[0:10:1])
print(name[-1:-11:-1])


# slice from beginning
print(name[0:4],name[:4])
print(name[0:7],name[0:7])
# till end
print(name[8:10],name[8:])
print(name[4:10],name[4:])
#middle 
print(name[3:7])

print(name[5:9:-1])
print(name[5:9:1])
print(name[9:2:-1])




print("hi"*5)
print("hi"+"bye")
print("n" in "python")
print("n" not in "python")
print("raj" > "bablu")








print("Hello".lower())
print("Hello".upper())
print("Hello".swapcase())
print("pratham bhalerao".title())
print("my name is pratham bhalerao ".capitalize() )
print("Hello455".lower())
print("5352546".lower())