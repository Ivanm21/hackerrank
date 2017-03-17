import sys

n = 6
k = 3

poles = []

poles.append((6,2))
poles.append((10,15))
poles.append((12,17))
poles.append((16,18))
poles.append((18,13))
poles.append((30,10))
poles.append((32,1))


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


def combinations (A, k, start, currLen, used):
    sub = []
    if currLen == k:
        subsub = []
        for i in A:
            if used[A.index(i)] == True:
                subsub.append(i)
        print()
        return  subsub     

    if start == len(A):
        return sub
        
    used[start] = True
    sub.append(combinations(A,k,start+1 ,currLen +1,used))

    if start != 0:
        used[start] = False
        sub.append(combinations(A,k,start +1,currLen,used))
    
    return sub

used = [False]*len(poles)
x = combinations(poles, k, 0,0,used)
print (x)



	