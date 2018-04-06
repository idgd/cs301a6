from Node import Node

class Tree:
	def __init__(self,root):
		self.root = Node(root)

	def add(self,node,index = None):
		if index:
			n = self.root
			for f in index[:-1]:
				n = n.relatives[f]
			n.relatives.insert(index[-1],Node(node))
		else:
			self.root.relatives.append(Node(node))
		

	def search(self,node,tree):
		n = tree

		if n.data == node:
			return(True)

		while n.relatives:
			if node in n.relatives:
				return(True)
			for f in n.relatives:
				self.search(node,f)

		return(False)

t = Tree("okay")
t.add("time")
t.add("for",[0,0])
t.add("lunch",[0,0,0])
t.add("breakfast",[0,0,1])
t.add("dinner",[0,0,2])
print(t.search("for",t.root))
