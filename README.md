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
- Run `python astar`.
3.For [Dijkstra]:
- Run `python dijkstra`.
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
- For [Object detection by color filtering]:   
![color_test image](https://github.com/Zhanghq8/Kinect2-object-detection/blob/master/color_test.png)
![pose_color1 image](https://github.com/Zhanghq8/Kinect2-object-detection/blob/master/pose_color1.png)   
![pose_color2 image](https://github.com/Zhanghq8/Kinect2-object-detection/blob/master/pose_color2.png)   
- For [Object detection by cloud filtering]:   
![pose_cloud image](https://github.com/Zhanghq8/Kinect2-object-detection/blob/master/pose_cloud.png)
