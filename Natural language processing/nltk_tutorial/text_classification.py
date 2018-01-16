"""Train a basic naive text classificator"""

import random
import pickle
import os
import nltk
from nltk.corpus import movie_reviews

def main():
    """Train a basic naive text classificator"""

    documents = [(list(movie_reviews.words(fileid)), category)
                 for category in movie_reviews.categories()
                 for fileid in movie_reviews.fileids(category)]

    random.shuffle(documents)

    print(documents[1])

    all_words = []
    for word in movie_reviews.words():
        all_words.append(word.lower())

    all_words = nltk.FreqDist(all_words)

    print(all_words.most_common(15))
    print(all_words["stupid"])

    word_features = list(all_words.keys())[:3000]

    def find_features(document):
        """"find these top 3,000 words in our positive and negative documents"""
        words = set(document)
        features = {}
        for word in word_features:
            features[word] = (word in words)

        return features

    print((find_features(movie_reviews.words('neg/cv000_29416.txt'))))

    featuresets = [(find_features(rev), category) for (rev, category) in documents]

    # set that we'll train our classifier with
    training_set = featuresets[:1900]

    # set that we'll test against.
    testing_set = featuresets[1900:]

    # define, and train our classifier
    classifier = nltk.NaiveBayesClassifier.train(training_set)

    # # load trained classifier
    # classifier_f = open("naivebayes.pickle", "rb")
    # classifier = pickle.load(classifier_f)
    # classifier_f.close()

    # save the trained classifier for later use
    path = os.getcwd()
    save_classifier = open(path + '\\naivebayes.pickle', "wb")
    pickle.dump(classifier, save_classifier)
    save_classifier.close()

    # test it
    print("Classifier accuracy percent:", (nltk.classify.accuracy(classifier, testing_set))*100)

    classifier.show_most_informative_features(15)

if __name__ == '__main__':
    main()
