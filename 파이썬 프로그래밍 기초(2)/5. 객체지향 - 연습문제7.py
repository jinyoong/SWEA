class Person:
     def getGender(self):
         return "Unknown"

class Male(Person):
    def getGender(self):
        return 'Male'

class Female(Person):
    def getGender(self):
        return 'Female'

x = Male()
y = Female()

print(x.getGender())
print(y.getGender())