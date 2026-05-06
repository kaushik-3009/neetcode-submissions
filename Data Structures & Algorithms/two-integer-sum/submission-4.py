class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = {}

        for index, number in enumerate(nums):
            difference = target - number
            if difference in hash_map:
                return [hash_map[difference], index]
            hash_map[number] = index