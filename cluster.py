import random
import math
import numpy
import multiprocessing as mp
#this class doubles as a vectors class, use arrays of arrays as inputs but think of them more like arrays of vectors
#the functions add, dist, and mult are used to add arrays, multiply arrays by a constant, or find the distance between 2 arrays
class cluster:

	def insert(self,v):
		#check which group a new vector might belong in
		#this is faster than regrouping the entire set of data each time
		closest_dist = math.inf
		h = 0
		for x in self.centers:
			current_dist = dist(v,x)
			if current_dist < closest_dist:
				closest_dist = current_dist
				group = h
			h = h+1
		return group

	def group(self,inp,groupCount,rounds):

		self.gn = groupCount
		self.rn = rounds
		self.inp = inp
		self.centers = []
		self.groupNums = []
		self.trend = []
		#get initial group centers
		prev = -1;
		x = 0
		d = numpy.zeros(self.gn)
		for g in range(self.gn):
			a = True
			#this part chooses random numbers until it finds one that isn't in the array d
			while(a):
				#this part needs refactoring, if i could automatically exclude past randoms from the RNG that'd be fukin great
				a = False
				f = random.randint(0,len(self.inp) - 1)
				for p in d:
					if f == p:
						a = True

			d[x] = f
			self.centers.append(self.inp[f])
			x = x + 1

		#start rounds
		for r in range(self.rn):
			total = []
			if r != 0:
				self.groupNums = []
			for v in self.inp:
				#for each vector in the input array, find the closest group vector
				closest_dist = math.inf #avoids setting the closest to the 1st group vector
				h = -1
				j = 0

				for g in self.centers:
					current_dist = self.dist(v,g)
					if current_dist < closest_dist:
						closest_dist = current_dist
						h = j
					j = j + 1
				self.groupNums.append(h)

			#find new centers
			#total = numpy.zeros(self.gn) #fill array with zeros
			for s in range(self.gn):
				total.append(numpy.zeros(len(self.inp[0])))
			l = numpy.zeros(self.gn) #this stores the length of each group
			for x in range(len(self.inp)):
				#add all vectors to each group total
				total[self.groupNums[x]] = self.add(total[self.groupNums[x]], self.inp[x])
				l[self.groupNums[x]] = l[self.groupNums[x]] + 1

			#find average for each group
			for t in range(len(total)):
				self.centers[t] = self.mult(total[t], 1/l[t])
			self.trend.append(self.centers) #used to graph how the centers change over each iteration
		
	def dist(self,v1,v2):
		#find distance between 2 arrays
		#v1 and v2 must be the same length
		resultant = 0
		for x in range(len(v1)):
			sub = v2[x] - v1[x]
			resultant += sub * sub
		resultant = math.sqrt(resultant)
		return resultant
		#magnitude = sqrt(x1^2 + x2^2 + x3^2 + ... + xn^2)

	def add(self,v1,v2):
		#add 2 arrays together
		result = numpy.zeros(len(v1))
		for x in range(len(v1)):
			result[x] = v1[x] + v2[x]
		return result


	def mult(self,v,c):
		#multiply an array by a constant
		result = []
		for x in range(len(v)):
			result.append(v[x] * c)
		return result

	

















