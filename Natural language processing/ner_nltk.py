"""Nltk default Named Entity Extractor"""

import os
import nltk

def main():
    """Nltk default Named Entity Extractor"""

    with open(os.getcwd() + "\\Natural language processing\\articles\\sampleArticle4.txt", 'r') as file:
        sample = file.read()

    # sentence segmenter
    sentences = nltk.sent_tokenize(sample)

    # word tokenizer
    tokenized_sentences = [nltk.word_tokenize(sentence) for sentence in sentences]

    # part-of-speech tagger
    tagged_sentences = [nltk.pos_tag(sentence) for sentence in tokenized_sentences]

    # named entities extraction
    chunked_sentences = nltk.ne_chunk_sents(tagged_sentences)

    entity_names = []
    for tree in chunked_sentences:
        
        # print(tree)
        entity_names.extend(extract_entity_names(tree))

    # Print unique entity names
    print(set(entity_names))

def extract_entity_names(item):
    """Docstring"""

    entity_names = []

    # if hasattr(item, 'label') and item.label:
    #     if item.label() == 'NE':
    #         entity_names.append(' '.join([child[0] for child in item]))
    #     else:
    #         for child in item:
    #             entity_names.extend(extract_entity_names(child))

    if hasattr(item, 'label') and item.label:
        if (
                item.label() == 'ORGANIZATION' or
                item.label() == 'PERSON' or
                item.label() == 'LOCATION' or
                item.label() == 'DATE' or
                item.label() == 'TIME' or
                item.label() == 'MONEY' or
                item.label() == 'PERCENT' or
                item.label() == 'FACILITY' or
                item.label() == 'GPE'
        ):
            entity_names.append(item.label() + ' ' + ' '.join([child[0] for child in item]))
        else:
            for child in item:
                entity_names.extend(extract_entity_names(child))

    return entity_names

if __name__ == '__main__':
    main()
