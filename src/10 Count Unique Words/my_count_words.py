# function, `count_words()`, that takes the path to a text file as the input argument and prints the total number of words in the file, as well as the top 20 most frequently used words and how many times each of them occurs.
import re
import collections
import os

def count_words(file):
    
    # Get the directory of the current script
    script_dir = os.path.dirname(os.path.abspath(__file__))

    # Create full path to the file
    file_path = os.path.join(script_dir, file)

    with open(file_path) as file:
        all_words = re.findall(r"[0-9a-zA-Z-']+", file.read())
        all_words = [word.upper() for word in all_words]
        print(f'\nTotal Words: {len(all_words)}')

        word_counts = collections.Counter(all_words)

        print('\nTop 20 Words:')
        for word in word_counts.most_common(20):
            print(f'{word[0]}\t{word[1]}')

if __name__ == '__main__':
    count_words('shakespeare.txt')