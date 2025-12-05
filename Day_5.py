# Part 0: parse input
filename = 'ex.txt'
lines = []
ranges = []
with open(filename, 'r') as f:
    lines = f.read().strip().split('\n')
blank_indx = lines.index('')

for line in lines[:blank_indx]:
    start,end = line.split('-')
    ranges.append([int(start), int(end)])

ingredients = []
for line in lines[blank_indx+1:]:
    ingredients.append(int(line))


# Part I: 
# list of fresh ingredient id ranges
# ingredient ids
# merging intervals
ranges.sort()
#print(ranges)
#print(ingredients)
merged_ranges = []
l = ranges[0][0]
r = ranges[0][1]
for i in range(1,len(ranges)):
    cur = ranges[i]
    

    if cur[0] <= r:
        r = max(cur[1],r)
    else:
        merged_ranges.append([l,r])
        l = cur[0]
        r = cur[1]
    if i+1 == len(ranges):
        merged_ranges.append([l,r])
        break
#print(merged_ranges)

total_count = 0
for i in range(len(ingredients)):
    for j in range(len(merged_ranges)):
        if ingredients[i] >= merged_ranges[j][0] and ingredients[i] <= merged_ranges[j][1]:
            total_count +=1
# print(total_count)




# Part II:
total_count = 0
for i in range(len(merged_ranges)):
    total_count += merged_ranges[i][1]- merged_ranges[i][0] + 1

print(total_count)