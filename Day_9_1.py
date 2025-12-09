# Part 0: parse input
lines = []
file_name = 'ex.txt'
with open(file_name, 'r') as f:
    lines = [list(map(int, line.strip().split(","))) for line in f]

# Create a set of red tiles for O(1) lookup
red_tiles = set((x, y) for x, y in lines)

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

for idx in range(len(L)):
    if idx == len(L) - 1:
        L_H[L[idx][2]] = idx
    else:
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

for idx in range(len(D)):
    if idx == len(D) - 1:
        D_H[D[idx][2]] = idx
    else:
        for row in range(D[idx+1][2] + 1, D[idx][2] + 1):
            D_H[row] = idx

# Cache for isValid results
valid_cache = {}

def isValid(r, c):
    # Check cache first
    key = (r, c)
    if key in valid_cache:
        return valid_cache[key]
    
    result = True
    
    # Check L
    if c in L_H:
        idx = L_H[c]
        if not (r >= L[idx][0] and r <= L[idx][1]):
            result = False
            valid_cache[key] = result
            return result
    
    # Check R
    if c in R_H:
        idx = R_H[c]
        if not (r >= R[idx][0] and r <= R[idx][1]):
            result = False
            valid_cache[key] = result
            return result
    
    # Check U
    if r in U_H:
        idx = U_H[r]
        if not (c >= U[idx][0] and c <= U[idx][1]):
            result = False
            valid_cache[key] = result
            return result
    
    # Check D
    if r in D_H:
        idx = D_H[r]
        if not (c >= D[idx][0] and c <= D[idx][1]):
            result = False
            valid_cache[key] = result
            return result
    
    valid_cache[key] = result
    return result

def findArea(r1, c1, r2, c2):
    # Early exit if area is too small
    potential_area = (abs(r1-r2)+1) * (abs(c1-c2)+1)
    if potential_area <= max_area:
        return -1
    
    min_r, max_r = min(r1, r2), max(r1, r2)
    min_c, max_c = min(c1, c2), max(c1, c2)
    
    # Check corners first (most likely to fail)
    if not isValid(min_r, min_c) or not isValid(max_r, max_c):
        return -1
    if not isValid(min_r, max_c) or not isValid(max_r, min_c):
        return -1
    
    # Check edges before checking interior
    # Top and bottom edges
    for c in range(min_c + 1, max_c):
        if not isValid(min_r, c) or not isValid(max_r, c):
            return -1
    
    # Left and right edges
    for r in range(min_r + 1, max_r):
        if not isValid(r, min_c) or not isValid(r, max_c):
            return -1
    
    # Check interior
    for r in range(min_r + 1, max_r):
        for c in range(min_c + 1, max_c):
            if not isValid(r, c):
                return -1
    
    return potential_area

max_area = 0

# Sort by potential area (larger rectangles first)
# This helps us find max_area faster and prune more
pairs = []
for i in range(len(lines)):
    for j in range(i + 1, len(lines)):
        r1, c1 = lines[i][1], lines[i][0]
        r2, c2 = lines[j][1], lines[j][0]
        potential = (abs(r1-r2)+1) * (abs(c1-c2)+1)
        pairs.append((potential, i, j))

# Sort by potential area descending
pairs.sort(reverse=True)

checked = 0
for potential, i, j in pairs:
    # Skip if this pair can't possibly beat current max
    if potential <= max_area:
        break
    
    r1, c1 = lines[i][1], lines[i][0]
    r2, c2 = lines[j][1], lines[j][0]
    
    cur_area = findArea(r1, c1, r2, c2)
    if cur_area > max_area:
        max_area = cur_area
        print(f"New max: {max_area} at iteration {checked}")
    
    checked += 1
    if checked % 10000 == 0:
        print(f"Checked {checked}/{len(pairs)} pairs, current max: {max_area}")

print(max_area)