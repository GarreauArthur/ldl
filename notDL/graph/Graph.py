from Digraph import Digraph
from Node import Node
from Edge import Edge

class Graph(Digraph):

  def addEdge(self, edge):
    Digraph.addEdge(self, edge)
    rev = Edge(edge.getDestination(), edge.getSource())
    Digraph.addEdge(self, rev)

