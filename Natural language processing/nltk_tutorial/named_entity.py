"""Doc"""

import nltk
from nltk.corpus import state_union
from nltk.tokenize import PunktSentenceTokenizer

def main():
    """Doc"""

    train_text = state_union.raw("2005-GWBush.txt")
    sample_text = state_union.raw("2006-GWBush.txt")

    custom_sent_tokenizer = PunktSentenceTokenizer(train_text)

    tokenized = custom_sent_tokenizer.tokenize(sample_text)

    process_content(tokenized)

def process_content(tokenized):
    """Docstring"""
    try:
        for i in tokenized[5:]:
            words = nltk.word_tokenize(i)
            tagged = nltk.pos_tag(words)
            named_ent = nltk.ne_chunk(tagged, binary=True)
            named_ent.draw()
    except Exception as exc:
        print(str(exc))

if __name__ == '__main__':
    main()
