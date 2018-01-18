#!/usr/bin/python
"""Provides a way to load more than one NER taggers"""

from nltk.tag.stanford import StanfordNERTagger

class NERComboTagger(StanfordNERTagger):

  def __init__(self, *args, **kwargs):
    self.stanford_ner_models = kwargs['stanford_ner_models']
    kwargs.pop("stanford_ner_models")
    super(NERComboTagger,self).__init__(*args, **kwargs)

  @property
  def _cmd(self):
    return ['edu.stanford.nlp.ie.NERClassifierCombiner',
            '-ner.model',
            self.stanford_ner_models,
            '-textFile',
            self._input_file_path,
            '-outputFormat',
            self._FORMAT,
            '-tokenizerFactory',
            'edu.stanford.nlp.process.WhitespaceTokenizer',
            '-tokenizerOptions',
            '\"tokenizeNLs=false\"']