unit_words = {1: "one", 2: "two", 3: "three", 4: "four", 5: "five",6: "six", 7: "seven", 8: "eight", 9: "nine"}
teen_words = {10: "ten", 11: "eleven", 12: "twelve", 13: "thirteen",14: "fourteen", 15: "fifteen", 16: "sixteen",17: "seventeen", 18: "eighteen", 19: "nineteen"}
tens_words = {20: "twenty", 30: "thirty", 40: "forty", 50: "fifty",60: "sixty", 70: "seventy", 80: "eighty", 90: "ninety"}

def number_to_words(n):
    if 1 <= n < 10:
        return unit_words[n]
    elif 10 <= n < 20:
        return teen_words[n]
    elif 20 <= n < 100:
        tens, below_ten = divmod(n, 10)
        return tens_words[tens * 10] + (unit_words[below_ten] if below_ten else "")
    elif 100 <= n < 1000:
        hundreds, below_hundred = divmod(n, 100)
        result = unit_words[hundreds] + "hundred"
        if below_hundred:
            result += "and" + number_to_words(below_hundred)
        return result
    elif n == 1000:
        return "onethousand"
    else:
        return ""

total_letters = sum(len(number_to_words(i)) for i in range(1, 1001))
print(total_letters)

