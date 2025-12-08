# Part 0: parse input
lines = []
file_name = 'ex.txt'
with open(file_name, 'r') as f:
    lines = [line.strip().split(",") for line in f]

#print(lines)
# Part 1: 
# new array with ["distance", "p1","p2" ]
# making 10 shortest connects
# 11 circuits
# multiply the sizes of the 3 largest circuits
# Union Find
class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))  # Each node is its own parent initially
        self.size = [1] * n  # Each set has size 1 initially
        self.max_size = 1
    
    def find(self, x):
        # Find root with path compression
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        # Union by size
        root_x = self.find(x)
        root_y = self.find(y)
        
        if root_x == root_y:
            return False  # Already in same set
        
        # Attach smaller tree under larger tree
        if self.size[root_x] < self.size[root_y]:
            self.parent[root_x] = root_y
            self.size[root_y] += self.size[root_x]
            self.max_size = max(self.max_size, self.size[root_y])
        else:
            self.parent[root_y] = root_x
            self.size[root_x] += self.size[root_y]
            self.max_size = max(self.max_size, self.size[root_x])
        
        return True  # Successfully merged
    




import math
dist = []
for i in range(len(lines)):
    for j in range(i+1,len(lines)):
        c1 = lines[i]
        c2 = lines[j]
        euclid = math.sqrt((int(c2[0])- int(c1[0]))**2 + (int(c2[1])- int(c1[1]))**2 + (int(c2[2])- int(c1[2]))**2)
        dist.append([euclid, i, j])
dist.sort(key=lambda x:x[0])
uf = UnionFind(len(lines))

target = len(lines)-1
sol = 0
for i in range(len(dist)):
    d, i1, i2 = dist[i]
    
    if uf.max_size == target:
        res = uf.union(i1,i2)
        if res:
            v1 = lines[i1]
            print("vi", v1)
            sol = int(v1[0])
            v2 = lines[i2]
            print("v2", v2)
            sol *= int(v2[0])
    else:
        res = uf.union(i1,i2)


print(sol)
