# Buat file reducer.py
%%writefile reducer.py
#!/usr/bin/env python3

import sys

current_word = None
current_count = 0
word = None

for line in sys.stdin:
    line = line.strip()
    word, count = line.split('\t')
    count = int(count)

    if current_word == word:
        current_count += count
    else:
        if current_word:
            print(f'{current_word}\t{current_count}')
        current_count = count
        current_word = word

if current_word == word:
    print(f'{current_word}\t{current_count}')
