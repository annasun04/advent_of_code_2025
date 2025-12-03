# Part 0: parse input
lines = []
file_name = 'ex.txt'
with open(file_name, 'r') as f:
    lines = f.read()
    
lines = lines.split(",")

# Part 1:
# given an input of ranges
# an invalid id is an id that is
# 2A where A is a subsequence of numbers
# return the sum of all invalid ids
total = 0
def is_subseq(s:str):
    # subsequence of 1 all the way to n/2
    for i in range(1, (len(s)//2)+1):
        item_set = set()
        for j in range(0, len(s), i):
            temp = s[j:j+i]
            item_set.add(temp)

        if len(item_set) == 1:
            return True

    return False



for line in lines:
    curRange = line.split("-")

    l = int(curRange[0])
    u = int(curRange[1])
    for i in range(l,u+1):
        id = str(i)
        is_invalid = is_subseq(id)
        if is_invalid:
            print("invalid ", i )
            total+=i

print(total)
# Part 2:
