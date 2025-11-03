grid = []


with open("DAA.txt") as f:
    for row,line in enumerate (f.read().splitlines()):
        rolex = []
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
                      
