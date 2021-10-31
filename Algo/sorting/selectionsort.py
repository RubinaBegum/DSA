def selection_sort(list1,lenght):
    for j in range(lenght):
        mini_index=j
        for i in range(j+1,lenght):
            if list1[i]<list1[mini_index]:
                mini_index=i
                (list1[j],list1[mini_index])=(list1[mini_index],list1[j])
list1=[0,-9,11,5,7,20]
lenght=len(list1)
selection_sort(list1,lenght)
print(list1)