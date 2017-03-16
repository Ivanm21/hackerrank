# Kevin was thinking about telephone poles and came up with an idea for a fun programming challenge. There are N telephone poles ascending a mountain and each pole has a weight and 
# a unique altitude. Our program must move the poles into K number of stacks, but we can only rearrange the poles according to certain criteria:

# Poles can only be moved from higher altitudes to lower altitudes.
# Stacks can only be formed at the intial pole altitudes.
# A stack can consist of at least one pole.

# Moving the poles down the mountain also costs money. Moving a pole with weight W1 and altitude X1 to an altitude X2 of  where X2 > X1  costs = W x (X1-Xj) .

# Write a program to determine the least amount of money needed to rearrange the poles into  stacks.

import sys
import itertools




#n,k = input().strip().split(' ')
#n,k = [int(n),int(k)]

def subset(_index, set):
    sum = 0
    for i in _index:
        if i == _index[-1]:
            newset = set[_index.index(i):]
        else:
            newset = set[_index.index(i):_index.index(i)+1]

        if len(newset) > 1:
            for x in newset:
                sum += x[1]*(x[0] - newset[0][0])
    return sum
       


n = 6
k = 3

poles = []
costs = []

# for a0 in range(n):
#     x_i,w_i = input().strip().split(' ')
#     x_i,w_i = [int(x_i),int(w_i)]

#     poles.append((x_i,w_i))

poles.append((10,15))
poles.append((12,17))
poles.append((16,18))
poles.append((18,13))
poles.append((30,10))
poles.append((32,1))
#firstPole = poles[0]
sumarray =[]
for comb in itertools.combinations(poles,k):
    sumarray.append(subset(comb, poles))
    print (comb)
    print (subset(comb, poles))

#print (min(sumarray, key=int))

    # if comb[0] == firstPole:
    #     list = []
    # else:
    #     break
    # for pol in comb:
    #     list.append([pol])

    # record = poles   
    # for pol in comb:
    #     combs = []
    #     for _input in record:
    #         if pol[0] == comb[-1][0]:
    #             combs.append(_input)
    #         elif  _input[0] >= pol[0] and _input[0] < comb[comb.index(pol)+1][0]:
    #             combs.append([_input])
    #         record.remove(_input) 
    #     print (combs)



