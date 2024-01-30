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
    

class Developer(Employee):
    def __init__(self, fname, lname, salary, skill):
        super().__init__(fname, lname, salary)
        self.skill = skill



class Manager(Employee):
    def __inti__(self, fname, lname, salary, team_members):
        super().__init__(fname, lname, salary)
        self.team_members = team_members

    def add_members(self, emp):
        if emp not in self.team_members:
            return self.team_members.append(emp)




emp1 = Employee('David','Smith',5000)       # emp1 is instance of class employee
emp2 = Employee('Maria', 'Jacob', 6000)       # emp2 is ALSO instance of class employee

emp3_str = 'Robin-Hood-8000'

dev1 = Developer('Steve', 'John', 3000, 'Python')

mgr1 = Manager('Nickolas', 'Drake', 15000, ['dev1'])


print(mgr1.email)

print(mgr1.team_members)


print(dev1.email)
print(dev1.skill )

 
