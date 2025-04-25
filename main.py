
def main():
  with open("books/frankenstein.txt") as b:
    file_contents = b.read()
    print(file_contents)

def countWords():
  with open("books/frankenstein.txt") as b:
    file_contents = b.read()
    file_words = file_contents.split()
    num_of_words = 0
    for w in file_words:
      num_of_words += 1
    print(num_of_words)


if __name__ == '__main__':
  main()
  countWords()