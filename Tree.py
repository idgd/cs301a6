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
		r = False

		if n.data == node:
			r = True
			return(r)

		while n.relatives:

			if node in n.relatives:
				r = True
				return(r)

			for f in n.relatives:
				n = f
				r = self.search(node,n)
				return(r)

		return(r)

t = Tree("okay")
t.add("time")
t.add("for",[0,0])
t.add("lunch",[0,0,0])
t.add("breakfast",[0,0,1])
t.add("dinner",[0,0,2])
print(t.search("for",t.root))
print(t.search("aoeu",t.root))
