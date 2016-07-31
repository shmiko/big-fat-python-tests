class Parent():
	def __init__(self,last_name,eye_color):
		print("Parent constructor called")
		self.last_name = last_name
		self.eye_color = eye_color

class Child(Parent):
	def __init__(self,last_name, eye_color, number_of_toys):
		print("Child constructor called")
		Parent.__init__(self, last_name, eye_color)
		self.number_of_toys = number_of_toys

paul_richard = Parent("Jones","Green")
print(paul_richard.last_name)
# print(paul_richard.__name__)

jack_paul = Child("Jones","Brown",56)
print(jack_paul.last_name)
print(jack_paul.number_of_toys)