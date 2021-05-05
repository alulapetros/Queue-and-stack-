class Node:
    def __init__(self,data,next):
        self.data = data
        self.next = next
                
class Stack:
    def __init__(self):
        self.head = None
        self.nodeCounter =0
             
    def push(self,data):
        self.nodeCounter  += 1
 
        if self.head is None:
            self.head = Node(data,None)
            return
        
        currentHead = self.head
        
        while currentHead.next != None:
            currentHead =  currentHead.next
           
        currentHead.next = Node(data,None)
        
        
    def pop(self):
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
    
    
    def pick(self):
        self.nodeCounter -=1
        if self.head == None:
            print("The List is empty")
            return
        else:
            currentHead = self.head
            
            while currentHead.next.next != None:
                currentHead =  currentHead.next
            currentHead.next = None
                               

stack = Stack()
stack.push(12)
stack.push(11)
stack.push(31)
stack.push(366)
stack.push(99)
stack.push(889)
print(stack.pop())
print(stack.pick())
stack.size()

stack.showItems()
    