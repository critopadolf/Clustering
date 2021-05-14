#import cluster
import clusterParallel as clusterP
import cluster as cluster
import random
import tkinter
from tkinter import *
import pathos.multiprocessing as mp
import time

def main():
	#helloworld = [[0,0],[0,0.1],[0.1,0.1],[0.1,0], [0.2,0],[0.2,0.3],[0.3,0.3],[0.3,0.2], [0,0.2],[0,0.3],[0.1,0.3],[0.1,0.2]]
	helloworld = []
	colors = ["red","blue","green","cyan","brown","black","orange","lime","plum","navy","darkviolet"]
	'''
	colors = []
	for x in range(100):
		colors.append(colorsp[int(random.random()*len(colorsp))])
	'''
	for z in range(1000):
		xyz = [random.random()*30,random.random()*30]
		helloworld.append(xyz)
	master = Tk()
	width = 1000
	height = 1000
	scale = 25
	radius = 4
	w = Canvas(master, width=width, height=height)
	w.pack()

	ex = cluster.cluster()
	exP = clusterP.cluster()
	t = time.time()
	ex.group(helloworld,4,3)
	print(time.time() - t)
	t = time.time()
	exP.group(helloworld,4,3)
	print(time.time() - t)
	count = 0
	for points in helloworld:
		radius = 3
		color = colors[ex.groupNums[count]]
		w.create_oval(scale*points[0] - radius,scale*points[1] - radius,scale*points[0] + radius,scale*points[1] + radius, fill=color)
		count = count + 1
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
	mainloop()

if __name__ == '__main__':
	main()