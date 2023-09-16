def longest_common_substring(str1, str2):
    len1 = len(str1)
    len2 = len(str2)
    dp = [[0] * (len2 + 1) for _ in range(len1 + 1)]
    longest_length = 0
    longest_substring = ""
    for i in range(len1 + 1):
        for j in range(len2 + 1):
            if i == 0 or j == 0:
                dp[i][j] = 0
            elif str1[i - 1] == str2[j - 1]:
                dp[i][j] = dp[i-1][j-1] + 1
                if dp[i][j] > longest_length:
                    longest_length = dp[i][j]
                    longest_substring = str1[i - longest_length:i]
            else:
                dp[i][j] = 0

    return longest_substring
print(longest_common_substring("guvigeek", "bcdefghijk"))
print(longest_common_substring("xylophone", "xyz"))
print(longest_common_substring("programming", "program"))