my_name = 'Yanbin'
my_age = 30
my_height = 70 # inch
my_weight = 160 # lbs
my_eyes = 'black'
my_teech = 'white'
my_hair = 'black'
my_height_in_cm = my_height * 2.54
my_weight_in_kilo = (my_weight / 2.2 )
print "Let's talk about %s." % my_name
# height in inch
print "He is %d inches tall" % my_height
# height in cm
print "He is %d cm tall" % my_height_in_cm
# weight in pounds
print "He is %d pounds heavy" % my_weight
# weight in kilo
print "He is %d kilo heavy" % my_weight_in_kilo
print "Actually, that's not to hearvy"
print "He's got %s eyes and %s hairs." % (my_eyes, my_hair)
print "His teech are usually %r depending on the coffee." % my_teech

# this time is tricky, try to get it exactly right
print "if I add %r %d and %d I get %d." %(my_age, my_height,my_weight,my_age + my_height + my_weight)