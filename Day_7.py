# Part 0: parse input
lines = []
file_name = 'ex.txt'
with open(file_name, 'r') as f:
    lines = [list(line.strip()) for line in f]

#print(lines)
# Part 1: 
# number of times a beam of light is split
# ie. number of times directly above a ^, there is a |
# An array of size len(matrix) which keeps track of which
# indices are current beams

# for each line, if index i == ^, check above, if so, increment count
# and alter i-1 and i+1 if they are '.' update 
# array as i-1 = 1, i+1 = 1, i = 0

n = len(lines)
m = len(lines[0])
total_count = 0
arr = [0]*m
for i in range(n):
    for j in range(m):
        #print(lines)
        if lines[i][j] == "." and arr[j] == 1:
            lines[i][j] = "|"
           

        if lines[i][j] == "S":
            
            arr[j] = 1
        elif lines[i][j] == '^':
            if i > 0:
                if lines[i-1][j] == '|':
                    total_count+=1
                    arr[j] = 0
                    if j >0 and lines[i][j-1] == ".":
                        lines[i][j-1] = "|"
                        arr[j-1] = 1
                    if j < n-1 and lines[i][j+1] == ".":
                        lines[i][j+1] = "|"
                        arr[j+1] = 1

#print(total_count)       




