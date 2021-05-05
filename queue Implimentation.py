class Node:
    def __init__(self,data,next):
        self.data = data
        self.next = next
                
class Queue:
    def __init__(self):
        self.head = None
        self.nodeCounter =0
             
    def enqueue(self,data):
        self.nodeCounter  += 1
        
        if self.head is None:
            self.head = Node(data,None)
            return
        
        currentHead = self.head
        
        while currentHead.next != None:
            currentHead =  currentHead.next
           
        currentHead.next = Node(data,None)
        
        
    def dequeue(self):
        self.nodeCounter -=1
        if self.head == None:
            print("The List is empty")
           
        else: 
            dqData = self.head.data
            self.head = self.head.next
            
        return dqData
            
           
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
    

                               

q= Queue()
q.enqueue(11)
q.enqueue(31)
q.enqueue(91)
q.enqueue(88)
print(q.dequeue())

q.size()

q.showItems()
    