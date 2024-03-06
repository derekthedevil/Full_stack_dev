def global_inside_function():
    # global city = "pune "
    global city 
    city = "pune "
    
global_inside_function()
print(city)


# sum = 0 
def update_global():
    global sum 
    sum = 10 
    print(sum)

# print(sum)
# update_global()
# print(sum)
# print(14000/150)

def range_1_10(start,end):
    if(start <= end):
        print(start)
        start += 1
        range_1_10(start, end)

# range_1_10(1,100)

sum = 0
def print_sum(start,end):
    global sum
    if start <= end :
        sum = sum + start 
        start = start + 1
        print_sum(start,end)

print_sum(1,5)
print(sum)

