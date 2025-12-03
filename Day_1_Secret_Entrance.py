# PART 0: parse input
lines = []
# 'Day_1_input''day_1_ex.txt' #
file_name = 'Day_1_input.txt'
with open(file_name, 'r') as f:
    lines = [line.strip() for line in f]

# PART I:
# 0-99
# left (lower numbers)
# right (towards higer numbers)
# dial starts at 50
# return number of times the dial is
# left pointing at 0 after any rotation

# if RXX,
    # curr + XX
    # if curr+XX > 99
# if LXX
    # curr - XX
    # if positive do nothing
    # if negative 99-(curr-x)
    # if 0
count = 0
dial = 50
for line in lines:
    direction = line[0]
    distance = int(line[1:])
    if direction == "R":
        dial = (dial + (distance%100))%100
    else:
        dial = dial - ((distance)%100)
        if dial < 0:
            dial = 100+dial
    if dial == 0:
        count+=1
    # print(dial)
print("part 1 count ", count)


# Part II:
# new password method
# count number of times any click causes
# dial to point at 0
# so any time it lands or passes 0
count = 0
dial = 50
for line in lines:
    direction = line[0]
    distance = int(line[1:])
    if direction == "R":
        count += (dial + distance)//100
        dial = (dial + distance)%100
    else:
        
        count += (distance - dial +99)//100
        dial = (dial - distance)%100
    if dial == 0:
        count+=1

print("part 2 count:", count)
pos = 50
count = 0

for line in lines:
    d = line[0]
    n = int(line[1:])

    if d == 'R':
        # how many times we hit 0 while moving right
        crosses = (pos + n) // 100
        pos = (pos + n) % 100
    else:  # 'L'
        # offset = distance from pos up to next 0 when moving right
        offset = (100 - pos) % 100
        # how many times we hit 0 while moving left
        crosses = (n + offset) // 100
        pos = (pos - n) % 100

    count += crosses

print(count) 