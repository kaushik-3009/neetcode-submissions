class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_counter = 0
        for i in range(len(s)):
            print("i: ", s[i])
            counter = 1
            num_set = {s[i]}
            for j in range(i+1, len(s)):
                print("j: ",s[j])
                if s[j] not in num_set:
                    num_set.add(s[j])
                    counter+=1
                else:
                    break
            max_counter = max(counter, max_counter)

        return max_counter