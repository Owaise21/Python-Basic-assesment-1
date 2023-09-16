def is_anagram(str1, str2):
    str1 = str1.lower().replace(" ", "")
    str2 = str2.lower().replace(" ", "")
    return sorted(str1) == sorted(str2)
print(is_anagram("listen", "silent"))
print(is_anagram("hello", "world"))
print(is_anagram("rail safety", "fairy tales"))