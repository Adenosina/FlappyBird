
from graphics import *
from random import *

class stars:
	
	def __init__(self,win):
		self.starsxlist, self.starsylist, self.starlist = [], [], []
		self.starsxlist = [97, 486, 608, 629, 574, 772, 413, 665, 1019,
		 1042, 56, 663, 911, 874, 481, 843, 565, 898, 827, 167]
		self.starsylist = [73, 468, 430, 726, 747, 82, 331, 66, 128,
		 543, 321, 867, 956, 495, 524, 194, 201, 870, 879, 1056]
		for i in range(0,20):
			self.star = Circle(Point(self.starsxlist[i],self.starsylist[i]),2)
			self.star.setFill("white")
			self.starlist.append(self.star)
		for i in self.starlist:
			i.draw(win)
	
	def getvalues(self):
		return self.starsxlist
		
	def getvalues2(self):	
		return self.starsylist
		
