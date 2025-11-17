# Contains Duplicate solution 
def contains_duplicate(nums):
    seen = set()
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    return False

# Example
print(contains_duplicate([1,2,3,1]))
print(contains_duplicate([1,2,3,4]))
