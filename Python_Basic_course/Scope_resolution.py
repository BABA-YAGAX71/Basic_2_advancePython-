# L --> Local
# E --> enclosing
# G --> Global
# B --> Built in  scope

n = "Global" # global variable

def outer():
    n = "Enclosing" # Enclosing variable
    def inner():
        n = "Local" # Local variable
        print(n)
    inner()
    print(n)
outer()     
print(n)   