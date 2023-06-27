
from textblob import TextBlob
from newspaper import Article

link = 'https://www.history.com/topics/21st-century/9-11-attacks'
article = Article(link)

article.download()
article.parse() #removes html
article.nlp() #prepares for natural language processing

text = article.summary
print(text)

blob = TextBlob(text)
sentiment = blob.sentiment.polarity 
print(sentiment)