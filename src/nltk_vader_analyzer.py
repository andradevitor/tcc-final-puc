import numpy as np
import pandas as pd
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import nltk
nltk.download('vader_lexicon')
import os


def check_polarity(doc):
    sid = SentimentIntensityAnalyzer()
    scores = sid.polarity_scores(doc)
    # print('{:+}: {}'.format(scores['compound'], doc))

    compound_score = scores['compound']
    if compound_score > 0.05:
        return [compound_score, 'positive']
    elif compound_score > -0.05:
        return [compound_score, 'neutral']
    else:
        return [compound_score, 'negative']

def run():
  df = pd.read_csv(os.path.dirname(__file__) + '/csv/data.csv')

  rows = []
  for comment in df['text_display']:
    class_number = None
    [score, classification] = check_polarity(
        comment)
    if classification == 'positive':
        class_number = 1
        row = [comment, class_number]
        rows.append(row)  
    elif classification == 'negative':
        class_number = -1
        row = [comment, class_number]
        rows.append(row)  
    # Discards neutral commentaries

  csv_path = os.path.dirname(__file__) + '/csv/data-labeled.csv'

  out_df = pd.DataFrame(rows, columns=['text_display','sentiment'])
  out_df.to_csv(csv_path, index=False)

run()
