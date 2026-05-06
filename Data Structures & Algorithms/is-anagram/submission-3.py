class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        char_dict_a = {}
        char_dict_b = {}
        if len(s) != len(t):
            return False
        for index in range(len(s)):
            char_dict_a[s[index]] = 1 + char_dict_a.get(s[index], 0)
            char_dict_b[t[index]] = 1 + char_dict_b.get(t[index], 0)
        return char_dict_a == char_dict_b