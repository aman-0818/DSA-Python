# Group Anagrams solution 
from collections import defaultdict

def group_anagrams(strs):
    groups = defaultdict(list)

    for s in strs:
        # Sort characters to create a key
        key = ''.join(sorted(s))
        groups[key].append(s)

    return list(groups.values())


# Example
print(group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
# Output:
# [["eat","tea","ate"], ["tan","nat"], ["bat"]]
