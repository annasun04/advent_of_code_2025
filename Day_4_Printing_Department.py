# Part 0: parse input
from collections import deque
filename = 'ex.txt'
matrix = []
with open(filename, 'r') as f:
    for line in f:
        row = list(line.strip())
        matrix.append(row)
# print(matrix)
# Part 1: 
# for each index if it is a '@' check surrounding and find count
# if count < 4, total +=1
n = len(matrix)
m = len(matrix[0])
total_count = 0
for i in range(n):
    for j in range(m):
        if matrix[i][j] == "@":
            nei_count = 0
            #cross
            if i-1>=0 and matrix[i-1][j] == "@":
                nei_count +=1
            if i+1<n and matrix[i+1][j] == "@":
                nei_count +=1
            if j-1>=0 and matrix[i][j-1] == "@":
                nei_count +=1
            if j+1<m and matrix[i][j+1] == "@":
                nei_count +=1
            #diagonals
            if i-1>=0 and j-1 >= 0 and matrix[i-1][j-1] == "@":
                nei_count +=1
            if i-1>=0 and j+1 < m and matrix[i-1][j+1] == "@":
                nei_count +=1
            if i+1<n and j-1 >= 0 and matrix[i+1][j-1] == "@":
                nei_count +=1
            if i+1<n and j+1 < m and matrix[i+1][j+1] == "@":
                nei_count +=1
            if nei_count < 4:
                total_count +=1
#print(total_count)

# Part 2:
# I think potentially bfs
n = len(matrix)
m = len(matrix[0])
total_count = 0
s = deque()




def valid_paper(i, j, n, m):
    
    nei_count = 0
    if i < 0 or j < 0 or i >= n or j >= m:
        return False
    if matrix[i][j] != "@":
        return False

    #cross
    if i-1>=0 and matrix[i-1][j] == "@":
        nei_count +=1
    if i+1<n and matrix[i+1][j] == "@":
        nei_count +=1
    if j-1>=0 and matrix[i][j-1] == "@":
        nei_count +=1
    if j+1<m and matrix[i][j+1] == "@":
        nei_count +=1
    #diagonals
    if i-1>=0 and j-1 >= 0 and matrix[i-1][j-1] == "@":
        nei_count +=1
    if i-1>=0 and j+1 < m and matrix[i-1][j+1] == "@":
        nei_count +=1
    if i+1<n and j-1 >= 0 and matrix[i+1][j-1] == "@":
        nei_count +=1
    if i+1<n and j+1 < m and matrix[i+1][j+1] == "@":
        nei_count +=1
    if nei_count < 4:
        return True
    return False

    

for i in range(n):
    for j in range(m):
        if valid_paper(i,j,n,m):
            s.append([i,j])
            matrix[i][j] = '.'

          
print("s", s)

# run bfs
while s:
    item = s.popleft()
    total_count+=1
    r = item[0]
    c  = item[1]
    if valid_paper(r-1,c,n,m):
        matrix[r-1][c] = '.'
        s.append([r-1,c])

    if valid_paper(r+1,c,n,m):
        matrix[r+1][c] = '.'
        s.append([r+1,c])

    if valid_paper(r,c-1,n,m):
        matrix[r][c-1] = '.'
        s.append([r,c-1])

    if valid_paper(r,c+1,n,m):
        matrix[r][c+1] = '.'
        s.append([r,c+1])

    if valid_paper(r-1,c-1,n,m):
        matrix[r-1][c-1] = '.'
        s.append([r-1,c-1])

    if valid_paper(r-1,c+1,n,m):
        matrix[r-1][c+1] = '.'
        s.append([r-1,c+1])

    if valid_paper(r+1,c-1,n,m):
        matrix[r+1][c-1] = '.'
        s.append([r+1,c-1])

    if valid_paper(r+1,c+1,n,m):
        matrix[r+1][c+1] = '.'
        s.append([r+1,c+1])

print("ah",total_count)

