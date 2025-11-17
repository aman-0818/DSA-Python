# Valid Palindrome solution 
def is_palindrome(s):
    filtered = ""
    for ch in s:
        if ch.isalnum():
            filtered += ch.lower()

    left, right = 0, len(filtered) - 1

    while left < right:
        if filtered[left] != filtered[right]:
            return False
        left += 1
        right -= 1

    return True

# Example
print(is_palindrome("A man, a plan, a canal: Panama"))  # True
print(is_palindrome("race a car"))                      # False
