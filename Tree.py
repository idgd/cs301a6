from Node import Node

class Tree:
	def __init__(self,root):
		self.root = Node(root)

	def add(self,node,parent):
		if search(parent,self):
			return(True)
		else:
			print("error: parent not found")
			return(False)

	def search(self,node,tree):
		n = tree.root

		if n.data == node:
			return(True)

		while n.relatives:
			if node in n.relatives:
				return(True)
			for f in n.relatives:
				search(node,f)

		return(False)
