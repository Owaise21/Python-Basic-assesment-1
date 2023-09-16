def find_most_frequent_character(string):
    char_counts = {}


    for char in string:
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1

    most_frequent_char = None
    max_count = 0
    for char, count in char_counts.items():
        if count > max_count:
            most_frequent_char = char
            max_count = count

    return most_frequent_char

print(find_most_frequent_character('parade'))
print(find_most_frequent_character('programming'))
print(find_most_frequent_character('jamming'))