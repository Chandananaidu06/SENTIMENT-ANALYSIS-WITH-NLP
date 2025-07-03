# SENTIMENT-ANALYSIS-WITH-NLP

COMPANY NAME: CODTECH IT SOLUTIONS

NAME: DEVARASETTY SRI RANGA CHANDANA NAIDU

INTERN ID: CT06DF182

DOMIAN: MACHINE LEARNING

DURATION: 6 WEEKS

MENTOR: NEELA SANTHOSH KUMAR

PROJECT DESCRIPTION:

This project involves building a machine learning model that performs sentiment analysis on customer reviews, particularly from the IMDB movie review dataset. The main objective of the project was to classify the reviews into positive or negative sentiments using Natural Language Processing (NLP) techniques and a machine learning algorithm known as Logistic Regression. Throughout this project, I gained hands-on experience in data preprocessing, feature engineering using TF-IDF vectorization, and model training and evaluation.

The dataset used in this project was the publicly available IMDB Dataset, which contains 50,000 labeled movie reviews. The dataset is balanced, with an equal number of positive and negative samples. Initially, I downloaded the dataset in ZIP format, extracted it, and saved it as a CSV file for further analysis using Jupyter Notebook, which I launched via the Anaconda distribution.

The first step in the process was data cleaning and preprocessing. Real-world text data is messy and unstructured, so I implemented a cleaning function (clean_text) to normalize the text. This included removing HTML tags, punctuation, numbers, and converting all words to lowercase. I also removed unnecessary whitespace and special characters using regular expressions. These steps are essential to ensure that the model receives clean and meaningful text data.

Following this, I used TF-IDF Vectorization (Term Frequency–Inverse Document Frequency) to convert the cleaned text into numerical feature vectors. Unlike traditional Bag-of-Words models, TF-IDF helps in identifying important words in each review while reducing the influence of commonly used but less informative words like "the", "is", or "and". This significantly improved the model's ability to distinguish between sentiments.

After transforming the data into numerical format, I split the dataset into training and testing sets using an 80:20 ratio. Then, I applied the Logistic Regression algorithm—a simple yet powerful classification model well-suited for binary classification problems like sentiment analysis. The model was trained on the training data and evaluated on the test data using accuracy score, confusion matrix, and classification report metrics (which include precision, recall, and F1-score).

Additionally, I implemented a custom prediction feature, allowing users to enter a sentence (e.g., “The movie was absolutely fantastic!”), which the model would classify as either positive or negative. This feature showcases the model’s practical utility in real-time applications such as product review monitoring, social media sentiment tracking, and customer support systems.

RESOURCES USED:

To complete this project effectively, I made use of several learning and coding support resources:

ChatGPT: This AI-powered assistant was a core resource throughout the project. It helped clarify concepts like TF-IDF, logistic regression, regular expressions, and evaluation metrics. I used ChatGPT to debug code, understand errors, and receive suggestions for improving data preprocessing and model performance.

YouTube Tutorials: I watched multiple YouTube videos that explained sentiment analysis, TF-IDF vectorization, and machine learning pipelines in Python. These visual demonstrations were particularly helpful in understanding the step-by-step process and best practices followed by professionals in real-world projects.

Google & Stack Overflow: I used Google extensively to explore documentation and resolve specific implementation challenges. Stack Overflow was especially helpful for understanding error messages and learning about vectorizer parameters, model fitting issues, and plotting confusion matrices.

Anaconda Navigator & Jupyter Notebook: I used the Anaconda distribution to manage the Python environment and launch Jupyter Notebook, which served as the interactive platform for coding, visualizing data, and documenting all results in a structured format.

![Image](https://github.com/user-attachments/assets/88c5e8fd-d161-4728-a29b-11775db1f1c2)

