class Solution:
    def myAtoi(self, s: str) -> int:
        integer = int(0)
        row = 1
        negative = False
        num = False
        plus = False
        integer = round(integer)
        for i in range (len(s)):
            integer = round(integer)
            integer *= 10
            match s[i]:                
                case "1":
                    num = True
                    integer += row
                case "2":
                    integer += row * 2
                    num = True
                case "3":
                    integer += row * 3
                    num = True
                case "4":
                    integer += row * 4
                    num = True
                case "5": 
                    integer += row * 5
                    num = True
                case "6": 
                    integer += row * 6
                    num = True
                case "7":
                    integer += row * 7
                    num = True
                case "8": 
                    integer += row * 8
                    num = True
                case "9":
                    integer += row * 9
                    num = True
                case " ":
                    integer /= 10
                    if num == True:
                        break
                case "+":
                    integer /= 10
                    plus = True
                    if negative == True:
                        break  
                    if num == True:
                        break
                    if i < len(s) - 1:
                        if s[i + 1] == " " or s[i + 1] == "+" or s[i + 1] == "-":
                            break
                case "0":
                    num = True
                case "-":                    
                    if num == True:
                        integer /= 10
                        break
                    if i < len(s) - 1:
                        if s[i + 1] == " " or s[i + 1] == "-":
                            break
                    if plus == False:
                        if num == False:
                            if integer == 0:
                                negative = True
                        else:
                            integer /= 10
                            break
                    else:
                        return 0                    
                case _:
                    integer /= 10
                    break
            integer = round(integer)
        integer = round(integer)
        string = str(integer)
        if len(string) > 1:
            if string[-1] == "0" and string[-2] == ".":
                string = string[:-2]
                string = string + "0"
                integer = int(string)
        if negative == True:
            integer *= -1
        if integer >= 2 ** 31:
            return 2147483647
        if integer < -2 ** 31:
            return -2147483648
        return int(integer)
                    



s = Solution()
print(s.myAtoi("-5-"))
