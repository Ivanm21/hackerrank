'''Alice is hosting a party! The party lasts for  minutes, and she puts out a bowl of  candies at the beginning of the party. During each minute , a person comes to the bowl and removes  candies.

Alice programs the following algorithm into her robot, Bob, to replenish the candy throughout the party:

If the party is ending (i.e., it's time ), do not refill the bowl.
If the bowl contains  candies at the end of minute  and , add  candies to the bowl.
For example, if , , and , then the candy bowl looks like this throughout the party:'''


import sys


n,t = input().strip().split(' ')
n,t = [int(n),int(t)]
c = list(map(int, input().strip().split(' ')))

time = 1
count = 0
capacity = n

while time < t:
    n = n - c[time-1]
    if n < 0:
        n = 0
    if n < 5:
        count += capacity - n
        n = capacity
    time += 1

print(count)

