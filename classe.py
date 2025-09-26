import testing
import merge_sort

print(testing.puzzle)


class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

#Use the Person class to create an object, and then execute the printname method:

x = Person("John", "Doe")
x.printname()

class Clerk(Person):
    def __init__(self, fname, lname, salary):
        super().__init__(fname, lname)
        self.salary = salary

    def printname(self):
        print('Novo: ')
        super().printname()
        Person.printname(self)

c = Clerk("Mateus", "Roberto", 5)
c.printname()
print(c.salary)