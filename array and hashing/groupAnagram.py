"""
Group Anagrams
Given an array of strings strs, group all anagrams together into sublists. You may return the output in any order.

An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.

Example 1:

Input: strs = ["act","pots","tops","cat","stop","hat"]

Output: [["hat"],["act", "cat"],["stop", "pots", "tops"]]
Example 2:

Input: strs = ["x"]

Output: [["x"]]
Example 3:

Input: strs = [""]

Output: [[""]]
"""

def groupAnagrams(strs: list[str]) -> list[list[str]]:
    anagram_map = {}
    for s in strs:
        # Sort the characters of the string to create a key
        # This ensures all anagrams will have the same key
        sorted_str = ''.join(sorted(s))

        # Check if the sorted string is already in the map
        if sorted_str in anagram_map:
            # If it is, append the current string to the existing list
            anagram_map[sorted_str].append(s)
        else:
            # If not, create a new list with the current string
            anagram_map[sorted_str] = [s]
    
    # Convert the map values to a list
    return list(anagram_map.values())

print(groupAnagrams(["act","pots","tops","cat","stop","hat"]))
print(groupAnagrams(["x"]))
print(groupAnagrams([""]))



