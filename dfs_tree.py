#Node structure
class Node:
	def __init__(self, data=None, left=None, center = None, right=None):
		self.data = data
		self.left = left
		self.center = center
		self.right = right

#Iterative function to perform dfs preorder traversal on a tree
def dfs(root):
 
    #If there is no root, return empty
    if root is None:
        return
 
    #Push root into empty stack
    stack = []
    stack.append(root)

    # loop till stack is empty
    while stack:
        # pop a node from the stack and print it
      curr = stack.pop()
      
      print(curr.data)
      #Push right node of current node into stack
      if curr.right:
          stack.append(curr.right)
      #Push center node of current node into stack    
      if curr.center:
          stack.append(curr.center)
      #Push left node of current node into stack
      if curr.left:
          stack.append(curr.left)
 
def main():

	''' The tree is as follows:
			       1
			 /     |     \
		   2       3      4
		  /|\     /|\    /|\
		5  6  7  8 9 10 11 12 13
	
	'''
	
	#Constructing tree
	root = Node(1)
	root.left = Node(2)
	root.center = Node(3)
	root.right = Node(4)
	root.left.left = Node(5)
	root.left.center = Node(6)
	root.left.right = Node(7)
	root.center.left = Node(8)
	root.center.center = Node(9)
	root.center.right = Node(10)
	root.right.left = Node(11)
	root.right.center = Node(12)
	root.right.right = Node(13)
    
    #Calling dfs on root
	dfs(root)

main()