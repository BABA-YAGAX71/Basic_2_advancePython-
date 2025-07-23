
#Custom Error baniyechi
def checkfile(filename):
    if not filename.endswith('.txt'):
        raise ValueError("Only .txt file are allowed")
    print("Valid file")

checkfile('data.csv')    


# Custom Error handling
try:
    checkfile('data.csv')

except Exception as e:
    print(e)    