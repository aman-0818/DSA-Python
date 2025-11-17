# Merge Sorted Array solution 
def merge(nums1, m, nums2, n):
    # Start from the end of both arrays
    i = m - 1
    j = n - 1
    k = m + n - 1  # Last index of nums1

    # Merge nums1 and nums2 from the end
    while i >= 0 and j >= 0:
        if nums1[i] > nums2[j]:
            nums1[k] = nums1[i]
            i -= 1
        else:
            nums1[k] = nums2[j]
            j -= 1
        k -= 1

    # If nums2 still has elements
    while j >= 0:
        nums1[k] = nums2[j]
        j -= 1
        k -= 1

    return nums1


# Example
print(merge([1,2,3,0,0,0], 3, [2,5,6], 3))  # [1,2,2,3,5,6]
print(merge([1], 1, [], 0))                # [1]
print(merge([0], 0, [1], 1))               # [1]
