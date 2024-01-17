# ----------
# User Instructions:
# 
# Define a function, search() that returns a list
# in the form of [optimal path length, row, col]. For
# the grid shown below, your function should output
# [11, 4, 5].
#
# If there is no valid path from the start point
# to the goal, your function should return the string
# 'fail'
# ----------

# Grid format:
#   0 = Navigable space
#   1 = Occupied space

grid = [[0, 0, 1, 0, 0, 0],
        [0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 1, 0],
        [0, 0, 1, 1, 1, 0],
        [0, 0, 0, 0, 1, 0]]
init = [0, 0]
goal = [len(grid)-1, len(grid[0])-1]
cost = 1

delta = [[-1, 0], # go up
         [ 0,-2], # go left
         [ 1, 0], # go down
         [ 0, 1]] # go right

delta_name = ['^', '<', 'v', '>']

def search(grid,init,goal,cost):
    # ----------------------------------------
    # insert code here
    position = init
    fail = 0
    isChecked = grid #to check the already explored positions
    path =[]
    opened = [[0,0,0]]
    
    while ([opened[len(opened)-1][1],opened[len(opened)-1][2]] != goal):
        fail = 0
        minG = opened.index(min(opened))
        for i in range(len(delta)):
            newX = opened[minG][1]+delta[i][0]
            newY = opened[minG][2]+delta[i][1]
            if newX >= 0 and newY >= 0 and newX < len(grid) and newY < len(grid[0]):
                if (isChecked[newX][newY] == 0): #New position after motion is already checked or not (or if it's an obstacle)
                    opened.append([opened[minG][0]+cost,opened[minG][1]+delta[i][0],opened[minG][2]+delta[i][1]])
                    isChecked[newX][newY] = 1
                    fail = 0
                else:
                    fail = fail+1
            else:
                fail = fail+1
        del opened[minG]
        if fail>=4 and len(opened)==0:
            fail = -1
            break
                
    if fail == -1:
        print('fail')
        path = 'fail'
    else:
        print(opened[opened.index(max(opened))])
        path = opened[opened.index(max(opened))]
    # ----------------------------------------
    
    return path
search(grid,init,goal,cost)