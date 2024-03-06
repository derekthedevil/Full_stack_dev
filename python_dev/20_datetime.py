import datetime 

my_date = datetime.datetime.now()
print(my_date)
print(my_date.strftime("%d"))
print(my_date.strftime("%a"))
print(my_date.strftime("%A"))
print(my_date.strftime("%w"))
print(my_date.strftime("%m"))
print(my_date.strftime("%M"))


random_date = datetime.datetime(2024,3,4,11,20,40,939393)
print(random_date)
print(random_date.year,random_date.month,random_date.day)
print(random_date.hour,random_date.minute,random_date.second)
print(random_date.strftime("%d/%b/%Y"))


# diff between 2 dates 

d1 = datetime.date(2024,3,4)
d2 = datetime.date(2024,3,20)
print(d1-d2)
print(d2-d1)

