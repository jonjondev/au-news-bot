import requests
import random
import json

API_KEY = '0cc6cdacf3ce40d0ac51e4447aa11043'
url = 'https://newsapi.org/v2/top-headlines?country=au&category=general&apiKey=' + API_KEY

response = requests.get(url).json()
articles = response['articles']

titles = []
for article in articles:
    titles.append(article['title'].split(' - ', 1)[0])

descriptions = []
for description in descriptions:
    descriptions.append(description['description'])


def build_chain(text, chain = {}):
    words = text.split(' ')
    index = 1
    for word in words[index:]:
        key = words[index - 1]
        if key in chain:
            chain[key].append(word)
        else:
            chain[key] = [word]
        index += 1
    
    return chain

def generate_message(chain, count = 100):
    word1 = random.choice(list(chain.keys()))
    message = word1.capitalize()

    while len(message.split(' ')) < count:
        if word1 in chain:
            word2 = random.choice(chain[word1])
        else:
            return message
        word1 = word2
        message += ' ' + word2
    
    return message

lechain = {}

for title in titles:
    lechain = build_chain(title, lechain)

for desc in descriptions:
    lechain = build_chain(desc, lechain)

le = generate_message(lechain)

print(le)