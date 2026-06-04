from token import STRING

# Write a program to reverse a string

str = "mangesh"
str1 = str[::-1]
print(str1)

# Write a program to reverse a string & print in separate line?

str1 = "Hello how are you"
str2 = str1[::-1]
for word in str2.split():
    print(word)

# Write a program to reverse a string (str=’Hello is hi and hi is hello); it needs to reverse is.

abc = "Hello is hi and hi is hello"
word_to_reverse = "is"
# reversed_word = word_to_reverse.upper() #It convert string/word in upper case.
reversed_word = word_to_reverse[::-1]
xyz =abc.replace(word_to_reverse,reversed_word)
print(xyz)

#
