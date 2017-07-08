#input a string of the form 123+345 output a integer 123 + 345 = 468
S = input()
for i in range(len(S)):
   if S[i] == '+':
      print(int(S[0:i]) + int(S[i+1:len(S)+1]))