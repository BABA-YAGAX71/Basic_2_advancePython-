a = [1,2,3,4,'a',5,8]

for i in a:
    if type(i) == type('str'):
        break #loop stopped
    else:
        print(i)    
print("\n")
for i in a:
    if type(i) == type('a'):
        continue # ignoring the value
    else:
        print(i)        