# Kevin was thinking about telephone poles and came up with an idea for a fun programming challenge. There are N telephone poles ascending a mountain and each pole has a weight and 
# a unique altitude. Our program must move the poles into K number of stacks, but we can only rearrange the poles according to certain criteria:

# Poles can only be moved from higher altitudes to lower altitudes.
# Stacks can only be formed at the intial pole altitudes.
# A stack can consist of at least one pole.

# Moving the poles down the mountain also costs money. Moving a pole with weight W1 and altitude X1 to an altitude X2 of  where X2 > X1  costs = W x (X1-Xj) .

# Write a program to determine the least amount of money needed to rearrange the poles into  stacks.

import sys
import itertools




n,k = input().strip().split(' ')
n,k = [int(n),int(k)]

def subset(_index, _set):
    sum = 0
    for i in _index:
        if i == _index[-1]:
            _from = _set.index(i)
            newset = _set[_from:]
        else:
            _from = _set.index(i)
            positionInIndex = _index.index(i) + 1
            _to = _set.index(_index[positionInIndex])
            newset = _set[_from:_to]

        if len(newset) > 1:
            for x in newset:
                sum += x[1]* (x[0] - newset[0][0])
    return sum
       



poles = []

 for a0 in range(n):
     x_i,w_i = input().strip().split(' ')
     x_i,w_i = [int(x_i),int(w_i)]

     poles.append((x_i,w_i))


firstPole = poles[0]
sumarray =[]
for indexes in itertools.combinations(poles,k):
    if indexes[0] == firstPole:
        sumarray.append(subset(indexes, poles))

print (min(sumarray, key=int))




