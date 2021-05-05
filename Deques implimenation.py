class Node:
    def __init__(self,data,next):
        self.data = data
        self.next = next
                
class Deque:
    def __init__(self):
        self.head = None
        self.nodeCounter =0
             
    def addRear(self,data):
        self.nodeCounter  += 1
        if self.head is None:
           self.head = Node(data,None)
           return
        
        currentHead = self.head
        
        while currentHead.next != None:
            currentHead =  currentHead.next
  
        currentHead.next = Node(data,None)
        
    
    def addFront(self,data):
        self.nodeCounter  += 1
        
        if self.head is None:
            self.head = Node(data,None)
            return
        
        currentHead = self.head
        self.head = Node(data,None)
        self.head.next = currentHead 
        
        
    def removeRear(self):
        self.nodeCounter -=1
        
        if self.head == None:
            print("The List is empty")
            return
        else:
            currentHead = self.head
            
            while currentHead.next.next != None:
                popOurData = currentHead.next.next.data
                currentHead =  currentHead.next
            currentHead.next = None
            return popOurData 
         
    def removeFront(self):
        self.nodeCounter -=1
        
        if self.head == None:
            print("The List is empty")
           
        else: 
            popOurData = self.head.data
            self.head = self.head.next
            
        return popOurData 
        
           
    def showItems(self):
        if self.head == None:
            print("The List is empty")
            return
            
        n = self.head
        listContainer= ""
        
        while n!= None:
            listContainer += str(n.data) + "->"
            n = n.next
            
        print(listContainer)

    
    def isEmpty():
        if self.head == None:
            print("The List is empty")
            
    def size(self):
        print("You have created {} items".format(self.nodeCounter))

d = Deque()
d.addFront(1)
d.addFront(2)
d.addFront(3)
d.addFront(4)
d.addFront(5)
d.addRear(6)
d.addRear(7)
d.removeRear()
d.removeFront()

d.showItems()

