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
		r = False

		if tree.data == node:
			r = True
			return(r)

		while tree.relatives:
			if node in [f.data for f in tree.relatives]:
				r = True
				return(r)

			for f in tree.relatives:
				r = self.search(node,f)
				return(r)

		return(r)

t = Tree("okay")
t.add("time")
t.add("for",[0,0])
t.add("lunch",[0,0,0])
t.add("breakfast",[0,0,1])
t.add("dinner",[0,0,2])
print(t.search("okay",t.root))
print(t.search("time",t.root))
print(t.search("for",t.root))
print(t.search("lunch",t.root))
print(t.search("breakfast",t.root))
print(t.search("dinner",t.root))
print(t.search("aoeu",t.root))
