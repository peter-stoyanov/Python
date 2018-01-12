import nltk
 
# tagged_sentences = nltk.corpus.brown.tagged_sents()
tagged_sentences = nltk.corpus.treebank.tagged_sents()
 
print(str(tagged_sentences[0]))
print("Tagged sentences: ", len(tagged_sentences))
print("Tagged words:", len(nltk.corpus.brown.tagged_words()))
 
# [(u'Pierre', u'NNP'), (u'Vinken', u'NNP'), (u',', u','), (u'61', u'CD'), (u'years', u'NNS'), (u'old', u'JJ'), (u',', u','), (u'will', u'MD'), (u'join', u'VB'), (u'the', u'DT'), (u'board', u'NN'), (u'as', u'IN'), (u'a', u'DT'), (u'nonexecutive', u'JJ')(u'director', u'NN'), (u'Nov.', u'NNP'), (u'29', u'CD'), (u'.', u'.')]
# Tagged sentences:  3914
# Tagged words: 1161192