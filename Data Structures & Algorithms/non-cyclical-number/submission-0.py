class Solution:
    def isHappy(self, n: int) -> bool:
        num = n
        sum_count = 0
        sum_history = {}
        while True:
            digit = num%10
            num //= 10
            sum_count += (digit**2)
            if num <= 0:
                if sum_count == 1:
                    return True
                elif sum_count in sum_history:
                    return False
                else:
                    sum_history[sum_count] = 1
                    num = sum_count
                    sum_count = 0
        
                