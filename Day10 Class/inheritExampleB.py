"""
	class BaseClass:
	  Body of base class
	class DerivedClass(BaseClass):
	  Body of derived class

"""
class Person:
		"""A simple attempt to model a person."""  
		def __init__(self, name, age):
			"""Initialize name and age attributes."""
			self.name = name
			self.age = age
        
		def walk(self):
			"""Simulate a person sitting in response to a command."""
			print(self.name.title() + " is now walking.")
		
		def run(self):
			"""Simulate person run in response to a command."""
			print(self.name.title() + " is now running!")
				
		def show(self):
			s =  self.name + ' ' + str(self.age)
			return s.title()

class Student(Person):
      
	def __init__(self,name,age,f):
		super().__init__(name, age)
		self.f = f
        
	def show(self):
			s =  self.name + ' ' + str(self.age)+ ' ' + str(self.f)
			return s.title()
			
s1 = Student('Meem',17,3000)
print(s1.show())	
			
p1 = Person('Nazmul', 46)
print("My name is " + p1.name.title() + ".")
print("I am " + str(p1.age) + " years old.")		
