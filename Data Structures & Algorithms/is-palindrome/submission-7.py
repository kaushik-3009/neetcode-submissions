class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned_s = ''.join(char.lower() for char in s if char.isalnum())
        str_len = len(cleaned_s)
        print(str_len)
        for index in range(str_len//2):
            print(cleaned_s[index], cleaned_s[str_len - (index+1)])
            if cleaned_s[index] != cleaned_s[str_len - (index+1)]:
                return False
            
        return True