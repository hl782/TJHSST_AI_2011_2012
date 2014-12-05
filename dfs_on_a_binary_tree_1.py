#
# Torbert, 6.29.2009
#
# Binary tree depth-first search example, Version 1.1
#
# Graph search on a tree, familiar case for recursion w/ left-right children.
#
# This version uses adjacency list (hash table) instead of building the tree.
#

def display(w,ht,lev=0):
	if w=='***': # bottom of tree
		return

	display(ht[w][1],ht,lev+1)	# right child

	for k in xrange(lev):
		print '\t',
	print '----',
	print w

	display(ht[w][0],ht,lev+1)	# left child

def search(w,target,ht):
	if w=='***':
		return False # dead end

	print 'Trying:',w

	if w==target: # hooray, we found it!!
		return True
	elif search(ht[w][0],target,ht):
		return True
	elif search(ht[w][1],target,ht):
		return True
	else:
		print '   Backtracking...',w
		return False

def main():
	#
	# NOTE: in this formulation the "links" are only in one direction
	#
	ht={}
	ht['can']=['cap','ran'] # root node of our search
	ht['cap']=['cop','lap']
	ht['cop']=['cob','top']
	ht['lap']=['lad','lip']
	ht['ran']=['rat','run']
	ht['rat']=['mat','rot']
	ht['run']=['fun','rug']
	ht['cob']=['***','***'] # leaves, bogus "null" value is ***
	ht['top']=['***','***']
	ht['lad']=['***','***']
	ht['lip']=['***','***']
	ht['mat']=['***','***']
	ht['rot']=['***','***']
	ht['fun']=['***','***']
	ht['rug']=['***','***']
	
	print
	display('can',ht)
	print
	
	search('can','rot',ht)
	k=1
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
