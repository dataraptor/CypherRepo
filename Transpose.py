import math

def print_array(arr):
    for r in arr:
        for c in r:
            print('\''+str(c)+'\'', end=' ')
        print()

def arr2str(arr):
    s = ''
    for r in arr:
        for c in r:
            s += c
    return s

def transpose(arr):
    r = len(arr)
    if r == 0:
        return

    c = len(arr[0])
    
    t = []
    for i in range(c):
        row = []
        for j in range(r):
            row.append(arr[j][i])
        t.append(row)
    return t

def str2arr(s, nrows=4, ncolumn=4):
    t = [[' ']*ncolumn for i in range(nrows)]
    for idx, i in enumerate(s):
        r = math.floor(idx / ncolumn)
        c = idx % ncolumn
        t[r][c] = i
    return t

def change_case(arr):
    for idx_r, r in enumerate(arr):
        for idx_c, c in enumerate(r):
            arr[idx_r][idx_c] = arr[idx_r][idx_c].swapcase()
    return arr


q = str2arr('i am a man')
print(q)
qt = transpose(q)
qt = change_case(qt)
print(qt)
cy = arr2str(qt)
print('Cypher Text: ', cy)


print('Decryption: ')
q = str2arr(cy)
print(q)
qt = transpose(q)
qt = change_case(qt)
print(qt)
txt = arr2str(qt)
print('Plain Text: ', txt)
