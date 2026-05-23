class Solution:
    def isPalindrome(self, s: str) -> bool:
        # s = ''.join([i for i in s if i.isalnum()]).lower()
        # return s == s[::-1]
        start = 0
        end = len(s) - 1
        while start < end:
            while start < end and not s[start].isalnum():
                start += 1
            while start < end and not s[end].isalnum():
                end -= 1     
            if s[start].lower() != s[end].lower():
                return False
            start += 1
            end -= 1
        return True



        # Aliter: 2 pointers - not a very big fan of grokking 'patterns' to code curbing my natural instinct
        # start = 0
        # end = len(s) - 1
        # while start <= end:
        #     if s[start] == s[end]:
        #         start += 1
        #         end -= 1
        #         continue
        #     else:
        #         return False
        # return True