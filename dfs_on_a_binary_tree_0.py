#
# Torbert, 6.29.2009
#
# Binary tree depth-first search example, Version 1.0
#
# Graph search on a tree, familiar case for recursion w/ left-right children.
#

class Node:
	# constructor
	def __init__(self,value,lt=None,rt=None):
		self.val=value
		self.left=lt
		self.right=rt
	# note that Java's implicit argument is passed explicitly in Python
	def display(self,lev=0):
		if self.right!=None:
			self.right.display(lev+1)	
		for k in xrange(lev):
			print '\t',
		print '----',
		print self.val
		if self.left!=None:
			self.left.display(lev+1)	

def search(t,target):
	if t==None:
		return False # dead end

	print 'Trying:',t.val

	if t.val==target: # hooray, we found it!!
		return True
	elif search(t.left,target):
		return True
	elif search(t.right,target):
		return True
	else:
		print '   Backtracking...',t.val
		return False

def main():
	a=Node('cop',Node('cob'),Node('top'))
	b=Node('lap',Node('lad'),Node('lip'))
	c=Node('cap',a,b)
	a=Node('rat',Node('mat'),Node('rot'))
	b=Node('run',Node('fun'),Node('rug'))
	root=Node('can',c,Node('ran',a,b))
	
	print
	root.display()
	print
	
	search(root,'rot')
	print
	print 'Now how do you construct the path?'
	print

main()

#
# Notes
# -----
# Output:
# 
#                         ---- rug
#                 ---- run
#                         ---- fun
#         ---- ran
#                         ---- rot
#                 ---- rat
#                         ---- mat
# ---- can
#                         ---- lip
#                 ---- lap
#                         ---- lad
#         ---- cap
#                         ---- top
#                 ---- cop
#                         ---- cob
# 
# Trying: can
# Trying: cap
# Trying: cop
# Trying: cob
#    Backtracking... cob
# Trying: top
#    Backtracking... top
#    Backtracking... cop
# Trying: lap
# Trying: lad
#    Backtracking... lad
# Trying: lip
#    Backtracking... lip
#    Backtracking... lap
#    Backtracking... cap
# Trying: ran
# Trying: rat
# Trying: mat
#    Backtracking... mat
# Trying: rot
# 
# Now how do you construct the path?
# 
