# Majority Element solution 
# Approach 1: Using Hashmap (count frequency)
def majority_element_hashmap(nums):
    count = {}
    for num in nums:
        count[num] = count.get(num, 0) + 1

        if count[num] > len(nums) // 2:
            return num

    return None


# Approach 2: Boyer-Moore Voting Algorithm (O(1) space)
def majority_element_boyer_moore(nums):
    count = 0
    candidate = None

    for num in nums:
        if count == 0:
            candidate = num
        count += 1 if num == candidate else -1

    return candidate


# Example
print("Hashmap:", majority_element_hashmap([3, 2, 3]))          # 3
print("Boyer-Moore:", majority_element_boyer_moore([2,2,1,1,1,2,2]))  # 2
