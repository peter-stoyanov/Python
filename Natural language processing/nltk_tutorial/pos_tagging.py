"""Doc"""

import nltk
from nltk.corpus import state_union
from nltk.tokenize import PunktSentenceTokenizer

def main():
    """Doc"""

    train_text = state_union.raw("2005-GWBush.txt")
    sample_text = state_union.raw("2006-GWBush.txt")

    # train the Punkt tokenizer
    custom_sent_tokenizer = PunktSentenceTokenizer(train_text)
    # Then we can actually tokenize
    tokenized = custom_sent_tokenizer.tokenize(sample_text)
    process_content(tokenized)

def process_content(sentences):
    """Docstring"""
    try:
        for i in sentences[:5]:
            words = nltk.word_tokenize(i)
            tagged = nltk.pos_tag(words)
            print(tagged)

    except Exception as exc:
        print(str(exc))

if __name__ == '__main__':
    main()
