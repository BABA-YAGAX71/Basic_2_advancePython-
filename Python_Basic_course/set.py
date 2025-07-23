
# no duplicates
a = [23,23, 23, 34,34,56,56,1,1,1,3,45]

n = set(a)

print(n)

#Union, intersection

x = {1,2,3,4}
y = {1,3,5,7,8}


c = y.intersection(x)
d = x.union(y)
print(c)
print(d)