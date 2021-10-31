def insertion_sort(list1):
    for i in range(1, len(list1)):
        temp = list1[i]
        j = i - 1
        while (j >= 0 and temp < list1[j]):
            list1[j + 1] = list1[j]
            j = j - 1
        list1[j + 1] = temp
 
 
alist = [3,4,7,2,4,1,5,9]
alist = [int(x) for x in alist]
insertion_sort(alist)
print('Sorted list: ', end='')
print(alist)