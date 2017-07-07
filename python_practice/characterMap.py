for i in range(32,113,16):
   print('chr:',end= '  ')
   for j in range(16):
     
      print(chr(i+j),end='   ')
   print()
   print('asc:',end=' ')
   for j in range(16):
      if i +j >= 100:
          print(i+j,end = ' ')
      else:
          print(i+j,end = '  ')
   print()