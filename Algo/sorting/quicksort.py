def partition(List1, low, high):
  pivot = List1[high]
  i = low - 1
  for j in range(low, high):
    if List1[j] <= pivot:
      i = i + 1
      (List1[i], List1[j]) = (List1[j], List1[i])
  (List1[i + 1], List1[high]) = (List1[high], List1[i + 1])
  return i + 1
def quickSort(List1, low, high):
  if low < high:
    pi = partition(List1, low, high)
    quickSort(List1, low, pi - 1)
    quickSort(List1, pi + 1, high)


data = [8, 7, 2, 1, 0, 9, 6]
print("Unsorted list")
print(data)

size = len(data)

quickSort(data, 0, size - 1)

print('Sorted Array in Ascending Order:',data)