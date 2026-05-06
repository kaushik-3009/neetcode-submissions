class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums)-1

        bdry_elem = -1

        while l<=r:
            mid = (l+r)//2
            if nums[mid]<= nums[-1]:
                bdry_elem=nums[mid]
                r = mid-1
            else:
                l=mid+1
        
        return bdry_elem






"""

6, 1, 2, 3, 4, 5

2, 3, 4, 5, 6, 1

l > r if rotated

l <= r in og

2, 3, 4, 5, 6, 1
"""