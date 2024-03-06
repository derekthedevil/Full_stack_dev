
def add_n_numbers (*n):
    sum = 0
    for i in n :
        sum = sum + i
    print(sum)
    

add_n_numbers(10,20,30)


def calci(p,q):
    add = p +q 
    sub = p - q
    div = p/q 
    return add,sub,div

print(calci(10,2 ))