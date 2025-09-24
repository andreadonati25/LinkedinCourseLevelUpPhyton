import re
import collections

def count_unique(path):
    with open(path, 'r') as file:
        all_words = re.findall(r"[0-9a-zA-Z-']+", file.read())
        all_words = [word.upper() for word in all_words]
        print(f"Total Words: {len(all_words)}")

        word_count = collections.Counter(all_words)

        for word in word_count.most_common(10):
            print(f"{word[0]}:\t{word[1]}")


count_unique("Ex10_LoremIpsum.txt")