#!/usr/bin/python3
def roman_to_int(roman_string):
    if not roman_string or type(roman_string) != str:
        return 0
    roman_d = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    sum = 0
    for i in range(len(roman_string)-1):
        left = roman_string[i]
        right = roman_string[i+1]
        if roman_d[left] < roman_d[right]:
            sum -= roman_d[left]
        else:
            sum += roman_d[right]
    sum += roman_d[roman_string[-1]]
    return sum

