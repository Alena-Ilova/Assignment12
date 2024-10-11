def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for b in range(0, n-i-1):
            if arr[b] > arr[b+1]:
                arr[b], arr[b+1] = arr[b+1], arr[b]
                return arr       
short_list = [8, 3, 5, 1, 7]
long_list = [6, 1, 9, 3, 10, 15, 7, 20, 4, 16]

sorted_short_list = bubble_sort(short_list.copy())
sorted_long_list = bubble_sort(long_list.copy())

print('Sorted short list:', sorted_short_list)
print('Sorted long list:', sorted_long_list)
