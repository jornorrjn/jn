s = "MCMXCIV"

values = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
result = 0

for i in range(len(s)):
    current = values[s[i]]
    # if the next symbol is bigger, this one gets subtracted (like the I in IV)
    if i + 1 < len(s) and current < values[s[i + 1]]:
        result = result - current
    else:
        result = result + current

print(result)