def merge_sort(arr):
    if len(arr)<=1:
        return arr
    mid=len(arr)//2
    left_half=merge_sort(arr[:mid])
    right_half=merge_sort(arr[mid:])
    return merge(left_half,right_half)

def merge(left_arr, right_arr):
    """Merge sort merging function."""

    left_index, right_index = 0, 0
    result = []
    while left_index < len(left_arr) and right_index < len(right_arr):
        if left_arr[left_index] <= right_arr[right_index]:
            result.append(left_arr[left_index])
            left_index += 1
        else:
            result.append(right_arr[right_index])
            right_index += 1
    result += left_arr[left_index:]
    result += right_arr[right_index:]
    return result
print(merge_sort([4,1,3,2,0,-1,7,10,9]))