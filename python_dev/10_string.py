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








print("HELLO".isupper())
print("HeLLo".isupper())

print("hello".islower())
print("Hello".islower())

print("hello Python".istitle())
print("Hello Python".istitle())


print("hello".isalpha())
print("hello5".isalpha())

print("hello45".isalnum())
print("Hello".isalnum())

print("4665".isalnum())

print("45".isdigit())
print("R45".isdigit())



name = 'virat18' 
sum = 0
for i in name :
    if name.isdigit() == True:
        sum += i
print(sum)
        

name = 'virat45' 
sum = 0
for i in name :
    if i.isdigit():
        sum = sum + int(i)
print(sum)


var = "a2b3c9d5"
alpa = ""
num = 0
for i in var:
    if i.isalpha():
        alpa= i
    elif i.isdigit():
        print(alpa*int(i),end="")


print(name.index("i"))
# print(name.index("ir"))
# print(name.index("z")) # gives errror in console is not found 
print(name.rindex("i"))


print(name.find("i"))
print(name.rfind("i"))
print(name.find("z")) # returns -1 if not found

result = name.find("z")
if result == -1:
    print("given substring is not present in name ")



date= "15/02/2024"
splited_date = date.split("/")
print(splited_date)

joind_date = "-".join(splited_date)
print(joind_date)



print(ord("A"))

print("delhi".startswith("d"))
print("delhi".startswith("D"))
print("delhi".startswith("del"))
print("delhi".startswith("e"))

print("delhi".endswith("i"))
print("delhi".endswith("I"))
print("delhi".endswith("hi"))


name = "raju"
upd_name1 = name.replace("r","k")
print(upd_name1)

upd_name2 = upd_name1.replace("k","b")
print(upd_name2)

x = "tomatto".replace("t","o",2)
print(x)


count_str = "pooja"
print(count_str.count("oj"))
print(count_str.count("z"))