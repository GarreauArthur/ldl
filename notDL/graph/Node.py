class Node(object):

  def __init__(self, name):
    """
    name is a string
    """
    self.name = name

  def getName(self):
    return self.name

  def __str__(self):
    return self.name

