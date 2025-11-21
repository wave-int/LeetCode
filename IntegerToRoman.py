class Solution:
    def intToRoman(self, num: int) -> str:
        size = 0
        if num > 9:
            size = 1
        if num > 99:
            size = 2
        if num > 999:
            size = 3
        num = str(num)
        roman = ""        
        for row in range(size + 1):
            if num[size - row] == "1":
                if row == 0:
                    roman = "I" + roman
                elif row == 1:
                    roman = "X" + roman
                elif row == 2:
                    roman = "C" + roman
                elif row == 3:
                    roman = "M" + roman

            if num[size - row] == "2":
                if row == 0:
                    roman = "II" + roman
                elif row == 1:
                    roman = "XX" + roman
                elif row == 2:
                    roman = "CC" + roman
                elif row == 3:
                    roman = "MM" + roman

            if num[size - row] == "3":
                if row == 0:
                    roman = "III" + roman
                elif row == 1:
                    roman = "XXX" + roman
                elif row == 2:
                    roman = "CCC" + roman
                elif row == 3:
                    roman = "MMM" + roman

            if num[size - row] == "4":
                if row == 0:
                    roman = "IV" + roman
                elif row == 1:
                    roman = "XL" + roman
                elif row == 2:
                    roman = "CD" + roman
                elif row == 3:
                    roman = "MMMM" + roman

            if num[size - row] == "5":
                if row == 0:
                    roman = "V" + roman
                elif row == 1:
                    roman = "L" + roman
                elif row == 2:
                    roman = "D" + roman
                elif row == 3:
                    roman = "MMMMM" + roman

            if num[size - row] == "6":
                if row == 0:
                    roman = "VI" + roman
                elif row == 1:
                    roman = "LX" + roman
                elif row == 2:
                    roman = "DC" + roman
                elif row == 3:
                    roman = "MMMMMM" + roman

            if num[size - row] == "7":
                if row == 0:
                    roman = "VII" + roman
                elif row == 1:
                    roman = "LXX" + roman
                elif row == 2:
                    roman = "DCC" + roman
                elif row == 3:
                    roman = "MMMMMMM" + roman

            if num[size - row] == "8":
                if row == 0:
                    roman = "VIII" + roman
                elif row == 1:
                    roman = "LXXX" + roman
                elif row == 2:
                    roman = "DCCC" + roman
                elif row == 3:
                    roman = "MMMMMMMM" + roman

            if num[size - row] == "9":
                if row == 0:
                    roman = "IX" + roman
                elif row == 1:
                    roman = "XC" + roman
                elif row == 2:
                    roman = "CM" + roman
                elif row == 3:
                    roman = "MMMMMMMMM" + roman
        return roman

        
#I	1
#V	5
#X	10
#L	50
#C	100
#D	500
#M	1000
s = Solution()
print(s.intToRoman(3749))     



