Python 3.6.5 (v3.6.5:f59c0932b4, Mar 28 2018, 16:07:46) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> class person:
	def __init__(self,name,age,height,weight):
		self.name = name
		self.age = age
		self.height = height
		self.weight = weight

		
>>> eliza = person("Eliza",20,"124cm","60kg")
>>> print(eliza.height)
124cm
>>> print(eliza.age)
20
>>> print(eliza.name)
Eliza
>>> def walk(self):
	print("I can walk fast!!")
	eliza.walk()

	
>>> print(eliza.walk)
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    print(eliza.walk)
AttributeError: 'person' object has no attribute 'walk'
>>> 
