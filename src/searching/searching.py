# TO-DO: Implement a recursive implementation of binary search
def binary_search(arr, target, start, end):
    # Your code here
    l = start
    h = end
    if l <= h:

        m = (l + h) // 2
        print('l', l, 'h', h, 'm', m)
        if arr[m] == target:
            return m
        elif arr[m] < target:
            return binary_search(arr, target, m + 1, h)
        else:
            return binary_search(arr, target, l, m - 1)
    else:
        return -1

# STRETCH: implement an order-agnostic binary search
# This version of binary search should correctly find 
# the target regardless of whether the input array is
# sorted in ascending order or in descending order
# You can implement this function either recursively 
# or iteratively
def agnostic_binary_search(arr, target):
    l, h = 0, len(arr) - 1
    def rev_binary_search(arr, target, l, h):
        if l >= h:
            m = (l + h) // 2
            print('l', l, 'h', h, 'm', m)
            if arr[m] == target:
                return m
            elif arr[m] < target:
                return rev_binary_search(arr, target, m - 1, h)  
            else:
                return rev_binary_search(arr, target, l, m + 1)                                 
        else:
            return -1
    if arr[l] > arr[h]:
        return rev_binary_search(arr, target, h, l)
    else:
        return binary_search(arr, target, l, h)

