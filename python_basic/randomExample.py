import random
num = random.randint(1,2)
print num


num1 = random.random()
print num1


num2 = random.uniform(5,3)
print num2

from random import choice
num3 =  random.choice([1,2,3,4,5])
print num3
num4 = random.choice('hello')
print num4
num5= random.choice(['hello', 'halo'])
print num5

num6= random.choice((1,2,3))
print num6

num7 = random.randrange(0,7,3)
print num7

num8 = random.randrange(4)
print num8
num9 = random.randrange(1,4)
print num9

random.sample(population, k) #don't change position

random.shuffle(x) #change the positon of elements

print random.seed(3)
