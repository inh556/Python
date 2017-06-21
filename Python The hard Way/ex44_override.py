class Parent(object):
	def override(self):
		print "PARENT override"
	def override1(self):
		print "A test of override"
class Child(Parent):
	def override(self):
		print "Child override"

dad = Parent()
son = Child()

dad.override()
son.override()
son.override1()