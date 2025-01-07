import re
import collections
import os

def count_words(path):
    # Get the directory of the current script
    script_dir = os.path.dirname(os.path.abspath(__file__))

    # Create full path to the file
    path = os.path.join(script_dir, path)
    
    with open(path, 'r', encoding='utf-8') as file:
        all_words = re.findall(r"[0-9a-zA-Z-']+", file.read())
        all_words = [word.upper() for word in all_words]
        print(f'\nTotal Words: {len(all_words)}')

        word_counts = collections.Counter(all_words)

        print('\nTop 20 Words:')
        for word in word_counts.most_common(20):
            print(f'{word[0]}\t{word[1]}')


# commands used in solution video for reference
if __name__ == '__main__':
    count_words('shakespeare.txt')
