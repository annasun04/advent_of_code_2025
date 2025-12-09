import math
from collections import deque


# Part 1:
# between any two points
# calculate the largest rectangle size
# keep track of the largest
# input is col,row
# equation for area of rec given opposite corners

"""def partOne():
    max_area = 0
    for i in range(len(lines)):
        for j in range(i,len(lines)):
            r1 = int(lines[i][1])
            c1 = int(lines[i][0])
            r2 = int(lines[j][1])
            c2 = int(lines[j][0])
            cur_area = findArea(r1,c1,r2,c2)
            if cur_area > max_area:
                max_area = cur_area
    return max_area
# print(partOne())


# Part 2: brute force
# make a matrix and 
# put in red tiles
# then fill in the green tiles
# do same algorithm
# but have to do an 
# extra check to see if 
# tiles within that rectangle
# are valid (either red or green)"""
"""r = 0
c = 0
for i in range(len(lines)):
    r = max(r, int(lines[i][1]))
    c = max(c, int(lines[i][0]))

r+=1
c+=1
m = [['.']*c for i in range(r)]

for i in range(len(lines)):
    m[int(lines[i][1])][int(lines[i][0])] = "#"

for i in range(r):
    green = deque()
    f = 0
    for j in range(c):

        if m[i][j] == "#" and f==0:
            f = 1
        elif m[i][j] != "#" and f == 1:
            green.append([i,j])
        elif m[i][j] == "#" and f == 1:
            while green:
                g_tile = green.popleft()
                m[g_tile[0]][g_tile[1]] = "O"
for i in range(c):
    green = deque()
    f = 0
    for j in range(r):
        if m[j][i] == "#" and f==0:
            f = 1
        elif m[j][i] != "#" and f == 1:
            green.append([j,i])
        elif m[j][i] == "#" and f == 1:
            while green:
                g_tile = green.popleft()
                m[g_tile[0]][g_tile[1]] = "O"


for i in range(r):
    green = deque()
    f = 0
    for j in range(c):

        if (m[i][j] == "#" and f==0) or (m[i][j] == "O" and f==0) :
            f = 1
        elif m[i][j] != "#" and m[i][j] != "O" and f == 1:
            green.append([i,j])
        elif (m[i][j] == "#" and f == 1) or (m[i][j] == "O" and f == 1):
            while green:
                g_tile = green.popleft()
                m[g_tile[0]][g_tile[1]] = "O"

# now do part 1 but incorporate checking

def findArea(a,b,c,d, m):
    # ab is one corner
    # cd is another corner
    # |a-b|*|c-d|
    # check validity before, if not valid, return -1
    for i in range(min(a,c), max(a,c)+1, 1):
        for j in range(min(b,d), max(b,d)):
            
            if m[i][j] == ".":
                return -1

    return (abs(a-c)+1) * (abs(b-d)+1)

max_area = 0
for i in range(len(lines)):
    for j in range(i,len(lines)):
        r1 = int(lines[i][1])
        c1 = int(lines[i][0])
        r2 = int(lines[j][1])
        c2 = int(lines[j][0])
        cur_area = findArea(r1,c1,r2,c2,m)
        if cur_area > max_area:
            max_area = cur_area

print(max_area)"""

# Part 0: parse input
lines = []
file_name = 'ex.txt'
with open(file_name, 'r') as f:
    lines = [list(map(int, line.strip().split(","))) for line in f]
# scan from l to r, track col ranges
# scan from r to l, track col ranges
# scan from u to d, track row ranges
# scan from d to u, track row ranges

lines.sort(key=lambda x:x[0]) # by col
L = []
R = []
U = []
D = []
L_H = {}
R_H = {}
U_H = {}
D_H = {} 
ma = -float('inf')
mi = float('inf')
# if range increases and on different column, append new
# else just change range of most recent
cur_col = 0
for i in range(len(lines)-1, -1,-1):
    if i == len(lines)-1:
        cur_col = lines[i][0]
        L.append([lines[i][1], lines[i][1], cur_col])
        ma = lines[i][1]
        mi = lines[i][1]
    else:
        if lines[i][1] > ma:
            if cur_col == lines[i][0]:
                L[-1][1] = lines[i][1]
            else:
                L.append([mi, lines[i][1], lines[i][0]])
                cur_col = lines[i][0]
            ma = lines[i][1]
        elif lines[i][1] < mi:
            if cur_col == lines[i][0]:
                L[-1][0] = lines[i][1]
            else:
                L.append([lines[i][1], ma, lines[i][0]])
                cur_col = lines[i][0]
            mi = lines[i][1]
# print(L)
print("L")
for idx in range(len(L)):
    if idx == len(L) - 1:
        # Last entry covers from its col to infinity
        L_H[L[idx][2]] = idx
    else:
        # Entry covers from L[idx+1][2]+1 to L[idx][2]
        for col in range(L[idx+1][2] + 1, L[idx][2] + 1):
            L_H[col] = idx

ma = -float('inf')
mi = float('inf')
cur_col = 0
for i in range(len(lines)):
    if i == 0:
        cur_col = lines[i][0]
        R.append([lines[i][1], lines[i][1], cur_col])
        ma = lines[i][1]
        mi = lines[i][1]
    else:
        if lines[i][1] > ma:
            if cur_col == lines[i][0]:
                R[-1][1] = lines[i][1]
            else:
                R.append([mi, lines[i][1], lines[i][0]])
                cur_col = lines[i][0]
            ma = lines[i][1]
        elif lines[i][1] < mi:
            if cur_col == lines[i][0]:
                R[-1][0] = lines[i][1]
            else:
                R.append([lines[i][1], ma, lines[i][0]])
                cur_col = lines[i][0]
            mi = lines[i][1]
