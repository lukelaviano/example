class Shark:
    def __init__(self, name):
        self.name = name
#Using the shark class, the name parameter is passed through __init__, then self.name is defined as name
    def swim(self):
        print(self.name + " is swimming.")
#Swim method is defined, and can now be printed as using self and "is swimming"
    def be_awesome(self):
        print(self.name + " is being awesome.")
#Be awesome method is defined, and can now be printed using self and "is being awesome"
def main():
    sammy = Shark("Sammy")
    sammy.be_awesome()
    stevie = Shark("Stevie")
    stevie.swim()
    luke = Shark("Luke")
    luke.be_awesome()
#3 shark objects are being created named luke, sammy, and stevie. There are 2methods;swim and be awesome.
if __name__ == "__main__":
  main()
#calls all of the objects and methods to be defined. Name defines the actual name, while main is attached to the string