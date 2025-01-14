import random
import os

def load_diceware_wordlist():
  wordlist = {}

  # Get the directory of the current script
  script_dir = os.path.dirname(os.path.abspath(__file__))
  file_path = os.path.join(script_dir, 'diceware.wordlist.asc')

  with open(file_path, 'r') as file:
    lines = file.readlines()[2:7778]
    for line in lines:
      if line.strip() and not line.startswith('#'):
        key, word = line.split()
        wordlist[key] = word
  return wordlist

def generate_passphrase(num_words):
  wordlist = load_diceware_wordlist()
  passphrase = []
  for _ in range(num_words):
    dice_roll = ''.join(str(random.randint(1, 6)) for _ in range(5))
    passphrase.append(wordlist[dice_roll])
  return ' '.join(passphrase)

# Example usage:
# print(generate_passphrase(5))

if __name__ == '__main__':
  print(generate_passphrase(5))  # Output: 'daisy miami krafty greek gouda'
  print(generate_passphrase(6))  # Output: 'sassy