position = (1, 2)
geeks = ('Sheldon', 'Leonard', 'Rajesh', 'Howard')

print position[0]
print geeks[1:3]
for g in geeks:
    print g


print '%s is %d years old' %('Mike', 23)

def get_pos(n):
    return (n/2, n*2)

x, y = get_pos(50)
print (x,y)


pos = get_pos(50)
print pos[0]
print pos[1]
