try:
    with open("e:/Ostad/Python_Basic_course/name.txt", 'r') as f:
        print(f.read())
    print(10/10)
    x = int("12")
    a = [1,2,3]
    print(a[1])
    x = 10
except ZeroDivisionError:
    print("Error: jah bhokchod")    
except FileNotFoundError:
    print("File isn't found")
except IndexError:
    print("Index Error")        
