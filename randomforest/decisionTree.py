import numpy as np
# let's build a decision tree

# a tree is made of nodes :
# the root node
#   doesn't have a parent
# the internal nodes
#   have parent
#		have children
# the leaf nodes
#   have a parent
#   have no children

"""
class Node:
  def __init__(self, parent = null, left = null, right = null):
    self.parent     = parent
    self.left       = left
    self.right      = right
    self.population = 0

  def setLeft(left):
    self.left = left

  def getLeft(left):
    return self.left

  def setRight(right):
    self.right = right
	
  def getRight(right):
    return self.right

  def setParent(parent):
    self.parent = parent
	
  def getParent(parent):
	  return self.parent


def count(x, y):
  #x : input  column
  #y : output column
	# test x and y are the same size
"""

"""
I need to think first
je pense que j'ai besoin de voir tout le process

putain j'ai perdu 3/4 d'heure à cause du voleur de voiture

pour comprendre le processus et réfléchir à comment implémenter, j'ai besoin d'
essayer avec un exemple et de faire tout le process sans tout spliter

"""

import pandas as pd

x = pd.Series([0,0,0,0,1,1,0,1,0,1,0,1,0,0,1,1,0,1])
y = pd.Series([1,1,0,1,0,0,0,1,1,1,1,1,1,0,0,1,0,1])
data = pd.DataFrame({
	'feature':x, 'pred':y
})
print(data)

""" 
j'ai mes données dans data dans un dataframe
"""


def gini(x, y):
  """
  Only for binary classification
  x and y should hold True/False or 0/1 values
  x : pandas.Series contains the data we want to compute the gini impurity of
  y : pandas.Series contains the true "prediction"

  """
  if x.size != y.size:
  # TODO : throw an exception
    print("pas ok")
    return -1

  pos = 0 # nb of positive/true examples
  pos_pos = 0 # positive with positive y
  pos_neg = 0 # positive with negative y

  neg = 0
  neg_pos = 0
  neg_neg = 0

  for i in range(x.size):
    f = x.iloc[i] # feature
    p = y.iloc[i] # what it has to predict
    if f :
      pos += 1
      if p :
        pos_pos += 1
      else :
        pos_neg += 1
    else :
      neg += 1
      if p :
        neg_pos += 1
      else :
        neg_neg += 1

  pos_partial_gini = 1 - (pos_pos/pos)**2 - (pos_neg/pos)**2

  neg_partial_gini = 1 - (neg_pos/neg)**2 - (neg_neg/neg)**2

  total = pos + neg
  gini  = (pos/total)*pos_partial_gini + (neg/total)*neg_partial_gini
  return gini


  """
  spliting data

  we need to split the data in 2 different situations :

  1. when creating the tree, to select a single column
  2. when the data in the column is non binary

  The first one is not difficult, let's focus on the 2nd situation

  Whenever we have non binary data, we need to create True/False questions,
  we create a dataset for each of these questions and compute the Gini Impurity
  to know which question is the best one.

  I am very annoyed by how to transform the data into some sort of binary data
  Automatically detecting the "type" of the data is not really possible, an int
  could be a rank, a continuous variables, a multiple choice or a boolean
  """
def data_to_binary(x, cat):
  """
  Take input x and return an array of indexes
  [[indexes]]
  np.array/pd.Series x : input
  string cat : category ('bool','numeric','choice')

  en fait je suis en train de mélanger plusieurs idées en même temps
  il faut que je réfléchisse un peu,
  si c'est déjà bool ou binaire, on a pas besoin de faire de transformation
  si c'est un multiple choice, on pourrait juste récupérer les indices des Trues
  même choses pour les numerics et les ranks
  """
  if cat == 'bool':
    return [np.arange(x.size())]
  if cat == 'numeric':
    return 0
  if cat == 'choice':
    # stores the indexes of the subsets
    # each choice has its own subset
    indexes = []
    # get all the possible choices
    choices = np.unique(x)
    # loop through all the choices
    for choice in choices:

    indexes = np.where(x)


    

def split_data(x, y):
  # if there is more than two type of data
  np.unique(x).size 
  # the struggle is real OMGLOL


print(gini(data["feature"], data["pred"]))
x = np.array([True,False])
data_to_binary(x[1])




























