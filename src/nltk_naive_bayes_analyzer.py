from sklearn.feature_extraction.text import CountVectorizer
from nltk.corpus import stopwords
import nltk
from sklearn.model_selection import train_test_split

from nltk.tokenize import wordpunct_tokenize

import math
import pandas as pd
import os
import pickle


nltk.download('punkt')
nltk.download('stopwords')

def pre_process(df):
    # Removes leading and trailing spaces and convert to lowercase:
    df['text_display'] = df['text_display'].str.strip().str.lower()

    # Replaces ' with empty string to join string such as I'll, I'm, etc
    df['text_display'] = df['text_display'].str.replace(
        '[\']+', '', regex=True)

    # Remove special characters:
    df['text_display'] = df['text_display'].str.replace(
        '[!~;.,’/<>()|\+\-\$%&#@\'"*\[\]?]+', ' ', regex=True)


def create_bag_of_words(df):

    # Creates a tuple like this:
    # (sentence, sentiment)
    # Currently disconsidering neutral sentiment 
    full_set = []
    for item in df.itertuples():
        # Item[1]: text_display. item[2]: sentiment
        full_set.append((item[1], item[2]))

    # print(full_set)

    stop_words = set(stopwords.words('english'))

    # Creates the vocabulary (a set containing all the unique words on all sentences)
    vocabulary = set()
    for passage in full_set:
        for word in wordpunct_tokenize(passage[0]):
            if not word in stop_words:
                vocabulary.add(word)

    # print(vocabulary)

    bag_of_words = []    
    for sentence_and_label in full_set:
        bow_item = create_bow_item(sentence_and_label, vocabulary)
        bag_of_words.append(bow_item)

    return (bag_of_words, vocabulary)

def create_bow_item(sentence_and_label, vocabulary):
    return ({word: (word in wordpunct_tokenize(sentence_and_label[0])) for word in vocabulary}, sentence_and_label[1])

def create_confusion_matrix(classifier, X_test):
  true_positives = 0
  true_negatives = 0
  false_positives = 0
  false_negatives = 0
  for (comment, tag) in X_test:
      guess = classifier.classify(comment)
      if guess == tag:
          if guess == 1:
            true_positives += 1
          elif guess == -1:
              true_negatives += 1
      else:
          if guess == 1:
            false_positives += 1
          elif guess == -1:
            false_negatives += 1
  print('true positives: ' + str(true_positives))
  print('true negatives: ' + str(true_negatives))
  print('false positives: ' + str(false_positives))
  print('false negatives: ' + str(false_negatives))

def run():
  comments_df = pd.read_csv(os.path.dirname(__file__) + '/csv/data-labeled.csv')

  pre_process(comments_df)
  (X, vocabulary) = create_bag_of_words(comments_df)

  train_test_division = math.floor(len(X)/2)

  X_train = X[train_test_division:]
  X_test = X[:train_test_division]

  classifier = nltk.NaiveBayesClassifier.train(X_train)
  
  print('accuracy')
  print(nltk.classify.accuracy(classifier, X_test))

  print('most informative features:')
  print(classifier.show_most_informative_features(5))

  create_confusion_matrix(classifier, X_test)
 
run()

