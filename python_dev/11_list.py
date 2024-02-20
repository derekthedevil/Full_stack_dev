#  how to create a list 
data1 = [1,2,3,4,5,6,7,8,9,10]
print(data1)

data2 = "15-2-2024".split("-")
print(data2)

data3 = []
print(data3)

data4 = list["hello"]
print(data4)

data5 = list(range(1,6))
print(data5)

l1 = [10,20]
l2 = [30,40]
l3 = l1 +l2
l5 = l1*3
print(l5)
print(l3)
print(10 in l1)
print(100 not in l1)




# data1[3].append(99)
print(data1)



data = [55,88,22,44,33,99,77,22]

print (data.index(22))


L_index = []
for i in range(0,len(data)):
    if data[i] == 22 :
        L_index.append(i)
print(L_index)