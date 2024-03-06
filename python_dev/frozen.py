l1 = [1,2,3,4,"hello"]
fs1 = frozenset(l1)
print(fs1)

t1 = (1,2,3,4,"hello")
fs2 = frozenset(t1)
print(fs2)

s1 = "string"
fs3 = frozenset(s1)
print(fs3)

set1 = {1,2,4,5,6,7,8,9}
fs4 = frozenset(set1)
print(fs4)


fset1 = frozenset({1,2,3})
fset2 = frozenset({3,4,5})


print(fset1.union(fset2))
print(fset1.intersection(fset2))
print(fset1.difference(fset2))