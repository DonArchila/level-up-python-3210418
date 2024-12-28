def is_palindrome(s):
  s = ''.join(char for char in s.upper() if 'A' <= char <= 'Z')
  return s == s[::-1]


if __name__ == '__main__':
  print(is_palindrome('hello world'))  # false
  print(is_palindrome("Go hang a salami, I'm a lasagna hog."))  # true
  print(is_palindrome('rac3 car'))  # true