import random

stars1 = open('oneStar.txt')
stars2 = open('twoStar.txt')
stars3 = open('thrStar.txt')
stars4 = open('fouStar.txt')
stars5 = open('fivStar.txt')

oneStrLst = list()
twoStrLst = list()
thrStrLst = list()
fouStrLst = list()
fivStrLst = list()

for line in stars1:
    oneStrLst.append(line)
for line in stars2:
    twoStrLst.append(line)
for line in stars3:
    thrStrLst.append(line)
for line in stars4:
    fouStrLst.append(line)
for line in stars5:
    fivStrLst.append(line)

oneStrRand = list()
twoStrRand = list()
thrStrRand = list()
fouStrRand = list()
fivStrRand = list()

count = 0
while count < 100:
    oneStrRand.append(random.choice(oneStrLst))
    twoStrRand.append(random.choice(twoStrLst))
    thrStrRand.append(random.choice(thrStrLst))
    fouStrRand.append(random.choice(fouStrLst))
    fivStrRand.append(random.choice(fivStrLst))
    count = count + 1

negReviews = open('samples/negativeReviews.txt', 'w')
neuReviews = open('samples/neutralReviews.txt', 'w')
posReviews = open('samples/positiveReviews.txt', 'w')

for line in oneStrRand:
    negReviews.write(line)
negReviews.flush()

for line in twoStrRand:
    negReviews.write(line)
negReviews.flush()

for line in thrStrRand:
    neuReviews.write(line)
neuReviews.flush()

for line in fouStrRand:
    posReviews.write(line)
posReviews.flush()

for line in fivStrRand:
    posReviews.write(line)
posReviews.flush()

print 'Finished gathering random samples.'
