import Other
class Child(object):
	def __init__(self):
		self.other = Other()
	def implicit(self):
		self.other.implicit()
	def override(self):
		print  "CHILD ovrried()"
	def altered(self):
		print "CHILD before Other altered()"
		self.other.altered()
		print "CHILD after other altered()"
		
son = Child()


son.implicit()

son.override()
son.altered()