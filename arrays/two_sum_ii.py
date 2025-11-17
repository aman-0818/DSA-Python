# Two Sum II solution 
def two_sum_ii(numbers, target):
    left = 0
    right = len(numbers) - 1

    while left < right:
        s = numbers[left] + numbers[right]

        if s == target:
            return [left + 1, right + 1]  # 1-indexed output
        elif s < target:
            left += 1
        else:
            right -= 1

    return []  # No solution

# Example
print(two_sum_ii([2, 7, 11, 15], 9))    # [1, 2]
print(two_sum_ii([1,2,3,4,4,9,56,90], 8))  # [4, 5]
