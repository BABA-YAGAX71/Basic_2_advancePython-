a = [24,5,35,48,67]

result = []

for i in a:
    if i%2 == 1:
        result.append(i)
print(result)        

# list cpmprehension

New_result = [i for i in a if i%2==0]
print(New_result)


b = [1,2,3,4,5,6] # --> [1,4,3,16,5,36]
'''re = []
for i in b:
    if i%2 == 0:
        i**2
        re.append(i)
    else:
        i

print(re)  '''      

b_new = [i**2 if i%2 == 0 else i for i in b]

print(b_new)