def find_mode(L):
   fre = [0]*10
   for i in L:
      fre[i] = fre[i] +1
   for i in range(10):
      if fre[i] == max(fre):
         return i

L =[9, 6, 7, 1, 1, 1, 1]
mode = find_mode(L)
print(mode)