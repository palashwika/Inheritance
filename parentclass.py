#Python code to demonstrate parent constructors
#are called

#parent class
class Person(object):

    # __init__ is known as the constructor


    def __init__(self,name,idnumber): #def is used to call a function
        self.name=name
        self.idnumber=idnumber
    def display(self):
        print(self.name)
        print(self.idnumber)

#child Class
class Employee(Person):
    def __init__(self,name,idnumber,salary,post):
        self.salary=salary
        self.post=post

        #invoking the __init__ of the parent class
    Person.__init__(self,name,idnumber)
    #def display(self):
       # print(self.name)
        #print(self.idnumber)
        #print(self.salary)
        #print(self.post)

#creation of an object variable or an instance
a=Employee('Sara', 541239, 8000000, "Manager")

#calling a function of the class Person using its instance
a.display() #only displays parent