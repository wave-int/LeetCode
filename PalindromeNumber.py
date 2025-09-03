class Solution:
    def isPalindrome(self, x: int) -> bool:
        result = True
        x = str(x)
        if len(x) % 2 > 0:
            if len(x) == 3:
                if x[0] != x[2]:
                    result = False
            else:
                for i in range (int(len(x) / 2)):
                    if x[int(len(x) / 2) - i] != x[int(len(x) / 2) + i]:
                        result = False
        else:
            for i in range (int(len(x) / 2)):
                if x[i] != x[int(len(x)) - i - 1]:
                    result = False
        if int(x) < 0:
            result = False
        return result