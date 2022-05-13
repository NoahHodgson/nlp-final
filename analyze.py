# from nltk.classify import NaiveBayesClassifier
# from nltk.corpus import subjectivity
# from nltk.sentiment import SentimentAnalyzer
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk.sentiment.util import *

def main():
    print("Analyzing Ukraine News Articles via Semantic Analysis")
    # https://www.nltk.org/howto/sentiment.html
    with open("./ukrainepost.txt", encoding="utf8") as file_in:
        post_para = []
        for line in file_in:
            post_para.append(line.strip().lower())

    with open("./ukrainepre.txt", encoding="utf8") as file_in:
        pre_para = []
        for line in file_in:
            pre_para.append(line.strip().lower())

    '''Look into this: https://medium.com/edward-leoni/build-your-own-sentiment-analysis-classifier-with-nltk-ff4bd8744dc0'''
    for sentence in pre_para:
        print("Pre War Assessment")
        sid = SentimentIntensityAnalyzer()
        print(sentence)
        ss = sid.polarity_scores(sentence)
        for k in sorted(ss):
            print('{0}: {1}, '.format(k, ss[k]), end='')
        print()
    
    for sentence in post_para:
        print("Post War Assessment")
        sid = SentimentIntensityAnalyzer()
        print(sentence)
        ss = sid.polarity_scores(sentence)
        for k in sorted(ss):
            print('{0}: {1}, '.format(k, ss[k]), end='')
        print()

if __name__ == "__main__":
    main()
