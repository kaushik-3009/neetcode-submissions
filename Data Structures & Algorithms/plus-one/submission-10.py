class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        reversed_digits = digits
        reversed_digits.reverse()
        sum = 1
        for index in range(len(reversed_digits)):
            sum += reversed_digits[index]*(10**(index))
        return self.get_new_digits(sum)

    def get_new_digits(self, n):
        nums = []
        while n>0:
            nums.append(n%10)
            n //= 10
        nums.reverse()
        return nums