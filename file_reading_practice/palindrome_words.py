"""
## 4. Find All Palindrome Words  *(Medium)*

=================================================
PALINDROME WORDS
=================================================

Problem Statement:
Read the text file `sowpods.txt` and PRINT
every PALINDROME word (a word that reads the
same forwards and backwards).

Write a helper FUNCTION called `is_palindrome`
that takes a single word and returns True if
it is a palindrome, else False. Pass every
word in the file to this function ONE AT A
TIME.

-------------------------------------------------
Input Example (sowpods.txt sample):
level
radar
hello
noon
civic
python
deified
racecar
banana

Output Example:
level
radar
noon
civic
deified
racecar
Total palindromes: 6

-------------------------------------------------
Explanation:
- "level"    reversed -> "level"   -> palindrome
- "radar"    reversed -> "radar"   -> palindrome
- "hello"    reversed -> "olleh"   -> not
- "noon"     reversed -> "noon"    -> palindrome
- "civic"    reversed -> "civic"   -> palindrome
- "python"   reversed -> "nohtyp"  -> not
- "deified"  reversed -> "deified" -> palindrome
- "racecar"  reversed -> "racecar" -> palindrome
- "banana"   reversed -> "ananab"  -> not
=================================================

"""
path = (r"C:\Users\D ROSHAN\OneDrive\Documents\GitHub\python-file-handling-Roshan-21v\file_reading_practice\sowpods.txt")

count = 0

def is_palindrome(word):
    if word == word[::-1]:
        return True
    else:
        return False


file = open(path, "r")

for line in file:
    word = line.strip()

    if is_palindrome(word):
            print(word)
            count += 1


file.close()

print("Total palindromes:", count)   




    
