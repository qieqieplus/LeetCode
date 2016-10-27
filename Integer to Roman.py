class Solution(object):
    def intToRoman(self, num):
        digits = [1000, 900,  500, 400,  100, 90,   50,  40,   10,  9,    5,   4,    1]
        dict   = ["M",  "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
        text   = ""
        for digit, symbol in zip(digits, dict):
            text += symbol * int(num / digit)
            num %= digit
        return text
