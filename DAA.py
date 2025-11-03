from queue import Queue 
grid = [ ] 

with open("DAA.txt") as f:
    for row,line in enumerate (f.read().splitlines()):
        rolex = [ ]
        for col,char in enumerate(line):
            if char == '#':
                rolex.append(1)
            elif char == '.':
                 rolex.append(0)
            else:
                rolex.append(char)
                if char == 'S':
                    start = row,col
        grid.append(rolex)            
                      
#parsing logic 
visited = set( )
q_ = Queue( )

q_.put((start,0))

while not q_.empty( ):
    node = q_.get( )
    (r,c), steps = node
    visited.add( (r,c) )
    for i,j in [(r+1,c),(r-1,c ),(r,c+1 ),(r,c-1)]:
        if i < 0 or j < 0:
            continue
        if grid[i][j] == 1:
            continue
        if (i,j) in visited:
            continue
        if grid[i][j] == 'E':
            print(steps)
            break
        q_.put( ( (i,j),steps+1) )

    

