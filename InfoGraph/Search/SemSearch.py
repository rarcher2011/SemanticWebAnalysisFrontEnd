import os
import bintrees


class rbt:	
	def __init__(self):
		self.RBT = bintrees.RBTree()
	def buildTree(self,mydir):
		thisdir = os.listdir(mydir)
		for f in thisdir:
			local = ""
			if(mydir[len(local)-1]=="/"):
				local = mydir+f
			else:
				local = mydir+"/"+f	
			self.RBT.insert(f, local)
	def find(self,val):
		myval = self.RBT.get(val)
		return myval
	def items(self):
		return self.RBT.items()
