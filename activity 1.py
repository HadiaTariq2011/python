class Vehicle:
    def __init__(self,name,max_speed,mileage):
        self.name=name
        self.max_speed=max_speed
        self.mileage=mileage
class Bus(Vehicle):
        pass
School_bus=Bus("School Volvo",180,12) 
print("vehicle name:",School_bus.name,"speed",School_bus.max_speed,"Mileage",School_bus.mileage )




class person(object):
     def __init__(self,idnumber,name):
          self.name=name
          self.idnumber=idnumber
     def display(self):
           print(self.name)
           print(self.idnumber)
class Employee(person):
      def __init__(self,name,idnumber,salary,post):
           self.salary=salary
           self.post=post 
           super().__init__(idnumber,name)   
a=Employee('Rahul',886012,2000000,"intern")
a.display()                          