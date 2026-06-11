"""
## 6. Words in sonnet_words.txt but NOT in sowpods.txt  *(Hard)*

=================================================
WORDS UNIQUE TO THE SONNET
=================================================

Problem Statement:
Read the text files `sowpods.txt` and
`sonnet_words.txt`. PRINT every word that
appears in `sonnet_words.txt` but does NOT
appear in `sowpods.txt`.

This problem is about CHOOSING THE RIGHT DATA
STRUCTURE. If you check each sonnet word
against the SOWPODS list with a nested loop,
the work is O(N*M). Using SETS turns the
membership check into O(1), giving you an
overall O(N + M) algorithm.

-------------------------------------------------
Input Example:
sowpods.txt sample:
   thee
   love
   summer
   day
   eyes
   shall
   more

sonnet_words.txt sample:
   shall
   i
   compare
   thee
   to
   a
   summer
   day

Output Example:
Words in sonnet but not in sowpods:
['a', 'compare', 'i', 'to']
Total: 4

-------------------------------------------------
Explanation:
sonnet words -> {'shall', 'i', 'compare',
                 'thee', 'to', 'a', 'summer',
                 'day'}
sowpods set   -> {'thee', 'love', 'summer',
                  'day', 'eyes', 'shall',
                  'more'}
Difference (sonnet - sowpods)
              -> {'i', 'compare', 'to', 'a'}
After sorting -> ['a', 'compare', 'i', 'to'].
=================================================
"""

sowpods_path = ("C:\\Users\\D ROSHAN\\OneDrive\\Documents\\GitHub\\python-file-handling-Roshan-21v\\file_reading_practice\\sowpods.txt")
sonnet_path = (r"C:\Users\D ROSHAN\OneDrive\Documents\GitHub\python-file-handling-Roshan-21v\file_reading_practice\sonnet_words.txt")


sowpods_words = []
sonnet_words = []
unique_words = []

# read sowpods file
f = open(sowpods_path, "r")
sowpods_lines = f.readlines()

for line in sowpods_lines:
    word = line.strip().lower()

    if word not in sowpods_words:
        sowpods_words.append(word)

f.close()

# read sonnet file
f = open(sonnet_path, "r")
sonnet_lines = f.readlines()

for line in sonnet_lines:
    word = line.strip().lower()

    if word not in sonnet_words:
        sonnet_words.append(word)

f.close()


for word in sonnet_words:
    if word not in sowpods_words:
        unique_words.append(word)


print("Words in sonnet but not in sowpods:")

for word in sorted(unique_words):
    print(word)

print(f"Total:{len(unique_words)}")