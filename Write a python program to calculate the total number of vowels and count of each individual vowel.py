def count_vowels(string):
    vowels = "AEIOU"
    vowel_counts = {"A": 0, "E": 0, "I": 0, "O": 0, "U": 0}
    total_vowels = 0

    for char in string:
        if char.upper() in vowels:
            vowel_counts[char.upper()] += 1
            total_vowels += 1

    return total_vowels, vowel_counts

string = "Guvi Geeks Network Private Limited"
total_vowels, vowel_counts = count_vowels(string)

print("Total number of vowels:", total_vowels)

for vowel, count in vowel_counts.items():
    print("Count of", vowel + ": " + str(count))