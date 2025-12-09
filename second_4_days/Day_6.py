# Part 0: parse input
lines = []
file_name = 'ex.txt'
with open(file_name, 'r') as f:
    lines = [line.strip().split() for line in f]
    

n = len(lines[0])
operations = lines[len(lines)-1]
total_sum = 0
for i in range(n):
    operation = operations[i]
    cur_sum = 0
    for j in range(len(lines)-1):
        if j == 0:
            cur_sum = int(lines[j][i])
        else:
            if operation == "*":
                cur_sum *= int(lines[j][i])
            elif operation == "+":
                cur_sum += int(lines[j][i])
    total_sum += cur_sum
print(total_sum)

# Part II: indentation matters

# Part 0: parse input
lines = []
file_name = 'ex.txt'
with open(file_name, 'r') as f:
    lines = [line.replace('\n','') for line in f]
    
# maybe read in input in a different way?
# check if index i is all spaces, if so add amount
# if index i is not all spaces and operation at i is not empty
# keep track of operation and begin operation
# else create the digit and do operation on current
lines = []
file_name = 'ex.txt'
with open(file_name, 'r') as f:
    lines = [line.replace('\n','') for line in f]

operations = lines[len(lines)-1]
lines = lines[:len(lines)-1]
n = len(lines[0])
m = len(lines)

operation = ""
total_sum = 0
cur_sum = 0
for i in range(n):
    f = 0
    digits = ""
    for j in range(m):
        if lines[j][i] != " ":
            f = 1
            digits += lines[j][i]
    if f == 1:
        if i < len(operations) and operations[i] != " ":
            operation = operations[i]
            cur_sum = int(digits)
        else:
            if operation == "+":
                cur_sum += int(digits)
            elif operation == "*":
                cur_sum *= int(digits)
    else:
        total_sum += cur_sum
        cur_sum = 0
    if i+1 == n:
        total_sum += cur_sum
print(total_sum)


    


