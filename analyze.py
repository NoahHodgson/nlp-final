# from nltk.classify import NaiveBayesClassifier
# from nltk.corpus import subjectivity
# from nltk.sentiment import SentimentAnalyzer
from calendar import c
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
    prewar={'compound':.0, 'neg':.0, 'neu':.0, 'pos':.0}
    postwar={'compound':.0, 'neg':.0, 'neu':.0, 'pos':.0}

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
    last = 0
    for sentence in post_para:
        sid = SentimentIntensityAnalyzer()
        print(sentence)
        sd = sid.polarity_scores(sentence)
        postwar = dict(Counter(postwar) + Counter(sd))

        for k in sorted(sd):
            print('{0}: {1}, '.format(k, sd[k]), end='')

        postwar['compound'] = postwar.get('compound', last)
        last = postwar['compound']
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
    for k in sorted(prewar):
        print('{0}: {1}, '.format(k, prewar[k]), end='')
    
    print()

    print("Postwar")
    for k in sorted(postwar):
        print('{0}: {1}, '.format(k, postwar[k]), end='')


    '''Next Part'''
    with open("./zelenskyPost.txt", encoding="utf8") as file_in:
        post_para = []
        for line in file_in:
            post_para.append(line.strip().lower())

    with open("./zelenskyPre.txt", encoding="utf8") as file_in:
        pre_para = []
        for line in file_in:
            pre_para.append(line.strip().lower())

    pre_para = ' '.join(pre_para)
    post_para = ' '.join(post_para)
    pre_para = pre_para.split('}')
    post_para = post_para.split('}')
    threePre = []
    threePost = []

    for story in pre_para:
        threePre.append(story.split('.'))
    
    for story in post_para:
        threePost.append(story.split('.'))

    print(threePre)
    print(threePost)
    print()

    prewar1={'compound':.0, 'neg':.0, 'neu':.0, 'pos':.0}
    prewar2={'compound':.0, 'neg':.0, 'neu':.0, 'pos':.0}
    prewar3={'compound':.0, 'neg':.0, 'neu':.0, 'pos':.0}

    last = 0
    for sentence in threePre[0]:
        sid = SentimentIntensityAnalyzer()
        print(sentence)
        sd = sid.polarity_scores(sentence)
        prewar1 = dict(Counter(prewar1) + Counter(sd))

        for k in sorted(sd):
            print('{0}: {1}, '.format(k, sd[k]), end='')

        prewar1['compound'] = prewar1.get('compound', last)
        last = prewar1['compound']
        print()

    last = 0
    for sentence in threePre[1]:
        sid = SentimentIntensityAnalyzer()
        print(sentence)
        sd = sid.polarity_scores(sentence)
        prewar2 = dict(Counter(prewar2) + Counter(sd))

        for k in sorted(sd):
            print('{0}: {1}, '.format(k, sd[k]), end='')

        prewar2['compound'] = prewar2.get('compound', last)
        last = prewar2['compound']
        print()

    last = 0
    for sentence in threePre[2]:
        sid = SentimentIntensityAnalyzer()
        print(sentence)
        sd = sid.polarity_scores(sentence)
        prewar3 = dict(Counter(prewar3) + Counter(sd))

        for k in sorted(sd):
            print('{0}: {1}, '.format(k, sd[k]), end='')

        prewar3['compound'] = prewar3.get('compound', last)
        last = prewar3['compound']
        print()

    postwar1={'compound':.0, 'neg':.0, 'neu':.0, 'pos':.0}
    postwar2={'compound':.0, 'neg':.0, 'neu':.0, 'pos':.0}
    postwar3={'compound':.0, 'neg':.0, 'neu':.0, 'pos':.0}

    for sentence in threePost[0]:
        sid = SentimentIntensityAnalyzer()
        print(sentence)
        sd = sid.polarity_scores(sentence)
        postwar1 = dict(Counter(postwar1) + Counter(sd))

        for k in sorted(sd):
            print('{0}: {1}, '.format(k, sd[k]), end='')

        postwar1['compound'] = postwar1.get('compound', last)
        last = postwar1['compound']
        print()

    for sentence in threePost[1]:
        sid = SentimentIntensityAnalyzer()
        print(sentence)
        sd = sid.polarity_scores(sentence)
        postwar2 = dict(Counter(postwar2) + Counter(sd))

        for k in sorted(sd):
            print('{0}: {1}, '.format(k, sd[k]), end='')

        postwar2['compound'] = postwar2.get('compound', last)
        last = postwar2['compound']
        print()
    
    for sentence in threePost[2]:
        sid = SentimentIntensityAnalyzer()
        print(sentence)
        sd = sid.polarity_scores(sentence)
        postwar3 = dict(Counter(postwar3) + Counter(sd))

        for k in sorted(sd):
            print('{0}: {1}, '.format(k, sd[k]), end='')

        postwar3['compound'] = postwar3.get('compound', last)
        last = postwar3['compound']
        print()

    


if __name__ == "__main__":
    main()
