def selectionSort(lists):
     for i in range(len(lists)):
        min_pos = i
        for j in range(i+1,len(lists)):
            if lists[j] < lists[min_pos]:
                min_pos = j
                
        temp = lists[i]
        lists[i] = lists[min_pos]
        lists[min_pos] = temp
      
                
myList = [9,5,8,6,7,10,3,2,1,4]

selectionSort(myList)
print(myList)               
    
      