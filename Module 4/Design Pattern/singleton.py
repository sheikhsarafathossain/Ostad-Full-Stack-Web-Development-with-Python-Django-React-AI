class Singleton:
    _instance = None
    def __new__(cls):
        if cls._instance is None:
            print("Object Created")
            cls._instance = super(Singleton, cls).__new__(cls)
        return cls._instance
            


ob1 = Singleton()
ob2 = Singleton()
ob3 = Singleton()
print(ob1 is ob2 is ob3)