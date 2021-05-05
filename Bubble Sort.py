def bubbleSort(lists):
    for i in range(len(lists)-1):
        for j in range(len(lists)-1):
            if lists[j] > lists[j+1]:
                temp = lists[j]
                lists[j] = lists[j+1]
                lists[j+1] =  temp 
                
myList = [9,5,8,6,7,10,3,2,1,4]

bubbleSort(myList)
print(myList)