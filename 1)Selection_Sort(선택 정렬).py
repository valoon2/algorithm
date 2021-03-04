array = [1,10,5,8,7,6,4,3,2,9]

#선택정렬
# def selection_sort(arr):
#     for i in range(len(arr) - 1):
#         min_idx = i
#         for j in range(i + 1, len(arr)):
#             if arr[j] < arr[min_idx]:
#                 min_idx = j
#         arr[i], arr[min_idx] = arr[min_idx], arr[i]

def selection_sort(arr):
    for i in range(len(arr)): 
        for j in range(i+1, len(arr)):
            if arr[i] > arr[j]:
                arr[j], arr[i] = arr[i], arr[j]

selection_sort(array)
print(array)