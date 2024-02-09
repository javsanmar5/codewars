'''
Write two functions that convert a roman numeral to and from an integer value. 
Multiple roman numeral values will be tested for each function.

Modern Roman numerals are written by expressing each digit separately starting 
with the left most digit and skipping any digit with a value of zero. In Roman 
numerals 1990 is rendered: 1000=M, 900=CM, 90=XC; resulting in MCMXC. 2008 is 
written as 2000=MM, 8=VIII; or MMVIII. 1666 uses each Roman symbol in descending 
order: MDCLXVI.

Input range : 1 <= n < 4000

In this kata 4 should be represented as IV, NOT as IIII (the "watchmaker's four").

'''


class RomanNumerals:

    conversions = {
        'I': 1, 
        'V': 5, 
        'X': 10,
        'L': 50, 
        'C': 100, 
        'D': 500, 
        'M': 1000
    }

    
    @staticmethod
    def to_roman(val : int) -> str:
        num = [1, 4, 5, 9, 10, 40, 50, 90, 100, 400, 500, 900, 1000]
        sym = ["I", "IV", "V", "IX", "X", "XL", "L", "XC", "C", "CD", "D", "CM", "M"]
        i = 12
        roman_num = ""
        
        while val > 0:
            div = val // num[i]
            val %= num[i]
            while div > 0:
                roman_num += sym[i]
                div -= 1
            i -= 1
        
        return roman_num
    

    @staticmethod
    def from_roman(roman_num : str) -> int:
        i = 0
        res = 0
        if len(roman_num) == 1: return RomanNumerals.conversions[roman_num]
        while i < len(roman_num):
            if i < len(roman_num) -1:
                s1 = RomanNumerals.conversions[roman_num[i]]
                s2 = RomanNumerals.conversions[roman_num[i+1]]
                if s1 >= s2 :
                    res += s1
                    i += 1
                else: 
                    res += s2 - s1
                    i += 2
            else:
                s1 = RomanNumerals.conversions[roman_num[i-1]]
                s2 = RomanNumerals.conversions[roman_num[i]]
                if s2 <= s1:
                    res += s2
                i += 1

        return res

    


#Tryouts

print(RomanNumerals.from_roman('CMXCV'))
print(RomanNumerals.to_roman(1000))