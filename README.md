# SENTIMENT-ANALYSIS-WITH-NLP

COMPANY: CODETECH IT SOLUTIONS

NAME: DEVARASETTY SRI RANGA CHANDANA NAIDU

INTERN ID: CT06DF182

DOMAIN: MACHINE LEARNING

BATCH DURATION: May 24th, 2025 to July 9th, 2025

MENTOR NAME: NEELA SANTHOSH KUMAR

PROJECT DESCRIPTION:

Sentiment Analysis is one of the most important applications of Natural Language Processing (NLP) that identifies whether a text has a positive, negative, or neutral sentiment. The aim of this project is to do sentiment analysis on Twitter data for a certain topic or event using Python and NLP libraries.

In this project, I created a sentiment analysis pipeline that scrapes tweets off Twitter with the snscrape module, pre-processes the text data, and analyzes the emotional tone of the tweets. The result is rendered using graphs and charts for easier interpretation.

 Tools and Technologies Used:
Python 3.10: The primary programming language utilized to implement all aspects of the project.

PyCharm: IDE used to develop, organize, and execute the Python code.

snscrape: A web scraper used to scrape Twitter data without the need for Twitter API access.

Matplotlib: A plot library employed for illustrating word frequency and sentiment distribution plots.

NLTK (Natural Language Toolkit): Employed for natural language preprocessing such as tokenization, stop-word removal, and possibly sentiment tagging.

String, Collections: Python built-in modules employed for text processing and determining word frequencies.

 Workflow Overview
Data Collection:

Twitter data was gathered by utilizing the snscrape module with a query (for example, tweets on "CoronaOutbreak").

The application does not need Twitter API keys, providing ease and speed in collecting public information.

Data Preprocessing:

The tweets are initially transformed to lowercase for standardization.

All punctuation is eliminated with Python's string.punctuation.

Tokenization is achieved by breaking down the text into separate words.

Common English stop words (such as "and", "the", "is") are eliminated to concentrate on significant content.

Sentiment Analysis:

By employing standard NLP methods, the words are matched against pre-determined lists of positive and negative words (or utilizing emotion lexicons).

The occurrence of positive, negative, or neutral words assists in categorizing the general sentiment of the tweets.

Visualization:

The final results of sentiment (such as how many positive vs. negative tweets) are represented by bar charts or pie charts using matplotlib.

Word clouds or frequency plots are also created to display which words are most frequently used in the data.

 Resources Used
In order to successfully execute this project, I depended on several learning resources and tools:

1. ChatGPT (OpenAI):
I utilized ChatGPT heavily for Python code writing and debugging, interpreting error messages (such as module compatibility problems), and getting step-by-step instructions on setting up the Python environments and resolving version issues.

It assisted in explaining how snscrape operates, writing efficient and clean Python code, and crafting the sentiment logic.

2. YouTube Tutorials:
Visual guides were essential in learning how to configure the PyCharm setup, install packages, and interact with Python virtual environments.

Ready-made code for sentiment analysis was also given on some channels, which I learned and then modified for my project.

3. Google & GeeksforGeeks:
GeeksforGeeks helped most in learning fundamental NLP principles such as tokenization, stemming, lemmatization, and stop-word removal.

I also gained knowledge about using Python libraries such as nltk and matplotlib from their articles and examples.

Stack Overflow threads resolved errors like ModuleNotFoundError and conflicts with Python versions.

OUTPUT:

<img width="665" alt="Image" src="https://github.com/user-attachments/assets/76e47f45-78dd-44dd-be75-17826c96d0cd" />
