"""Doc"""

from nltk.tokenize import sent_tokenize, word_tokenize

def main():
    """Doc"""

    example_text = 'Hello Mr. Smith, how are you doing today? The weather is great, and Python is awesome. The sky is pinkish-blue. You shouldn"t eat cardboard.'

    print(sent_tokenize(example_text))
    print(word_tokenize(example_text))

if __name__ == '__main__':
    main()
