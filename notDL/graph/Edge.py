class Edge(object):

  def __init__(self, src, dest):
    """
    @param src  : node
    @param dest : node
    """
    self.src  = src
    self.dest = dest

  def getSource(self):
    return self.src

  def getDestination(self):
    return self.dest

  def __str__(self):
    return self.src.getName() + '->' + self.dest.getName()

