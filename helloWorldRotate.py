import cluster
import random
import tkinter
from tkinter import *
import math
import time
#helloworld = [[0,0],[0,0.1],[0.1,0.1],[0.1,0], [0.2,0],[0.2,0.3],[0.3,0.3],[0.3,0.2], [0,0.2],[0,0.3],[0.1,0.3],[0.1,0.2]]
helloworld = []
colors = ["red","blue","green","cyan","brown","black","crimson"]
rg = 60
width = 1000
height = 1000
scale = 25
radius = 4
for z in range(300):
	xyz = [random.random()*rg +width/2 - rg/2,random.random()*rg +height/2 -rg,random.random()*rg*2 +height/2 - rg/2]
	helloworld.append(xyz)
master = Tk()
w = Canvas(master, width=width, height=height)
w.pack()

ex = cluster.cluster()
ex.group(helloworld,5,30)

t = 0
#length = sqrt(y*y +z*z)
while t < 25:
	count = 0
	for points in helloworld:
		radius = 3
		color = colors[ex.groupNums[count]]
		rv = [points[0] - width/2, points[1] - height/2, points[2] - height/2]
		r = math.sqrt(rv[1]*rv[1] + rv[2]*rv[2])
		if r == 0:
			phase = 0
		else:
			arc = (rv[1])/r;
			phase = math.acos(arc)
		y = r*math.sin(t + phase) + height/2

		w.create_oval(points[0] - radius, y - radius, points[0] + radius, y + radius, fill=color)
		count = count + 1
	t = t + 0.01
	w.update()
	time.sleep(0.01)
	
	w.delete("all")
radius = 10

j = 0
for f in range(ex.gn):
	x = 0
	for k in range(ex.rn):
		g = ex.trend[k][f]
		w.create_oval(scale*g[0] - radius,scale*g[1] - radius,scale*g[0] + radius,scale*g[1] + radius, fill="red")
		if x != 0:
			w.create_line(scale*prevX, scale*prevY, scale*g[0], scale*g[1], fill="red")
		prevX = g[0]
		prevY = g[1]
		x = x + 1
	j = j+1
