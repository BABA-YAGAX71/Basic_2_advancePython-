a = [23,11,17,34,77,53]

rslt = 0
i = 0

n = len(a)

while i<n:
    rslt = rslt + a[i]
    i = i + 1

print(rslt)   

x = [-12, 45, 67, -1, -9] # make the negative numbers 0
i = 0
while i<len(x):
    if x[i] < 0:
        x[i] = 0
    i += 1

print(x)        