def bubble_sort(List1):
    i=0
    while i<len(List1):
        j=i+1
        while j<len(List1):
            if List1[i]<List1[j]:
                List1[i],List1[j]=List1[j],List1[i]
            j=j+1
        i=i+1
    print(List1)
(bubble_sort(List1=[7,8,3,4,10]))