def choose(n, k):
   numerator = 1
   denominator = 1
   for i in range(1,n + 1):
      if i <=(n-k):
         denominator = denominator * i
      if i > k:
         numerator = numerator * i   
   return numerator/denominator


choose(20, 7)