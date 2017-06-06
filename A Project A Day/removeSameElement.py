lst_1 = [4,7,3,4,1,9,8,3,7]
lst_1.sort()
lst_2 = []
lst_2.append(lst_1[0])
for i in range(1,len(lst_1)):
      if lst_1[i] == lst_1[i-1]:
           continue
      else:
          lst_2.append(lst_1[i])
print lst_2
