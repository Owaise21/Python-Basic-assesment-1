def rem_vowel(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = [letter for letter in string if letter.lower() not in vowels]
    result = ''.join(result)
    print(result)



string = "Guvi Geeks Netowork Private Limited"
rem_vowel(string)
string = "Education"
rem_vowel(string)
