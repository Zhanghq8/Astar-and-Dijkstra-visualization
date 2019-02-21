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
- tkinter package(https://wiki.python.org/moin/TkInter)

## Description   
1.A* algorithm  
- [astar.py].    

2.Dijkstra
- [dijkstra].

3.Maze or map
- The maze or map is [xxx.txt] file, you can modify it and create a new one(with 0 or 1) to check different results .

## Run
1.Activate your KInect2 device by running `roslaunch kinect2_bridge kinect2_bridge.launch`.   
2.For [Object detection by color filtering]:
- First run `rosrun kinect2_viewer color_test` to tune the HSV value to get the desired result;
- Substitute the HSV value in [pose_color.cpp] with the new one;
- Do `catkin_make` in your workspace and then run `rosrun kinect2_viewer pose_color`.   

3.For [Object detection by loud filtering]:
- First substitute the depth range for your goal;
- Do `catkin_make` in your workspace and then run `rosrun kinect2_viewer pose_cloud`.

## Screenshots

Here are some screenshots of the results for this project:    
- For [Object detection by color filtering]:   
![color_test image](https://github.com/Zhanghq8/Kinect2-object-detection/blob/master/color_test.png)
![pose_color1 image](https://github.com/Zhanghq8/Kinect2-object-detection/blob/master/pose_color1.png)   
![pose_color2 image](https://github.com/Zhanghq8/Kinect2-object-detection/blob/master/pose_color2.png)   
- For [Object detection by cloud filtering]:   
![pose_cloud image](https://github.com/Zhanghq8/Kinect2-object-detection/blob/master/pose_cloud.png)
