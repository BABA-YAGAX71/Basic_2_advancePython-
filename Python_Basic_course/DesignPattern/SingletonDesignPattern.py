class Singleton:
    _intance = None

    def __new__(cls):
        if cls._intance == None:
            print("1st obj is created")
            cls._intance = super(Singleton, cls).__new__(cls)
        return cls._intance

ob1 = Singleton()
ob2 = Singleton()       

print(ob1 is ob2)