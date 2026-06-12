class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        n = len(intervals)
        res = []
        left, right = 0, n-1

        target = newInterval[0]

        while left <= right:
            mid = (left+ right)// 2
            if intervals[mid][0] < target:
                left = mid+1
            else:
                right = mid -1
        
        intervals.insert(left, newInterval)

        for interval in intervals:
            if not res or res[-1][1] < interval[0]:
                res.append(interval)
            else:
                res[-1][1] = max(res[-1][1], interval[1])
        
        return res


"""

        n = len(intervals)
        res = []
        i = 0

        while i < n and intervals[i][1] < newInterval[0]:
            res.append(intervals[i])
            i+=1
        
        while i < n and newInterval[1] >= intervals[i][0]:
            newInterval[0] = min(newInterval[0], intervals[i][0])
            newInterval[1] = max(newInterval[1], intervals[i][1])
            i+=1 
        res.append(newInterval)
        
        while i < n:
            res.append(intervals[i])
            i+=1
        
        return res
        
"""




# my_list = ['apple', 'banana', 'cherry']
# # Syntax: list.insert(index, element)
# my_list.insert(1, 'orange') 



"""
linear saerch:
add everthing upto curr[i][1] < new[0]

 search until you find something where  new[end] > curr[start]    
 new[0] = max(new[0], curr[0])
 same as above for end
 
 new.append to res

 add in rest of intervals


 binary search:
 target: new[0]
 
 when you find left

 insert into og intervials
 for loop:
    if res[1]> curr[start], merge them
"""