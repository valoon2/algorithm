array = [1,10,5,8,7,6,4,3,2,9]

def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(1, len(arr) - i):
            if arr[j-1] > arr[j] :
                arr[j-1], arr[j] = arr[j], arr[j-1]

bubble_sort(array)
print(array)