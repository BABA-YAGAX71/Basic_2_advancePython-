import functools

# it's an anonymous funtion

def square(x):
    return x*x
n = square(5)
print(n)

# how to write lambd function --> lambda arguments: expression

square = lambda x: x*x
print(square(4))


add = lambda a,b: a+b
print(add(3,4))

# tuples
students = [('karim', 70), ('Rahim',90), ('sharif', 66)]

sorted_students = sorted(students, key= lambda x: x[1])
print(sorted_students)

# Map
x = [1,2,3,4,5,7,9,12,18]

#nums = list(map(square korte chacchi, square kake korte chacchi))
nums = list(map(lambda x: x*x, x))

print(nums)

#filters
num = list(filter(lambda x: x%2==0, x))
print(num)

#Reduce
n = functools.reduce(lambda x,y: x+y, nums)
print(n)