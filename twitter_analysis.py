import string
from collections import Counter
import matplotlib.pyplot as plt
import snscrape.modules.twitter as sntwitter


query = "CoronaOutbreak since:2020-01-01 until:2020-04-01"
tweets = []
for i, tweet in enumerate(sntwitter.TwitterSearchScraper(query).get_items()):
    if i > 1000:
        break
    tweets.append(tweet.content)


text = " ".join(tweets)


lower_case = text.lower()
cleaned_text = lower_case.translate(str.maketrans('', '', string.punctuation))
tokenized_words = cleaned_text.split()


stop_words = ["i", "me", "my", "myself", "we", "our", "you", "your", "he", "him", "she", "it", "they", "them",
              "what", "which", "who", "this", "that", "am", "is", "are", "was", "were", "be", "been", "have",
              "has", "had", "do", "does", "did", "a", "an", "the", "and", "but", "if", "or", "because", "as",
              "until", "of", "at", "by", "for", "with", "about", "against", "between", "into", "through", "during",
              "before", "after", "above", "below", "to", "from", "up", "down", "in", "out", "on", "off", "over", "under",
              "again", "further", "then", "once", "here", "there", "when", "where", "why", "how", "all", "any", "both",
              "each", "few", "more", "most", "other", "some", "such", "no", "nor", "not", "only", "own", "same", "so",
              "than", "too", "very", "can", "will", "just", "don", "should", "now"]


final_words = [word for word in tokenized_words if word not in stop_words]


emotion_list = []
with open('emotions.txt', 'r') as file:
    for line in file:
        clear_line = line.replace("\n", '').replace(",", '').replace("'", '').strip()
        word, emotion = clear_line.split(':')
        if word in final_words:
            emotion_list.append(emotion)


w = Counter(emotion_list)
print(w)


fig, ax1 = plt.subplots()
ax1.bar(w.keys(), w.values())
fig.autofmt_xdate()
plt.savefig('graph.png')
plt.show()
