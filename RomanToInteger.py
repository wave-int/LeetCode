class Solution:
    def romanToInt(self, s: str) -> int:       
        s = ' ' + s
        nums = []
        last = ''
        group = ""
        for i in range (len(s)):
            if s[i] == last:
                group += s[i]
            else:
                nums.append(group)
                group = s[i]
                last = s[i]
        nums.append(group)
        for i in range(2, len(nums)):
            if i < 2: 
                i = 2
            match nums[i][0]: 
                case 'I': nums[i] = len(nums[i]) * 1
                case 'V': nums[i] = len(nums[i]) * 5
                case 'X': nums[i] = len(nums[i]) * 10
                case 'L': nums[i] = len(nums[i]) * 50
                case 'C': nums[i] = len(nums[i]) * 100
                case 'D': nums[i] = len(nums[i]) * 500
                case 'M': nums[i] = len(nums[i]) * 1000
        result = nums[2]
        for i in range(3, len(nums)):
            result += nums[i]
            if nums[i] > nums[i - 1]:
                result -= nums[i - 1]
                result -= nums[i - 1]
        return result