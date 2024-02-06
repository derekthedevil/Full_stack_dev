# datatype is used to recognise what kind of data variable holds

# in python datatype is categorise into 3 parts : numeric , boolean and collections 

#  in numeric there are three datatypes 

# # 1. int 
# # 2. float
# # 3. complex

#  in boolean there is one datatypes : bool  

#  in collections there are six datatypes : string, list, tuple, set frozenset and dictionary 

# ################# example for numeric datatype #########################

x = 5                       # integer value assigned to x   
y = 5                       # float value assigned to y 
z = 10 + 10.5j              # complex value assigned to z 

print(x ,type(x))
print(y,type(y))
print(z, type(z))

# ###############  examples for boolean  datatype #########################

d = True
e = False

print(d,type(d))
print(e,type(e))

################################  collections in python     #################################

f ='z'
g= 'python$123'
h = "java@123"
i = "525252"

print(f,type(f))
print(g,type(g))
print(h,type(h))
print(i,type(i))



j =""" my name is pratham bhalerao 
i live in vikhroli """

k = ''' my name is pratham bhalerao
i live in vikhroli'''

print(j,type(j))
print(k,type(k))


m = [10,20,'hello']
n= (10,20,'hello')
p = {10,20,'hello'}
q= frozenset({10,20,'hello'})
r = {'name':"raj","age":25}

print(m,type(m))
print(n,type(n))
print(p,type(p))
print(q,type(q))
print(r,type(r))




