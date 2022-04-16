# Youtube comment sentiment analysis

## Setting up
### Setting up the virtualenv:

```
$ pip install virtualenv
$ virtualenv venv
$ source venv/bin/activate # OR, depending on your version:
$ source venv/Scripts/activate 
```

### Freezing the environment into requirements.txt

```
$ python -m pip freeze > requirements.txt
```

### Installing dependencies from requirements.txt

```
$ pip install -r requirements.txt
```

## Fetching data:
You must export your Youtube API KEY to the terminal where you will run the data_collector. Replace xyz123 with your api key
```
$ export YOUTUBE_API_KEY=xyz123
$ python src/data_collector.py
```

## Running VADER for first database classification
```
$ python src/nltk_vader_analyzer.py
```

## Train and validate Naive Bayes model:
```
$ python src/nltk_naive_bayes_analyzer.py
```
