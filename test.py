import Node
import Tree
import DirectedGraph

t = Tree.Tree("okay")
t.add("time")
t.add("for",[0,0])
t.add("lunch",[0,0,0])
t.add("breakfast",[0,0,1])
t.add("dinner",[0,0,2])
print(t.search("okay",t.root)) # true
print(t.search("time",t.root)) # true
print(t.search("for",t.root)) # true
print(t.search("lunch",t.root)) # true
print(t.search("breakfast",t.root)) # true
print(t.search("dinner",t.root)) # true
print(t.search("aoeu",t.root)) # false

dg = DirectedGraph.DirectedGraph("okay")
dg.add("this")
dg.add("is")
dg.add("sparta")
dg.add("mhm",[dg.first.relatives])
print(dg.search("mhm",dg.first)) # true
print(dg.search("this",dg.first)) # true
print(dg.search("is",dg.first)) # true
print(dg.search("sparta",dg.first)) # true
print(dg.search("woah",dg.first)) # false
