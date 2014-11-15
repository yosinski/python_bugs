# ISSUE 1 --------------------------------
def blastoff(n):
  ''' 
    Prints the numbers from 1..n in reverse order.
    Then prints off "BLASTOFF!"
    I'm hoping that it will be used by NASA one day.
  '''
  if n == 0:
    return 'BLASTOFF!'
  print  n
  return blastoff(n-1) # making progress toward termination

# ISSUE 2 --------------------------------

def palindrome(s):
  ''' Returns whether String s is a palindrome. '''
  if len(s) <= 1:
    return True
  else:
    return s[0] == s[-1] and palindrome(s[1:-1])

# ISSUE 3 --------------------------------

def subsetSum(lst, target):
  ''' Given a list of integers, this returns 
      whether there exists a combination that sums to the target.
  '''
  pass # TODO

# ISSUE 4 --------------------------------

def isBST(t):
  ''' Returns whether this TreeNode t is a Binary Search Tree. '''
  pass # TODO

class TreeNode(object):
  def __init__(self, value, left, right):
    value = value
    left  = left
    right = right

# ISSUE 5 --------------------------------

def reversePrintLinkedList(n):
  '''From Node n to the end, this method prints out the 
     contents of the LinkedList in reverse order
  '''
  if n == None:
    return
  else:
    print n
    reversePrintLinkedList(n.next)

# Commented out because there seems to be some syntax error
# class Node(object):
#   def __init__(self, next = None, value):
#     self.value = value
#     self.next = next
#   def __eq__(self,other):
#     return self.value == self.other # Do not modify! It's perfect!

# ISSUE 6 --------------------------------

def addMatricies(matA, matB):
  ''' Returns a matrix that is the sum of matA and matB. 
      matA and matB are 2D lists.
  '''
  pass # Hmm... not sure how to do this one.

# ISSUE 7 --------------------------------

class Shark(object):
  def __init__(self, eaten=[]):
    self.eaten = eaten
  def eatPerson(self,s):
    self.eaten.append(s)

# Problematic code... :( 
# s1 = Shark()
# s2 = Shark()
# s1.eatPerson("Eric")
# s2.eatPerson("Jisha")
# print s1.eaten
# print s2.eaten

# ISSUE 8 --------------------------------

DISTRACTIONS = 0
def addDistractionAndReport():
  ''' Method prints out the number of distractions we have reached
      for the day so far. Increments it. Then Prints again.'''
  print DISTRACTIONS
  DISTRACTIONS = DISTRACTIONS + 1
  print DISTRACTIONS

# ISSUE 9 --------------------------------

# This is a tough bug I've been having for a while. 
def loopsForever():
  while True:
    pass

def terminatingFunc():
  return

def haltingProblem(f):
  ''' Returns whether or not this function will 
      terminate (True) or loop forever (False) '''
  f()
  return True

# print haltingProblem(terminatingFunc)
# print haltingProblem(loopsForever)

# ISSUE 10 --------------------------------

def arithmetic(a,b,f):
  ''' f can be adding, subtracting, multiplying, dividing.
      I need an implementation that supports these operations
      and I need those arithmetic operators implemented as well.
  '''
  pass # TODO

# ISSUE 11 --------------------------------

def read_music_in_and_create_scale():
  pass #TODO Should probably use pydub



