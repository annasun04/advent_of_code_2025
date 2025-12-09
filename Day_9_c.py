# Part 0: parse input
lines = []
file_name = 'ex.txt'
with open(file_name, 'r') as f:
    lines = [list(map(int, line.strip().split(","))) for line in f]

# The red tiles form a polygon in the order given
# Part 2: polygon is formed by connecting consecutive red tiles
# All points inside this polygon (and on the green connecting edges) are valid

def point_in_polygon(x, y, polygon):
    """
    Ray casting algorithm to check if point (x,y) is inside polygon.
    polygon is a list of [x, y] coordinates.
    Returns True if inside, False otherwise.
    """
    n = len(polygon)
    inside = False
    
    p1x, p1y = polygon[0]
    for i in range(1, n + 1):
        p2x, p2y = polygon[i % n]
        if y > min(p1y, p2y):
            if y <= max(p1y, p2y):
                if x <= max(p1x, p2x):
                    if p1y != p2y:
                        xinters = (y - p1y) * (p2x - p1x) / (p2y - p1y) + p1x
                    if p1x == p2x or x <= xinters:
                        inside = not inside
        p1x, p1y = p2x, p2y
    
    return inside

def is_on_polygon_edge(x, y, polygon):
    """
    Check if point (x,y) is on any edge of the polygon.
    Since consecutive tiles are connected horizontally or vertically,
    we just need to check if point is on the line segment between consecutive vertices.
    """
    n = len(polygon)
    for i in range(n):
        x1, y1 = polygon[i]
        x2, y2 = polygon[(i + 1) % n]
        
        # Check if point is on horizontal edge
        if y1 == y2 == y:
            if min(x1, x2) <= x <= max(x1, x2):
                return True
        
        # Check if point is on vertical edge
        if x1 == x2 == x:
            if min(y1, y2) <= y <= max(y1, y2):
                return True
    
    return False

def is_valid_point(x, y, polygon, red_tiles):
    """
    A point is valid if it's:
    1. A red tile (corner of polygon)
    2. On a green edge (connecting consecutive red tiles)
    3. Inside the polygon (green interior)
    """
    # Check if it's a red tile
    if (x, y) in red_tiles:
        return True
    
    # Check if it's on the polygon edge (green connecting tiles)
    if is_on_polygon_edge(x, y, polygon):
        return True
    
    # Check if it's inside the polygon (green interior)
    if point_in_polygon(x, y, polygon):
        return True
    
    return False

# Create polygon from red tiles (in order given)
polygon = [[x, y] for x, y in lines]
red_tiles = set((x, y) for x, y in lines)

# Cache for valid points
valid_cache = {}

def is_valid_cached(x, y):
    if (x, y) not in valid_cache:
        valid_cache[(x, y)] = is_valid_point(x, y, polygon, red_tiles)
    return valid_cache[(x, y)]

def find_rectangle_area(r1, c1, r2, c2):
    """
    Check if rectangle with corners at (c1,r1) and (c2,r2) is valid.
    All points in the rectangle must be red or green tiles.
    """
    min_r, max_r = min(r1, r2), max(r1, r2)
    min_c, max_c = min(c1, c2), max(c1, c2)
    
    # Check all points in rectangle
    for r in range(min_r, max_r + 1):
        for c in range(min_c, max_c + 1):
            if not is_valid_cached(c, r):
                return -1
    
    return (abs(r1 - r2) + 1) * (abs(c1 - c2) + 1)

# Find maximum rectangle area
max_area = 0
n = len(lines)

print(f"Total red tiles: {n}")
print(f"Total pairs to check: {n * (n - 1) // 2}")

# Check all pairs of red tiles as potential corners
checked = 0
for i in range(n):
    if i % 50 == 0:
        print(f"Processing tile {i}/{n}, current max: {max_area}")
    
    for j in range(i + 1, n):
        c1, r1 = lines[i]  # x, y
        c2, r2 = lines[j]  # x, y
        
        # Skip if this can't beat current max
        potential = (abs(r1 - r2) + 1) * (abs(c1 - c2) + 1)
        if potential <= max_area:
            continue
        
        area = find_rectangle_area(r1, c1, r2, c2)
        if area > max_area:
            max_area = area
            print(f"New max area: {max_area} (tiles {i} and {j})")
        
        checked += 1

print(f"\nChecked {checked} pairs")
print(f"Maximum rectangle area: {max_area}")