# print(R)
print("R")
for idx in range(len(R)):
    if idx == len(R) - 1:
        R_H[R[idx][2]] = idx
    else:
        for col in range(R[idx][2], R[idx+1][2]):
            R_H[col] = idx


lines.sort(key=lambda x:x[1]) # by row
ma = -float('inf')
mi = float('inf')
cur_row = 0
for i in range(len(lines)):
    if i == 0:
        cur_row = lines[i][1]
        U.append([lines[i][0], lines[i][0], cur_row])
        ma = lines[i][0]
        mi = lines[i][0]
    else:
        if lines[i][0] > ma:
            if cur_row == lines[i][1]:
                U[-1][1] = lines[i][0]
            else:
                U.append([mi, lines[i][0], lines[i][1]])
                cur_row = lines[i][1]
            ma = lines[i][0]
        elif lines[i][0] < mi:
            if cur_row == lines[i][1]:
                U[-1][0] = lines[i][0]
            else:
                U.append([lines[i][0], ma, lines[i][1]])
                cur_row = lines[i][1]
            mi = lines[i][0]

# print(U)
print("U")
for idx in range(len(U)):
    if idx == len(U) - 1:
        U_H[U[idx][2]] = idx
    else:
        for row in range(U[idx][2], U[idx+1][2]):
            U_H[row] = idx

ma = -float('inf')
mi = float('inf')
cur_row = 0
for i in range(len(lines)-1,-1,-1):
    if i == len(lines)-1:
        cur_row = lines[i][1]
        D.append([lines[i][0], lines[i][0], cur_row])
        ma = lines[i][0]
        mi = lines[i][0]
    else:
        if lines[i][0] > ma:
            if cur_row == lines[i][1]:
                D[-1][1] = lines[i][0]
            else:
                D.append([mi, lines[i][0], lines[i][1]])
                cur_row = lines[i][1]
            ma = lines[i][0]
        elif lines[i][0] < mi:
            if cur_row == lines[i][1]:
                D[-1][0] = lines[i][0]
            else:
                D.append([lines[i][0], ma, lines[i][1]])
                cur_row = lines[i][1]
            mi = lines[i][0]
# print(D)
print("D")
for idx in range(len(D)):
    if idx == len(D) - 1:
        D_H[D[idx][2]] = idx
    else:
        for row in range(D[idx+1][2] + 1, D[idx][2] + 1):
            D_H[row] = idx

# done with ranges
# now, find possible rectangles and when checking validity, check the point's all 4 directions
def isValid(r,c):
    
    """for i in range(len(L)):
        if i == len(L)-1:
            if not( r >= L[i][0] and r <= L[i][1]):
                    return False
        else:
            if c <= L[i][2] and c > L[i+1][2]:
                if not( r >= L[i][0] and r <= L[i][1]):
                    return False
                
    for i in range(len(R)):
        if i == len(R)-1:
            if not( r >= R[i][0] and r <= R[i][1]):
                    return False
        else:
            if c >= R[i][2] and c < R[i+1][2]:
                if not( r >= R[i][0] and r <= R[i][1]):
                    return False
                
    for i in range(len(U)):
        if i == len(U)-1:
            if not( c >= U[i][0] and c <= U[i][1]):
                    return False
        else:
            if r >= U[i][2] and r < U[i+1][2]:
                if not( c >= U[i][0] and c <= U[i][1]):
                    return False
    for i in range(len(D)):
        if i == len(D)-1:
            if not( c >= D[i][0] and c <= D[i][1]):
                    return False
        else:
            if r <= D[i][2] and r > D[i+1][2]:
                if not( c >= D[i][0] and c <= D[i][1]):
                    return False
    return True"""
    # Check L
    if c in L_H:
        idx = L_H[c]
        if not (r >= L[idx][0] and r <= L[idx][1]):
            return False
    
    # Check R
    if c in R_H:
        idx = R_H[c]
        if not (r >= R[idx][0] and r <= R[idx][1]):
            return False
    
    # Check U
    if r in U_H:
        idx = U_H[r]
        if not (c >= U[idx][0] and c <= U[idx][1]):
            return False
    
    # Check D
    if r in D_H:
        idx = D_H[r]
        if not (c >= D[idx][0] and c <= D[idx][1]):
            return False
    
    return True

    
    

def findArea(r1,c1,r2,c2):
    if ((abs(r1-r2)+1) * (abs(c1-c2)+1) < max_area):
        return -1

    for r in range(min(r1,r2), max(r1,r2)+1, 1):
        for c in range(min(c1,c2), max(c1,c2)+1, 1):
            # check all 4 directions for each point
            if not isValid(r,c):
                return -1

    return (abs(r1-r2)+1) * (abs(c1-c2)+1)

max_area = 0
for i in range(len(lines)):
    if i == len(lines)//2:
        print("halfway")
    if i == len(lines)//4:
        print("fourthway")
    if i == len(lines)//100:
        print("one hundreth way")

    for j in range(i,len(lines)):
        r1 = int(lines[i][1])
        c1 = int(lines[i][0])
        r2 = int(lines[j][1])
        c2 = int(lines[j][0])
        cur_area = findArea(r1,c1,r2,c2)
        if cur_area > max_area:
            max_area = cur_area
print(max_area)