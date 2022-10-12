
import re

# pattern = re.compile("python")
# matcher = pattern.finditer("python is a easy , i love python")

# pattern = re.compile("ab")
# matcher = pattern.finditer("abaababa")
# matcher = re.finditer("ab", "abaababa")
# matcher = re.finditer("[abc]", "abaababa")
# matcher = re.finditer("\w", "abaababa")

matcher = re.finditer("a*", "abaababa")

count = 0
for m in matcher:
    count += 1
    print("start-{}, end-{}, group-{}".format
          (m.start(), m.end(), m.group()))
print()
print(count)
# group() method returns the matched item
# start() method returns the matched starting index
# end() method returns the matched ending index by adding one to it

# character classes

# [abc]- either a or b or c
# [^abc] - except a and b and c
# [a-z] - any lower case alphabet symbols
# [A-Z] - any upper case alphabet symbols
# [a-zA-Z] - any alphabet symbol
# [0-9] - any digit
# [a-zA-Z0-9] - any alpha numeric character
# [^a-zA-Z0-9] - other than alpha numeric character

# predefined character classes
# \s - space character
# \S - except space character
# \d - [0-9]
# \D - [^0-9]
# \w - [a-zA-Z0-9]
# \W - [^a-zA-Z0-9]
# . - every character

# quantifiers - number of occurrences

# a - exactly one "a"
# a+ - atleast one "a"
# a* - any number of "a" including zero number of "a" also
# a? - atmost one "a" (either one "a" or zero number of "a")
# a{n} - exactly n numbers of "a"
# a{m, n} - minimum m number of "a" and maximum n number of "a"
# a{2}a* - minimum two numbers of "a"
# ^a - it will check whether the target string starts with "a" or not
# a$ - it will check whether the target string ends with "a" or not

# important functions of re module
# match()
# fullmatch()
# search()
# findall()
# finditer()
# sub()
# subn()
# split()
# compile()

if __name__ == "__main__":
    print()
