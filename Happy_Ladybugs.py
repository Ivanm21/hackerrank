'''#Happy Ladybugs is a board game having the following properties:

The board is represented by a string, , of length . The  character of the string, , denotes the  cell of the board.
If  is an underscore (i.e., _), it means the  cell of the board is empty.
If  is an uppercase English alphabetic letter (i.e., A through Z), it means the  cell contains a ladybug of color .
String  will not contain any other characters.
A ladybug is happy only when its left or right adjacent cell (i.e., ) is occupied by another ladybug having the same color.
In a single move, you can move a ladybug from its current position to any empty cell.
Given the values of  and  for  games of Happy Ladybugs, determine if it's possible to make all the ladybugs happy. For each game, print YES on a new line if all the ladybugs can be made happy through some number of moves; otherwise, print NO to indicate that no number of moves will result in all the ladybugs being happy.
'''
#!/bin/python3

import sys

def analyse(n, b):
    if b.count('_') == 0 and alreadyHappy(b):
        return "NO"
    for x in b:
        if b.count(x) == 1 and x!='_':
            return "NO"
    
    return "YES"

def alreadyHappy(b):
    if len(b) == 1:
        return True
    for x in set(b):
        print(x*b.count(x))
        print(b[b.index(x):b.index(x)])
        print(b[b.index(x):b.index(x) + b.count(x)])        
        if x * b.count(x) != b[b.index(x):b.index(x) + b.count(x)]:
             return True
    return False

b = "aassddwwweeeefшfff"
print(alreadyHappy(b))

'''Q = int(input().strip())
for a0 in range(Q):
    n = int(input().strip())
    b = input().strip()
    print(analyse(n,b))
'''