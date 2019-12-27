# n = 2
# while n < 12:
#     print(n)
#     n += 2
# print("Goodbye!")

# print("Hello!")
# n = 10
# while n >= 2:
#     print(n)
#     n -= 2
#
# school = 'Massachusetts Institute of Technology'
# numVowels = 0
# numCons = 0
#
# for char in school:
#     if char == 'a' or char == 'e' or char == 'i' \
#        or char == 'o' or char == 'u':
#         numVowels += 1
#     elif char == 'o' or char == 'M':
#         print(char)
#     else:
#         numCons -= 1
#
# print('numVowels is: ' + str(numVowels))
# print('numCons is: ' + str(numCons))

# """
# Problem 1
# Assume s is a string of lower case characters. Write a program
# that counts up the number of vowels contained in the string s. Valid vowels
# are: 'a', 'e', 'i', 'o', and 'u'. For example, if s = 'azcbobobegghakl',
# your program should print: Number of vowels: 5
# """
#
# s = "some stringaaui"
# count = 0
# for word in s:
#     if word == "a" or word == "e" or word == "i" or word == "o" or word == "u":
#         count += 1
# print("Number of vowels:", count)

"""
Problem 2 
Assume s is a string of lower case characters. Write a program 
that prints the number of times the string 'bob' occurs in s. For example, 
if s = 'azcbobobegghakl', then your program should print: Number of times bob 
occurs is: 2 
"""
# s = "azcbobobegghabobklbob"
# bob = 0
# for position in range(len(s)):
#     if "bob" in s[position:position + 3]:
#         bob += 1
# print("Number of times bob occurs is:", bob)


"""
Problem 3
Assume s is a string of lower case characters.
Write a program that prints the longest substring of s in which the letters 
occur in alphabetical order. For example, if s = 'azcbobobegghakl', then your 
program should print

Longest substring in alphabetical order is: beggh
In the case of ties, print the first substring. For example, if s = 'abcbcd', 
then your program should print

Longest substring in alphabetical order is: abc
"""
s = "azcbobobeabcdgghaklabcdefghi"
# longest = ""
# for index in range(len(s)):
#     long = s[index]
#     for letter in s[index + 1:]:
#         if long[-1] <= letter:
#             long += letter
#         else:
#             break
#     if len(long) > len(longest):
#         longest = long
# print(longest)

cur = lng = s[0]
for c in s[1:]:
    if c < cur[-1]:
        if len(cur) > len(lng):
            lng = cur
        cur = c
    else:
        cur += c
print("Longest substring in alphabetical order is:", lng)
