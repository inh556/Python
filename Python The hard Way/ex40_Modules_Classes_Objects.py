class Student(object):
	def __init__(self, name, score):
		self.name = name
		self.score = score
	def print_score(self):
		print "%s: %s" %(self.name, self.score)
	def get_grade(self):
		if self.score >= 90:
			return 'A'
		elif self.score >=60:
			return 'B'
		else:
			return 'C'
		
bart = Student("Bart Mith", 100)
print bart.name
print bart.score
bart.print_score()
print bart.get_grade()


import ex40_testfile
print ex40_testfile.aab