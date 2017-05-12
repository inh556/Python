# for in n 
list1 = [1,2,3,5,8,19,23,24,34]
list2 = []
for i in list1:
    if i % 2 ==0:
        list2.append(i)
print list2


#comprehension

list1 = [1,2,3,5,8,14,23,24,34]
list3 = [i for i in list1]
print list3
list2 =[i/2 for i in list1 if i %2 ==0]
print list2

list5 = [i for i in range(1,101) if i %30 ==0]
print list5
print ';'.join([str(i) for i in range(1,101) if i % 2 == 0 and i % 3 == 0 and i % 5 == 0])

