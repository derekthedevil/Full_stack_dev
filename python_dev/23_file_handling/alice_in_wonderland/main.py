import os 
file_name = "alice_in_wonderland.txt"
is_file_exist = os.path.isfile(file_name)

if(is_file_exist):
    my_file = open(file_name,"r")
    x = my_file.read()
    my_file.close()
    list_of_words  = x.split(' ')
    split_list = []
    for i in list_of_words:
        if len(i.splitlines()) > 1:
            abc = i.splitlines()
            for items in abc :
                split_list.append(items)
        else :
            split_list.append(i)
    count = len(split_list)
    print(count)
    final_list  = []
    for i in range(0,count,1):
        print(split_list[i])
        if bool(split_list[i]) and (split_list[i] != " "):
            final_list.append(split_list[i])
    print((final_list))
    count = len(final_list)
    print(count)
    new_file = open("count.txt", "a")
    new_file.write("total number of words in the file are : ")
    new_file.write(str(count))
    new_file.write('\n')
    my_file.close()
else:
    print("file not exist")


