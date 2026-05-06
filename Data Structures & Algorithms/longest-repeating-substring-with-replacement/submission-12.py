class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        from collections import Counter
        mp = Counter()
        left = 0
        max_f_char = 0
        len_substr_sofar = 0
        for right in range(len(s)):
            mp[s[right]]+=1
            max_f_char =  max(max_f_char, mp[s[right]]) 

            while ((right-left+1) - max_f_char) > k:
                mp[s[left]] -=1
                left+=1

            len_substr_sofar = max(len_substr_sofar, right-left+1) 
        return len_substr_sofar