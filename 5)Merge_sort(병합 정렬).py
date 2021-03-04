array = [3,7,8,1,5,9,6,10,2,4]

def merge_sort(arr):

    print("처음시작",arr)
    result = []
    if len(arr) < 2:
        return arr

    mid = len(arr) // 2

    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    print("left : ", left)
    print("right : ", right)

    left_idx = right_idx = 0
    
    while(left_idx < len(left) and right_idx < len(right)):
        if left[left_idx] > right[right_idx] :
            result.append(right[right_idx])
            right_idx += 1
            if right_idx == len(right):
                result += left[left_idx:]
        else :
            result.append(left[left_idx])
            left_idx += 1
            if left_idx == len(left):
                result += right[right_idx:]
    print("return 되는 값 : ", result)
    return result
    

a = merge_sort(array)
print(a)
