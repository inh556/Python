from random import randint
print 'you name'
name = raw_input()
f = open('https://inh556.github.io/coursera-test/py/game.txt')
lines = f.readlines()
f.close()
scores = {}
for l in lines:
    s = l.split()
    scores[s[0]] = s[1:]
score = scores.get(name)
if score is None:
    score = [0,0,0]
game_times = int(score[0])
min_times = int(score[1])
total_times = int(score[2])

num = randint(1,5)
print 'guess what I think'
bingo = False
times = 0
while bingo ==False: 
    answer =input()
    times +=1
    print times
    if answer > num:
        print' too big'
    elif answer < num:
        print 'too small'
    else:
        print'bingo, you are right'
        bingo = True
if game_times == 0 or times < min_times:
        min_times = times
        print min_times
game_times +=1        
total_times +=times

scores[name] = [str(game_times), str(min_times), str(total_times)]
result = ''
for n in scores:
       line = n + ' ' + ' '.join(scores[n]) + '\n'
       result += line

output = open('https://inh556.github.io/coursera-test/py/gamere.txt', 'w')
output.write(result)
output.close()
