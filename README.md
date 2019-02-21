# Astar-and-Dijkstra-visualization     
## Maintainer
- [Hanqing Zhang], <<hzhang8@wpi.edu>>, WPI   
*Note: The pseudo code used in this project is based on Coursera robotic course, and the visualization code template comes from motion planning course(RBE550) of WPI*    
## Read this first
- .

## Dependencies

- ROS Kinetic
- Ubuntu 16.04
- Python 3(Python 2)
- Tkinter package(https://wiki.python.org/moin/TkInter)

## Description   
1.A* algorithm  
- [astar.py].    

2.Dijkstra
- [dijkstra].

3.Maze or map
- The maze or map is [xxx.txt] file, you can modify it and create a new one(with '0' or '1') to check different results.
- A basic map looks like this:
![map](https://github.com/Zhanghq8/Astar-and-Dijkstra-visualization/blob/master/normalmap.txt), where '0' means free space, and '1' means obstacle space.

## Run
1.Install [tkinter]:
- Run `sudo apt-get install python-tk python3-tk`.   
2.For [Astar]:
- Run `python astar.py`.
3.For [Dijkstra]:
- Run `python dijkstra.py`.
4.To use your map:
- Create a new txt file, and customize your own using '0' and '1'.
- Substitute the file name with the one you created into this line.
`with open("failedmap.txt") as text:`   
5.To change the start and goal node:
- Modify these lines below:
`entrance_node = (row - 4, 1)`   
`exit_node = (row - 6, col - 2)`   
6.To obtain a roughly time cost, you need to commit some lines to avoid unnecessary time cost(visualization) as guided in the code.

## Screenshots

Here are some screenshots of the results for this project:    
- For [maze]:   
![maze case for astar](https://github.com/Zhanghq8/Astar-and-Dijkstra-visualization/blob/master/maze%20case%20for%20astar.png)
![maze case for dijkstra](https://github.com/Zhanghq8/Astar-and-Dijkstra-visualization/blob/master/maze%20case%20for%20dijkstra.png)   
- For [map]:   
![map case for astar](https://github.com/Zhanghq8/Astar-and-Dijkstra-visualization/blob/master/normal%20case%20for%20astar.png)
![map case for dijkstra](https://github.com/Zhanghq8/Astar-and-Dijkstra-visualization/blob/master/normalmap%20case%20for%20dijkstra.png)
- For [failed case]
![no path case for star](https://github.com/Zhanghq8/Astar-and-Dijkstra-visualization/blob/master/failedmap%20for%20astar.png)
![no path case for dijkstra](https://github.com/Zhanghq8/Astar-and-Dijkstra-visualization/blob/master/failed%20case%20for%20dijkstra.png)


