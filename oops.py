# class - unfilled railway reservation form
# object - filled railway reservation form

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def getSalary(self):
        return self.salary


rohan = Employee("Rohan", "34546")
print(rohan.name)
print(rohan.salary)

shree= Employee("Shree", "120000")
print(shree.name)
print(shree.salary)

# *********************************************************************************************

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def getSalary(self):
        print(self.salary)


rohan = Employee("Rohan", "34546")
print(rohan.name)
print(rohan.salary)

shree = Employee("Shree", "120000")
print(shree.name)
print(shree.salary)

rohan.getSalary()

