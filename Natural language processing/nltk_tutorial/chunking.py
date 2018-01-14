"""Chunking - getting to a noun-phrase"""

import nltk
from nltk.corpus import state_union
from nltk.tokenize import PunktSentenceTokenizer

def main():
    """Docstring"""
    train_text = state_union.raw("2005-GWBush.txt")
    sample_text = state_union.raw("2006-GWBush.txt")

    custom_sent_tokenizer = PunktSentenceTokenizer(train_text)

    tokenized = custom_sent_tokenizer.tokenize(sample_text)

    process_content(tokenized)

def process_content(tokenized):
    """Docstring"""
    try:
        for i in tokenized:
            words = nltk.word_tokenize(i)
            tagged = nltk.pos_tag(words)
            chunk_gram = r"""Chunk: {<RB.?>*<VB.?>*<NNP>+<NN>?}"""
            # chinking = specify what to exclude when searching  } .. {
            chink_gram = r"""Chunk: {<.*>+}
                                    }<VB.?|IN|DT|TO>+{"""
            chunk_parser = nltk.RegexpParser(chunk_gram)
            chunked = chunk_parser.parse(tagged)
            chunked.draw()
    except Exception as exc:
        print(str(exc))

if __name__ == '__main__':
    main()
