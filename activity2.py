class Employee:
    def __init__(self):
       print("employee created")
    def __del__ (self):
       print("destructor called")
def create_obj():
   print('making object...')
   obj=Employee()
   print('function end.....')
   return obj
print('calling create_obj() function...')
obj=create_obj()
print("end programe")