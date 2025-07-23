a = {'karim' : 14,'rahim' : 34, 1 : {2,3,4} , 2 : [5,6,7,8]}

print(type(a))
for i in a:
    print(i)

print("_________________")    

for i in a.values():
    print(i)
print(a.keys(), a.values())

print('__________________')

for k,v in a.items():
    print(f"the key value: {k}, values: {v}")

print("__________________")  
  
a = [1,2,3]
b = ['mango', 'banana', 'grape']

c = dict(zip(a, b))
print(c)