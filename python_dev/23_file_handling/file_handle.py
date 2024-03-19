# x = "C:/Users/prath/OneDrive/Desktop/Full_stack_dev/python_dev/23_file_handling/test.txt"
# open(x,"r")
# print("file exists")


import os 
file_name = "test.txt"
is_file_exist = os.path.isfile(file_name)

if(is_file_exist):
    my_file = open("test.txt", "r")
    # print(my_file.read(),1)
    print(my_file.read(5),2)
    print(my_file.readline(),3)
    print(my_file.readlines(),4)
    my_file.close()
    
else:
    print("non exist")
    


with open("test.txt","r") as test_file:
    print(test_file.name)
    print(test_file.closed)

print(test_file.closed)
print(bool(""))