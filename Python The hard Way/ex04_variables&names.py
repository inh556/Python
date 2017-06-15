# how many cars
cars =100
# how many people can be carried on each car
space_in_a_car = 4.0
# how many drivers
drivers = 30
# how many passengers
passengers = 90
# How many cars will not be driven today
cars_not_driven = cars -drivers
#  how many cars can be driven
cars_driven = drivers
# how many passengers can be transported today
carpool_capacity = cars_driven * space_in_a_car
# how many passengers each car on average 
average_passengers_per_car = passengers /cars_driven

print "There are ", cars, "cars available."
print "There are only ", drivers, "drivers available."
print "There will be ", cars_not_driven, "empty cars today."
print "We can transport ", carpool_capacity, "people today."
print "We have ", passengers,  "to carpool today."
print "We need to put about ", average_passengers_per_car, "in each car."

i = 4.0
x = 20.0
y = 100.0
m = i * x
n = y / x
t = y - x * i
print m, n, t