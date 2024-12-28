# sort string in alphabetical order and return the sorted string with original capitalization
def my_sort_words(s):
    # split the string into words
    words = s.split()
    # sort the words in alphabetical order
    words.sort(key=lambda x: x.lower())
    # join the words back into a string
    return ' '.join(words)

if __name__ == '__main__':
    print(my_sort_words('hello world'))  # hello world
    print(my_sort_words('Hello World'))  # Hello world
    print(my_sort_words("Hello, Bart!"))  # Bart! Hello,
    print(my_sort_words("Hello, bart"))  # bart Hello,