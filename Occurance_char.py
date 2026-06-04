from collections import Counter

# Write a program to count occurrence of the character?

# 1 Using Counter function()
# str = "This is my input"
# char_count = Counter(str)
# print(char_count)
# O/P: Counter({'o': 5, ' ': 5, 'e': 2, 'l': 2, 'a': 2, 'y': 2, 'd': 2, 'H': 1, 'h': 1, 'w': 1, 'r': 1, 'u': 1, 'i': 1, 'n': 1, 'g': 1, 't': 1})

#2 using if else
# str1 = "Mississippi"
# occurance = {}
# for char in str1:
#     if char in occurance:
#         occurance[char] += 1
#     else:
#         occurance[char] = 1
# print(occurance)
# O/P: {'M': 1, 'i': 4, 's': 4, 'p': 2}


# Write a program to count occurance of specific character from string?

#1 Using Counter function()
# str = "Mississippi"
# char_to_count= 'p'
# occurance_count = str.count(char_to_count)
# print(f"The char '{char_to_count}' appears {occurance_count} times in string.")
# O/P: The char 'i' appears 4 times in string.

#2 Using if else
# abc = "Mississippi"
# char_to_count= 'i'
# occurance_count = 0
# for char in abc:
#     if char == char_to_count:
#         occurance_count +=1
# print(f"The char '{char_to_count}' appears {occurance_count} times in string.")
# O/P: The char 'i' appears 4 times in string.
