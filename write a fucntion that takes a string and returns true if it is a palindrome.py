def is_palindrome(param):
    pass
def is_palindrome(s):
    s = s.replace(" ", "").lower()
    return s == s[::-1]


print(is_palindrome("bob"))
print(is_palindrome("builder"))