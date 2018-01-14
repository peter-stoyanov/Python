"""Nltk default Named Entity Extractor"""

import os
import nltk

def main():
    """Docstring"""

    with open(os.getcwd() + "\\Natural language processing\\articles\\sampleArticle3.txt", 'r') as file:
        sample = file.read()

    # sentence segmenter
    sentences = nltk.sent_tokenize(sample)

    # word tokenizer
    tokenized_sentences = [nltk.word_tokenize(sentence) for sentence in sentences]

    # part-of-speech tagger
    tagged_sentences = [nltk.pos_tag(sentence) for sentence in tokenized_sentences]

    # named entities extraction
    chunked_sentences = nltk.ne_chunk_sents(tagged_sentences, binary=True)

    entity_names = []
    for tree in chunked_sentences:
        # Print results per sentence
        # print extract_entity_names(tree)

        entity_names.extend(extract_entity_names(tree))

    # Print all entity names
    #print entity_names

    # Print unique entity names
    print(set(entity_names))

def extract_entity_names(item):
    """Docstring"""

    entity_names = []

    if hasattr(item, 'label') and item.label:
        if item.label() == 'NE':
            entity_names.append(' '.join([child[0] for child in item]))
        else:
            for child in item:
                entity_names.extend(extract_entity_names(child))

    return entity_names

if __name__ == '__main__':
    main()
