from math import floor

f = open('speeds.dat', 'r')
info = f.readlines()

name = []
dist = []
time = 2503
score = {}
reindeers = {}

for line in info:
    words = line.split()
    name.append(words[0])
    speed = int(words[3])
    run_time = int(words[6])
    rest_time = int(words[13])
    reindeers[words[0]] = [speed, run_time, rest_time]
    score[words[0]] = 0
    tmp1 = floor(time/(run_time+rest_time))
    tmp2 = time % (run_time+rest_time)
    tmp_dist = speed * tmp1 * run_time
    dist.append(tmp_dist + min(tmp2, run_time)*speed)

winner = [i for i in range(len(dist)) if dist[i] == max(dist)]
print("The winning reindeer is %s, who ran %i km." % (name[winner[0]], max(dist)))


for second in range(1,time+1):
    dist_max = -1
    winner = []
    for reindeer in reindeers.keys():
        tmp1 = floor(second/(reindeers[reindeer][1]+reindeers[reindeer][2]))
        tmp2 = second % (reindeers[reindeer][1]+reindeers[reindeer][2])
        speed = reindeers[reindeer][0]
        dist = speed * tmp1 * reindeers[reindeer][1] + min(tmp2, reindeers[reindeer][1]) * speed
        if dist > dist_max:
            dist_max = dist
            winner  = [reindeer]
        elif dist == dist_max:
            winner.append(reindeer)
    for i in range(len(winner)):
        score[winner[i]] += 1
    
print("After Santa changed the Olympics, the score of the winner is ", max(score.values()))

        
    
