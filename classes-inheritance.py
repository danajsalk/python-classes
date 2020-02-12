#Class Rich Design: encapsulation of 
class Person: 
    #self = instance of the class
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    #each func is method (type of func in class)
    def printname(self): 
        print(self.firstname, self.lastname)

# inherits everything from person class
class Student(Person):
    # init looks at lowest subclass
    def __init__(self, fname, lname, year):
        
        # super executes everything person, merges classes
        super().__init__(fname, lname) # looks at previous init that's overridden
        self.graduationyear = year
        
    def printname(self):
        super().printname()
        
        print(self.graduationyear)
        

x = Person("John", "Doe")
x.printname()

m = Student("Mike", "Olsen", 2019)
m.printname()


        
