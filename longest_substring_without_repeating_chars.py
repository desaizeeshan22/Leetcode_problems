def lengthOfLongestSubstring(s):
    hash_map = {}
    left = 0
    if s == "":
        return 0
    max_len = float("-inf")
    for right, char in enumerate(s):
        if char in hash_map and left <= hash_map[char]:
            left = hash_map[char] + 1
        else:
            max_len = max(max_len, right - left + 1)
        hash_map[char] = right
    return max_len

s = "abcabcbb"
print(lengthOfLongestSubstring(s))