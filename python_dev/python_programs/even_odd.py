data = [25,46,8,76,9,69,7]
even_list = []
odd_list = []
for i in data:
    if i%2 == 0:
        even_list.append(i)
    else:
        odd_list.append(i)

print("there are total ",len(even_list),"in the even list")
print("those are ",even_list)


print("there are total ",len(odd_list),"in the odd list")
print("those are ",odd_list)


even_sum = 0
for nums in even_list :
    even_sum = even_sum + nums
print("sum of all even numbers : " ,even_sum )


odd_sum = 0
for nums in odd_list :
    odd_sum = odd_sum + nums
print("sum of all odd numbers : " ,odd_sum )


even_large = 0
for num in even_list :
    if even_large < num :
        even_large = num

print("largest even number : " ,even_large)

odd_large = 0
for num in odd_list :
    if odd_large < num :
        odd_large = num

print("largest odd number : " ,odd_large)