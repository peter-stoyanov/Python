"""Doc"""

from nltk.stem import WordNetLemmatizer

def main():
    """Doc"""

    lemmatizer = WordNetLemmatizer()

    print(lemmatizer.lemmatize("cats"))
    print(lemmatizer.lemmatize("cacti"))
    print(lemmatizer.lemmatize("geese"))
    print(lemmatizer.lemmatize("rocks"))
    print(lemmatizer.lemmatize("python"))
    print(lemmatizer.lemmatize("better", pos="a"))
    print(lemmatizer.lemmatize("best", pos="a"))
    print(lemmatizer.lemmatize("run"))
    print(lemmatizer.lemmatize("run", 'v'))

if __name__ == '__main__':
    main()
