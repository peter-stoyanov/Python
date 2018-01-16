# -*- coding: utf-8 -*-
"""Stanford Named Entity Extractor"""

import os
from itertools import groupby
from nltk.tag import StanfordNERTagger
from nltk.tokenize import word_tokenize

def main():
    """Stanford Named Entity Extractor"""

    # Change the path according to your system
    java_path = "C:\\Program Files\\Java\\jre1.8.0_151\\bin"
    os.environ['JAVAHOME'] = java_path

    stanford_classifier = 'D:\\stanford-ner-2017-06-09\\classifiers\\english.all.3class.distsim.crf.ser.gz'
    stanford_commetric_classifier = os.getcwd() + "\\Natural language processing\\Train Stanford NER Model\\ner-model-commetric.ser.gz"
    stanford_ner_path = 'D:\\stanford-ner-2017-06-09\\stanford-ner.jar'

    # Creating Tagger Object
    st_ner_tagger = StanfordNERTagger(stanford_classifier, stanford_ner_path, encoding='utf-8')

    with open(os.getcwd() + "\\Natural language processing\\articles\\sampleArticle3.txt", 'r') as file:
        sample = file.read()

    tokenized_text = word_tokenize(sample)

    classified_text = st_ner_tagger.tag(tokenized_text)

    # Stanford NER classifier will show 'John Snow' as two separate entities
    # => group adjacent entities of the same type
    entity_names = []
    for tag, chunk in groupby(classified_text, lambda x: x[1]):
        if tag != "O":
            # print("%-12s"%tag, " ".join(w for w, t in chunk))
            entity_names.append(tag + " " + " ".join(w for w, t in chunk))

    print(set(entity_names))

if __name__ == '__main__':
    main()
