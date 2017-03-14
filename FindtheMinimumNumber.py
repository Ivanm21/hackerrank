import sys


n = int(input().strip())

res = "min(int, int)"
main = "min(int, "
lst = ")"

if n == 2:
    print(res)
else:
    for count in range(n):
        if count == n - 2:
            main +=  res + lst
        if count > 1:
            main += main
    
    print (main)


