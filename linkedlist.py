#Create structures for Node and LinkedList objects
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None;
        self.prev = None;
        
class LinkedList:
    def __init__(self):
        self.head = None;
        self.tail = None;
        
    #Function which adds node to tail of list    
    def insert(self, data):
    	
        node = Node(data)
     
        if self.head == None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node
        
    #Function that sets head node to next to head.    
    def removeFirstNode(self):
        self.head = self.head.next
        
    #Function that checks until no neighboring node, and sets current node to prev.    
    def removeEndNode(self):
        temp = self.head
        while(temp):
            print(temp.data)
            temp = temp.next
            if(temp.next == None):
                return
            
def main():
    
    #Create a linkedList instance
    linkedList = LinkedList()
    
    #Insert elements
    linkedList.insert(1)
    linkedList.insert(2)
    linkedList.insert(3)
    linkedList.insert(4)
    
    
    #Removing head and tail
    linkedList.removeFirstNode()
    linkedList.removeEndNode()
  

main()