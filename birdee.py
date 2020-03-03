# Class bird represent the bird in kerala
class bird:

    def __init__(self, name, color):
        self.name = name
        self.color = color

    def crow(self, btype):
        '''The example of the instance variable
           ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        '''
        self.btype = btype
        L_crow = ["black crow", "house oriole"]
        print("The self parameter is a reference to the current"
              "instance of the class.\n The type of bird is"
              ":{}".format(self.btype))
        for crows in L_crow:
            if self.btype == crows:
                print("The bird is {}".format(self.btype))
            else:
                break


# class wetland inherit the bird class
class wetland_bird(bird):

    def __init__(self, name, color):
        super().__init__(name, color)

    def cattle_egret(self):
        print("The cattle egret is a cosmopolitan species"
              "of heron found in the tropics, subtropics, "
              "and warm-temperate zones.")

    def small_eget(self):
        print("The little egret is a species of small heron"
              "in the family Ardeidae.")


class add_example:

    def __init__(self, A):
        self.A = A

    def __add__(self, o):
        return(self.A + o.A)


bobj = bird("cuckoo", "black")
print("data from birdee class\n","--"*10)
print("name = {}, color ={} (parent class object)"
      .format(bobj.name, bobj.color))
bobj.crow("house crow")
wobj = wetland_bird("oriole", "yellow")
print("\nname = {}, color = {} (child class object)"
      .format(bobj.name, bobj.color))
ex1 = add_example(10)
ex2 = add_example(15)
print("result = ", ex1 + ex2)
print("--"*10)