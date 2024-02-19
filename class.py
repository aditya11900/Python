# Create a class and demonstrate name mangling to access private data and functions
class MyClass:
    def __init__(self):
        self.__private_var = 10
        self.public_var = 20
    
    def __private(self):
        print("Private")
    
    def public(self):
        print("Public")
        self.__private()

obj = MyClass()
print(obj.public_var)
obj.public()

print(obj._MyClass__private_var) 
obj._MyClass__private()          
          

