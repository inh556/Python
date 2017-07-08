# def getBASIC from subtask 1
def getBASIC():
   li = []
   while True:
	      line = input()
	      li.append(line)
	      if line.endswith('END'):
	           break
   return(li)
# def findLine from subtask 2
def findLine(prog, target):
   for i in range(len(prog)):
      if prog[i].startswith(target):
         return i
# def execute from subtask 3
def execute(prog):
  location = 0
  counter = 0
  while True:
     counter +=1
     if counter ==4:
         return "infinite loop"
         break
     line = prog[location].split()
     T = line[len(line)-1]
    #get T from prog[location] via str.split
     location = findLine(prog, T)
     if location==len(prog)-1:
         return "success"

print(execute(getBASIC()))
