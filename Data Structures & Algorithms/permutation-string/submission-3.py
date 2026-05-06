class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1 = sorted(s1)

        for i in range(len(s2)-len(s1)+1):
            print(sorted(s2[i:(i+len(s1))]))
            if sorted(s2[i:(i+len(s1))]) == s1:
                return True

        return False            
            





"""

-> sliding window of size s1

-> use this to pass through the s2

-> keep a dict of s1 counts

-> at every window: if key not in dict or value < 0 after minusing:
    return False

-> at every window transition, add left elem of window back in dict
 and minus new right element from dict (keep above check always)

return True if all elem in dict are 0 after covering window elems 

return false at end
"""