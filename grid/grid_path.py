from functools import wraps


grid = lambda X,Y: [[(x,y) for x in range(X+1)] for y in range(Y+1)]
cache = {}
def paths(s,e,grid,holes):
    if s in cache:
        return cache[s]
    i,j = s
    x,y = e
    if i == x and j == y:
        cache[s] = 1
    elif any((i<0,j<0,i>=len(grid[0]),j>=len(grid))) or s in holes:
        cache[s] = 0
    else:
        cache[s] = paths((i+1,j),e,grid,holes) + paths((i,j+1),e,grid,holes)
    return cache[s]
print(paths((0,0),(5,10),grid(5,10),[(2,4),(4,4),(1,3)]))
