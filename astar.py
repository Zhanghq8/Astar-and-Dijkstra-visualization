## A* Algorithm implement and visualization

# import libraries
from sys import version_info

if version_info.major == 2:
    # We are using Python 2.x
    from Tkinter import *
    import ttk
elif version_info.major == 3:
    # We are using Python 3.x
    from tkinter import *
    from tkinter import ttk

import time as t
import numpy as np
import math

'''
Define the color scheme for visualization. You may change it but I recommend using the same colors
'''
# white (0) is an unvisited node, black(1) is a wall, blue(2) is a visited node
# yellow(3) is for start node, green(4) is for exit node, red (5) is a node on the completed path
# orange(6) is for current node, purple(7) is for on list node
colors = {5: "red", 4: "green", 3: "yellow", 2: "blue", 1: "black", 0: "white", 6: "orange", 7: "purple"}

'''
Opens the maze file and creates tkinter GUI object
'''
# load maze or map
with open("./map/normalmap.txt") as text:
    maze = [list(line.strip()) for line in text]
[col, row] = np.shape(maze)

# create map
root = Tk()
size = 800 / row
canvas = Canvas(root, width=(size * row), height=(size * col))
root.title("A* Algorithm")


def draw_canvas(canvas, maze):
    '''
    Change this according to the data structure of your maze variable.
    If you are using a node class like the one mentioned below,
    You may have to change fill=colors[int(maze[i][j])] to fill=colors[int(maze[i][j].color)]
    '''
    for i in range(0, col):
        for j in range(0, row):
            canvas.create_rectangle(j * size, i * size, (j + 1) * size, (i + 1) * size, fill=colors[int(maze[i][j])])
    canvas.pack()


def a_star(maze, start_node, exit_node):
    '''
    Visualize the map. Use these functions to visualize your maze.
    '''

    # This visualizes the grid. You may remove this and use the functions as you wish.
    maze[start_node[0]][start_node[1]] = '3'
    maze[exit_node[0]][exit_node[1]] = '4'
    draw_canvas(canvas, maze)
    root.update()

    # -------------------------------------------YOUR CODE HERE--------------------------------------------------
    row, col = np.shape(maze)

    # Initialize node parent list to store previous node
    parent_mat = np.zeros((row, col))

    # Define coordinates
    x_tmp = np.linspace(0, col - 1, col)
    y_tmp = np.linspace(0, row - 1, row)
    xh, yh = np.meshgrid(x_tmp, y_tmp)

    # Define start and goal node coordinates
    xd = exit_node[1]
    yd = exit_node[0]
    # xs = start_node[1]
    # ys = start_node[0]

    # Define Heuristic cost for each node
    H = np.sqrt(np.square(xh - xd) + np.square(yh - yd))  # Euclidean distance as heuristic function
    # H = abs(xh - xd) + abs(yh - yd) # Manhatten distance as heuristic function

    # Initialize cost arrays
    f = np.full((row, col), 9999999)
    g = np.full((row, col), 9999999)

    # Add start node to the f,g matrix
    g[start_node[0]][start_node[1]] = 0
    f[start_node[0]][start_node[1]] = H[start_node[0]][start_node[1]]

    # keep track of the number of nodes that are expanded
    numExpanded = 0

    while (True):
        '''
        Comment the following 4 lines if you want to ignore the searching process
        and compute the time cost 
        '''
        maze[start_node[0]][start_node[1]] = '3'
        maze[exit_node[0]][exit_node[1]] = '4'
        draw_canvas(canvas, maze)
        root.update()

        # Find the node with the minimum f value
        min_f = np.min(f)
        cn_list = np.where(f == np.min(f))
        cn_list0 = cn_list[0].flatten()
        cn_list1 = cn_list[1].flatten()
        list = []
        for i in range(len(cn_list0)):
            tmp = cn_list1[i] * row + cn_list0[i] + 1
            list.append(tmp)
        index = np.argmin(list, axis=0)
        current_node = (cn_list[0][index], cn_list[1][index])
        parent_index = cn_list1[index] * row + cn_list0[index]

        if current_node == exit_node:
            break
        if min_f == 9999999:
            print("No path exist from start to goal.")
            return
        xc = int(current_node[1])
        yc = int(current_node[0])
        # change current node state as visited
        maze[yc][xc] = '2'
        f[yc][xc] = 9999999

        # Visit all of the neighbors around the current node and update the
        # entries in the map, f, g and parent arrays

        if (yc - 1) >= 0:
            north_node = (yc - 1, xc)
        else:
            north_node = (yc, xc)
        if (yc + 1) <= row - 1:
            south_node = (yc + 1, xc)
        else:
            south_node = (yc, xc)
        if (xc + 1) <= col - 1:
            east_node = (yc, xc + 1)
        else:
            east_node = (yc, xc)
        if (xc - 1) >= 0:
            west_node = (yc, xc - 1)
        else:
            west_node = (yc, xc)

        adjacent_nodes = [north_node, south_node, east_node, west_node]
        for nums in range(4):
            ad_node = adjacent_nodes[nums]
            # we only visit the adjacent node which is unvisited or exit or nodes on the visiting list
            if maze[ad_node[0]][ad_node[1]] == '0' or maze[ad_node[0]][ad_node[1]] == '7' or maze[ad_node[0]][
                ad_node[1]] == '4':
                if g[ad_node[0]][ad_node[1]] > g[yc][xc] + 1:
                    g[ad_node[0]][ad_node[1]] = g[yc][xc] + 1
                    f[ad_node[0]][ad_node[1]] = g[ad_node[0]][ad_node[1]] + H[ad_node[0]][ad_node[1]]
                    # add the parent node(current node) for adjacent node
                    parent_mat[ad_node[0]][ad_node[1]] = parent_index
                    # change the node state to on lists
                    maze[ad_node[0]][ad_node[1]] = '7'
        numExpanded = numExpanded + 1
    parent_list = parent_mat.flatten('F')
    route = []
    route = [exit_node[1] * row + exit_node[0]]
    while route[-1] != 0:
        route.append(int(parent_list[route[-1]]))
    path = []
    for i in range(len(route)):
        if i > 0 and i < len(route) - 2:
            path.append((route[i]))
    path.reverse()
    result_list = []
    # change the color state to show the complete path
    for i in range(len(path)):
        path_row = (path[i] % row)
        path_col = int(path[i] / row)
        maze[path_row][path_col] = '5'
        result_list.append((path_row, path_col))
    print("The complete path:", (start_node[0], start_node[1]), result_list, (exit_node[0], exit_node[1]))
    maze[start_node[0]][start_node[1]] = '3'
    maze[exit_node[0]][exit_node[1]] = '4'
    draw_canvas(canvas, maze)
    root.update()
    print("Expanded nodes number: ", numExpanded)
    return


def main():
    '''
    Define start and goal node. You may change how to define the nodes.
    '''
    entrance_node = (row - 4, 1)
    exit_node = (2, col - 2)

    '''
    Run your ana_star algorithm function. You may choose to change the function or not use it.
    Uncomment the t1, t2, and print lines below if you want to compute the time cost
    '''
    # run the  algorithm
    # t1 = t.time()
    a_star(maze, entrance_node, exit_node)
    # t2 = t.time()
    # print ("Total time cost:", t2-t1)

    root.mainloop()


if __name__ == '__main__':
    main()