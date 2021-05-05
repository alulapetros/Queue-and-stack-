def insertionSort(lists):
    for index in range(1,len(lists)):
        value = lists[index]
        i = index -1
        
        while i >= 0:
            if value < lists[i]:
                lists[i+1] = lists[i]
                lists[i] = value
                i = i-1
            else:
                break
            
                
myList = [9,5,8,6,7,10,3,2,1,4]
insertionSort(myList)

print(myList)

       