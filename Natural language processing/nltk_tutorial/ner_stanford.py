# -*- coding: utf-8 -*-
"""Stanford Named Entity Extraction"""

from nltk.tag import StanfordNERTagger
from nltk.tokenize import word_tokenize

def main():
    """Doc"""

    st_tagger = StanfordNERTagger('C:\\Users\\pesho\\AppData\\Local\\Programs\\Python\\Python36\\stanford-ner-2017-06-09\\classifiers\\english.all.3class.distsim.crf.ser.gz',
					                'C:\\Users\\pesho\\AppData\\Local\\Programs\\Python\\Python36\\stanford-ner-2017-06-09\\stanford-ner.jar',
					                encoding='utf-8')

    text = 'While in France, Christine Lagarde discussed short-term stimulus efforts in a recent interview with the Wall Street Journal.'

    tokenized_text = word_tokenize(text)
    classified_text = st_tagger.tag(tokenized_text)

    print(classified_text)

if __name__ == '__main__':
    main()
