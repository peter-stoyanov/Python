"""Doc"""

from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize

def main():
    """Doc"""

    stemmer = PorterStemmer()

    example_words = ["python", "pythoner", "pythoning", "pythoned", "pythonly"]

    for word in example_words:
        print(stemmer.stem(word))

    new_text = "It is important to by very pythonly while you are pythoning with python. All pythoners have pythoned poorly at least once."

    words = word_tokenize(new_text)

    for word in words:
        print(stemmer.stem(word))

if __name__ == '__main__':
    main()
