array = [3,7,8,1,5,9,6,10,2,4]

def quick_sort(arr):

    print("초기 입력값 : " , arr)
    if len(arr) < 2:
        return arr

    pivot = arr[len(arr) // 2]

    left_arr, equal_arr, right_arr = [], [], []
    

    for i in arr:
        if i < pivot :
            left_arr.append(i)
        elif i == pivot:
            equal_arr.append(i)            
        else :
            right_arr.append(i)            
    
    print("left_arr : ", left_arr)
    print("equal_arr : ", equal_arr)
    print("right_arr : ", right_arr)
    
    return quick_sort(left_arr) + quick_sort(equal_arr) + quick_sort(right_arr)

a = quick_sort(array)
print(a)

