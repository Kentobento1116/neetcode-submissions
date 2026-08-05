class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned_str = ''.join(x for x in s if x.isalnum())
        if not cleaned_str:
            return True
        for i in range(len(cleaned_str) // 2):
            if cleaned_str[i].upper() != cleaned_str[-1-i].upper():
                return False
        return True