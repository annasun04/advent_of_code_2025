# Part 0: parse input
filename = 'ex.txt'
lines = []
with open(filename, 'r') as f:
    lines = [line.strip() for line in f]

# Part I: 
# list of digits 1-9
# each line of digits 
# corresponds to a "bank"
# each bank turn on exactly 2 batteries
# and the concatenation will be the bank's
# "joltage"
# find largest possible joltage for each bank
# total output is the sum of
# each bank's joltages

# 2 pointer approach
# if r is > l, l = r (ones place becomes the tens place)
# else continue. keep track of largest

total = 0
for line in lines:
    max_amount = 0
    l = 0
    r = 1
    if len(line) == 1:
        total += int(line)
    elif len(line) > 1:
        while r < len(line):
            tens = line[l]
            ones = line[r]
            cur = int((tens+ones))
            if cur > max_amount:
                max_amount = cur
            if int(ones) > int(tens):
                l = r
                r+=1
            else:
                r+=1

    total+= max_amount

# print(total)

# Part II:
# get the max i from 0-len(line)-12
# get the max from i+1 to len(line)-11
# ...
# get the max from k+1 to len(line)-1
total = 0
#lines = ["234234234234278"]
for line in lines:
    last_indx = -1
    joltage = ""
    for d in range(12,-1,-1):
        max_digit = 0
        cur_digit= 0
        temp = last_indx
        # print("indx after prev", temp+1)
        for i in range(temp+1,len(line)-d+1):
            if i != len(line):
                cur_digit = int(line[i])
                if cur_digit > max_digit:
                    last_indx = i
                    # print("new max", cur_digit, " for digit", 12-d+1)
                    max_digit = cur_digit
            else:
                max_digit = 0
        if max_digit != 0:
            joltage += str(max_digit)
    # print(joltage)
    total += int(joltage)

print(total)






    # first digit
    # second digit
    # thrid digit
    # 4th digit