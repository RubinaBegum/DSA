def binary_search(list1, x):  
    low = 0  
    high = len(list1) - 1  
    mid = 0  
  
    while low <= high:  
        mid = (high + low) // 2    
        if list1[mid] < x:  
            low = mid + 1  
        elif list1[mid] > x:  
            high = mid - 1    
        else:  
            return "the positon of the element is",mid     
list1 = [0,2, 13, 14, 19, 20]  
x = 20 
print(binary_search(list1, x))