import cluster
import random
import tkinter
from tkinter import *
helloworld = [[0,0],[0,0.1],[0.1,0.1],[0.1,0], [0.2,0],[0.2,0.3],[0.3,0.3],[0.3,0.2], [0,0.2],[0,0.3],[0.1,0.3],[0.1,0.2]]


ex = cluster.cluster()
ex.group(helloworld,3,3)
