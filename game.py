import time
from os import system, name
row = col = 75
grid = [[" "]*col for _ in range(col)]

#uncomment for Toad
grid[2][2] = grid[2][3] = grid[2][4] = grid[2][4] =grid[3][1] =grid[3][2] = grid[3][3] = "*"

#uncomment for glider
#grid[2][0] = grid[3][1] = grid[3][2] = grid[2][2] =grid[1][2] = "*"

#uncomment for glider
grid[10][23] = grid[10][24] = grid[10][26] = grid[10][27] =grid[10][28] =grid[10][29] = grid[10][31] = grid[10][32] = "*"
grid[9][25] = grid[9][30] = grid[11][25] = grid[11][30] = "*"
def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')
def get_alive_neigbours(index,grid):
    l = 0
    index = [index[0]-1,index[1]-1]
    for i in range(index[0],index[0]+3):
        for j in range(index[1],index[1]+3):
            if(row>i>=0 and 0<=j<col):
                if((i!=index[0]+1 or j!=index[1]+1) and grid[i][j] == "*"):
                    l = l+1 
    return l
while(True):
    temp_grid = []
    for i in range(0,row):
        t =[]
        for j in range(0,col):
            num = get_alive_neigbours([i,j],grid)
            if(num==3):
                t.append("*")
            elif(num<2 or num>3):
                t.append(" ")
            else:   
                t.append(grid[i][j])
            print(t[j],end="")
        temp_grid.append(t)
        print()
    grid = temp_grid.copy()
    time.sleep(0.5)
    clear()