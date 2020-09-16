# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(left, right):
    # elements = len(left) + len(right)
    # merged_arr = [0] * elements
    merged_arr = []

    # Your code here

    left_point = right_point = 0

    while left_point < len(left) and right_point < len(right):

        if left[left_point] < right[right_point]:
            merged_arr.append(left[left_point])
            left_point += 1

        else:
            merged_arr.append(right[right_point])
            right_point += 1

    merged_arr.extend(left[left_point:])
    merged_arr.extend(right[right_point:])

    return merged_arr

# TO-DO: implement the Merge Sort function below recursively


def merge_sort(arr):
    # Your code here

    if len(arr) <= 1:
        return arr

    midpoint = len(arr) // 2

    left, right = merge_sort(arr[:midpoint]), merge_sort(arr[midpoint:])

    return merge(left, right)

# STRETCH: implement the recursive logic for merge sort in a way that doesn't
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists
# or data structures; it can only re-use the memory it was given as input


def merge_in_place(arr, start, mid, end):
    # Your code here
    pass


def merge_sort_in_place(arr, l, r):
    # Your code here
    pass
