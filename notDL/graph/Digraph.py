from Node import Node
from Edge import Edge

class Digraph(object):
  """
  from MIT 6.0002 lecture 3
  edges is a dict mapping each node to a list of its children
  """
  def __init__(self):
    self.edges = {}

  def addNode(self, node):
    """
    nodes are represented as keys in edges
    """
    if node in self.edges:
      raise ValueError("Duplicate node")
    else:
      self.edges[node] = []

  def addEdge(self, edge):
    """
    Edges are represented by destinations as values in list associated with a
    source key
    """
    src = edge.getSource()
    dest = edge.getDestination()
    if not (src in self.edges and dest in self.edges):
      raise ValueError("Node not in graph")
    self.edges[src].append(dest)

  def childrenOf(self, node):
    return self.edges[node]

  def hasNode(self, node):
    return node in self.edges

  def getNode(self, name):
    for n in self.edges:
      if n.getName() == name:
        return n
    raise NameError(name)

  def __str__(self):
    result = ''
    for src in self.edges:
      for dest in self.edges[src]:
        result = result + src.getName() + '->' + dest.getName() + '\n'
    return result[:-1] # omit the final newline

