
class Employee:                                     # CLASS is  a combination of variables/attrubutes/data and functions/methods. 
    hike_percent = 1.2                              # OBJECT is an instance to the class
    no_of_employees = 0

    def __init__(self, fname, lname, salary):       # any function defined in class is called method.
        self.fname = fname 
        self.lname = lname                          # fname, lname , email, salary are istance variables
        self.salary = salary
        self.email = fname + '.' + lname + '@demo.com'
        Employee.no_of_employees += 1


    def fullname(self):
        return self.fname + ' ' + self.lname
    
    def sal_increment(self):
        self.salary = int(self.salary*Employee.hike_percent)
    

    @classmethod
    def set_hike_percent(cls, amt):
        cls.hike_percent = amt 


    @classmethod
    def from_str(cls, emp_str):
        fname, lname, salary = emp_str.split('-')
        return cls(fname, lname, salary)

print(Employee.no_of_employees)
emp1 = Employee('David','Smith',5000)       # emp1 is instance of class employee
emp2 = Employee('Maria', 'Jacob', 6000)       # emp2 is ALSO instance of class employee

emp3_str = 'Robin-Hood-8000'
fname, lname, salary = emp3_str.split('-')
print(fname, lname, salary)

emp3 = Employee(fname, lname, salary)
print(emp3.email)

# emp1.fname = 'David'    # fname, lname , email, salary are varialbles of instances
# emp1.lname = 'Smith'
# emp1.email = 'david@smith@demo.com'
# emp1.salary = 5000

# emp2.fname = 'Maria'
# emp2.lname = 'Jacob'
# emp2.email = 'maria.jacob@demo.com'
# emp2.salary = 6000


# Employee.hike_percent = 1.5
Employee.set_hike_percent(2)
emp1.sal_increment()
print(emp1.salary)



emp2.sal_increment()
print(emp2.salary)


emp1 = Employee('David','Smith',5000)       # emp1 is instance of class employee
emp2 = Employee('Maria', 'Jacob', 6000)       # emp2 is ALSO instance of class employee

emp3_str = 'Robin-Hood-8000'




fname, lname, salary = emp3_str.split('-')
print(fname, lname, salary)

emp3 = Employee(fname, lname, salary)
print(emp3.email)









