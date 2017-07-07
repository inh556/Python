S = input()
for i in range(len(S)):
   if S[i] == '+':
      print(int(S[0:i]) + int(S[i+1:len(S)+1]))