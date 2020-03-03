class Descriptor(object):
    
    def __init__(self, name):
        self.name = name

    def __get__(self): 
        print("The old value:",self.name)
        return self.name
    def __set__(self,name):
        self.name = name
        print("The new value:",self.name)
    def __del__(self, name):
        print('Deleting value')  
        del self.name  
    
Dob = Descriptor("aksa")
print(Dob.name)
Dob.name = 'Aksa'  
del Dob.name 

    
