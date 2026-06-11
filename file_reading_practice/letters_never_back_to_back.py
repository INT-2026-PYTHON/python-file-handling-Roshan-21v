"""
## 2. Alphabets That Never Appear Back-to-Back  *(Medium)*

=================================================
ALPHABETS NEVER IN SEQUENCE
=================================================

Problem Statement:
Read the text file `sowpods.txt` and PRINT
every alphabet letter that:
   - APPEARS at least once in the words of
     the file, AND
   - NEVER appears TWICE IN A ROW (back-to-back)
     in ANY word of the file.

Letters that never appear in the file at all
should NOT be in the answer. Letters that
appear back-to-back at least once (like the
'u' in "vacuum") should also be excluded.

-------------------------------------------------
Input Example (sowpods.txt sample):
aardvark
hello
buzz
moon
puppy

Output Example:
Letters that never appear back-to-back:
['b', 'd', 'e', 'h', 'k', 'm', 'n', 'r', 'u', 'v', 'y']

-------------------------------------------------
Explanation:
Letters seen anywhere in the sample:
   aardvark -> a, r, d, v, k
   hello    -> h, e, l, o
   buzz     -> b, u, z
   moon     -> m, o, n
   puppy    -> p, u, y
   seen    = {a, b, d, e, h, k, l, m, n, o,
              p, r, u, v, y, z}

Letters that ever appear back-to-back:
   aa (aardvark), ll (hello), zz (buzz),
   oo (moon),     pp (puppy)
   doubled = {a, l, z, o, p}

Answer = seen - doubled
       = {b, d, e, h, k, m, n, r, u, v, y}
Sorted -> ['b', 'd', 'e', 'h', 'k', 'm', 'n',
           'r', 'u', 'v', 'y']
=================================================

"""
path = (r"C:\Users\D ROSHAN\OneDrive\Documents\GitHub\python-file-handling-Roshan-21v\file_reading_practice\sowpods.txt")

letters = []
repeated = []

f = open(path, "r")
words = f.readlines()

for line in words:
    word = line.strip().lower()

    # STEP 1: collect all letters
    for ch in word:
        if ch.isalpha():
            if ch not in letters:
                letters.append(ch)

    # STEP 2: find consecutive repeated letters
    for i in range(len(word) - 1):
        if word[i] == word[i + 1]:
            if word[i] not in repeated:
                repeated.append(word[i])

f.close()

result = []

print("Letters that never appear back-to-back:")
# STEP 3: print valid letters
for ch in sorted(letters):
    if ch not in repeated:
        result.append(ch)
        
        
print(result)