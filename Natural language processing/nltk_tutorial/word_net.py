"""Doc"""

from nltk.corpus import wordnet

def main():
    """Doc"""
    syns = wordnet.synsets("program")
    # synset
    print(syns[0].name())
    # just the word
    print(syns[0].lemmas()[0].name())
    # definition of the synset
    print(syns[0].definition())
    # examples of use
    print(syns[0].examples())

    synonyms = []
    antonyms = []

    for syn in wordnet.synsets("good"):
        for l in syn.lemmas():
            synonyms.append(l.name())
            if l.antonyms():
                antonyms.append(l.antonyms()[0].name())

    print(set(synonyms))
    print(set(antonyms))

    word1 = wordnet.synset('ship.n.01')
    word2 = wordnet.synset('boat.n.01')
    print(word1.wup_similarity(word2))

if __name__ == '__main__':
    main()
