# from nltk.classify import NaiveBayesClassifier
# from nltk.corpus import subjectivity
# from nltk.sentiment import SentimentAnalyzer
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk.sentiment.util import *
from collections import Counter 

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
    prewar={'compound':0, 'neg':0, 'neu':0, 'pos':0}
    postwar={'compound':0, 'neg':0, 'neu':0, 'pos':0}
    pre_count = 145
    post_count = 149
    print("Pre War Assessment")
    for sentence in pre_para:
        sid = SentimentIntensityAnalyzer()
        print(sentence)
        ss = sid.polarity_scores(sentence)

        prewar = dict(Counter(prewar) + Counter(ss))

        for k in sorted(ss):
            print('{0}: {1}, '.format(k, ss[k]), end='')
        print()


    print("Post War Assessment")
    for sentence in post_para:
        sid = SentimentIntensityAnalyzer()
        print(sentence)
        ss = sid.polarity_scores(sentence)

        postwar = dict(Counter(postwar) + Counter(ss))

        for k in sorted(ss):
            print('{0}: {1}, '.format(k, ss[k]), end='')
        print()

    for key in prewar:
        print(key)
        print(prewar[key])
        prewar[key] = prewar[key] / pre_count
        
    for key in postwar:
        print(key)
        print(postwar[key])
        postwar[key] = postwar[key] / post_count

    print("Prewar")
    prewar.pop('compound')
    for k in sorted(prewar):
        print('{0}: {1}, '.format(k, prewar[k]), end='')
    
    print()

    print("Postwar")
    for k in sorted(postwar):
        print('{0}: {1}, '.format(k, postwar[k]), end='')

if __name__ == "__main__":
    main()
