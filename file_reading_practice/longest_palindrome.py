"""
## 5. Longest Palindrome in the File  *(Hard)*

=================================================
LONGEST PALINDROME
=================================================

Problem Statement:
Read the text file `sowpods.txt` and find the
LONGEST PALINDROME word in the file.

If multiple palindromes share the maximum
length, print ALL of them.

-------------------------------------------------
Input Example (sowpods.txt sample):
level
radar
noon
civic
deified
racecar
rotator
malayalam

Output Example:
Longest palindrome length: 9
malayalam

-------------------------------------------------
Explanation:
Lengths of the palindromes in the sample:
   level    -> 5
   radar    -> 5
   noon     -> 4
   civic    -> 5
   deified  -> 7
   racecar  -> 7
   rotator  -> 7
   malayalam -> 9
The longest is "malayalam" with 9 characters.
=================================================

"""
def is_palindrome(word):
    rev = word[::-1]

    if word == rev:
        return word


path = (r"C:\Users\D ROSHAN\OneDrive\Documents\GitHub\python-file-handling-Roshan-21v\file_reading_practice\sowpods.txt")
longest_palindrome = 0
palindromes = []

f = open(path, "r")
words = f.readlines()

for line in words:
    word = line.strip()

    if is_palindrome(word):

        if len(word) > longest_palindrome:
            longest_palindrome = len(word)
            palindromes = [word]

        elif len(word) == longest_palindrome:
            palindromes.append(word)

f.close()

print(f"Longest palindrome length: {longest_palindrome}")

for word in palindromes:
    print(word)