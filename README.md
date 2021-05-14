# Clustering
![image](https://user-images.githubusercontent.com/77860196/118322396-0cbde900-b4cd-11eb-9701-d3476619f992.png)

[HelloWorld.py -- grouping 2D vectors]

![image](https://user-images.githubusercontent.com/77860196/118322575-5c9cb000-b4cd-11eb-9bc0-b334eb6b28a8.png)

[HelloWorldRotate.py -- grouping 3D vectors]

Algorithm:
Groups N dimensional vectors with a specified number of groups.
-Starts groups at random positions, assigns closest vectors to each group.
-Finds center of each group by averaging each vector. Uses each average vector as the new group center. 
-Repeat R times until decent group centers are found.
