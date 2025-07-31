class Pakistan():
    def capital(self):
        print("islamabad is the capital of pakistan")
    def language(self):
        print("urdu is widely spoken language of pakistan")
    def type(self):
        print("pakistan is developing country")
class USA (): 
    def capital(self):
        print("Washington is the capital of usa")
    def language(self):
        print("english is widely spoken language of pakistan")
    def type(self):
        print("pakistan is developed country")    
obj_pak=Pakistan()
obj_usa=USA()
for country in(obj_pak,obj_usa):
    country.capital()
    country.language()
    country.type()            