def checkfile(filename):
    if not filename.endswith('.txt'):
        raise ValueError("Only .txt file are allowed")
    print("Valid file")

checkfile('data.csv')    

