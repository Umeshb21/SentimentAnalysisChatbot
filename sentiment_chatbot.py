import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
nltk.download('vader_lexicon')
analyzer = SentimentIntensityAnalyzer()
def analyze_sentiment(text):
sentiment = analyzer.polarity_scores(text)
if sentiment['compound'] >= 0.05:
  return "Positive"
elif sentiment['compound'] <= -0.05:
  return "Negative"
else:
  return "Neutral"
responses = {
  "positive": "Positive Statement",
  "negative": "Negative Statement",
  "neutral": "Neutral Statement",
  "farewell": "Goodbye! Feel free to return if you have more questions."
}
while True:
  user_input = input("You: ").strip().lower()
  if user_input == 'exit':
    print(responses['farewell'])
    break
  sentiment = analyze_sentiment(user_input)
  if sentiment == 'Positive':
    print("Chatbot: " + responses['positive'])
  elif sentiment == 'Negative':
    print("Chatbot: " + responses['negative'])
  else:
    print("Chatbot: " + responses['neutral'])
