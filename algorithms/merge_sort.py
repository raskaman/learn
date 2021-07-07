def merge_sort(list):
    """
    Sort given list in ascending order
    Returns a new sorted list

    Divide: find the mid point of the list and dive into sublists
    Conquer: recursively sort the sublist created in previous (divide) step
    Combines: merge the sorted sublists created in previous step

    Takes 0(kn Log n) time
    Takes 0(n) linear space complexity

    """

    if len(list) <= 1:
        return list

    left_half, right_half = split(list)
    left = merge_sort(left_half)
    right = merge_sort(right_half)

    return merge(left, right)

def split(list):
    """
    Divide the unsorted list at midpoint into sublits
    Returns two sublists - left and right

    Takes overall 0(k log n) time
    """

    midPoint = len(list) // 2

    return list[:midPoint], list[midPoint:]

def merge(left, right):
    """
    Merges two lists (arrays), sorting them in the process
    Returns a new merged list

    Runs in ovcerall 0(n) linear time
    """

    l = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            l.append(left[i])
            i += 1
        else:
            l.append(right[j])
            j += 1
    
    while i < len(left):
        l.append(left[i])
        i += 1

    while j < len(right):
        l.append(right[j])
        j += 1

    return l

def verify_sorted(list):
    n = len(list)

    if n == 0 or n == 1:
        return True

    return list[0] < list[1] and verify_sorted(list[1:])

"""
Test merge_sort
"""
alist = [54, 62, 93, 17, 77, 31, 44, 55, 20]
print(alist)
print("Sorted: %s" % verify_sorted(alist))
l = merge_sort(alist)
print(l)
print("Sorted: %s" % verify_sorted(l))