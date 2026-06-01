class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashset = {}
        result = []
        for string in strs:
            if str(sorted(string)) in hashset:
                hashset[str(sorted(string))].append(string)
                continue
            hashset[str(sorted(string))] = [string]
        
        for res_arr in hashset.values():
            result.append(res_arr)

        return result