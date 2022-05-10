from nltk.classify import NaiveBayesClassifier
from nltk.corpus import subjectivity
from nltk.sentiment import SentimentAnalyzer
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk.sentiment.util import *

def main():
    print("Analyzing Ukraine News Articles via Semantic Analysis")
    # https://www.nltk.org/howto/sentiment.html
    '''
    code below is for using your own training and tag set
    n_instances = 100
    subj_docs = [(sent, 'subj') for sent in subjectivity.sents(categories='subj')[:n_instances]]
    obj_docs = [(sent, 'obj') for sent in subjectivity.sents(categories='obj')[:n_instances]]
    # Sub out training documents with the BBC politics files
    train_subj_docs = subj_docs[:80]
    test_subj_docs = subj_docs[80:100]
    train_obj_docs = obj_docs[:80]
    test_obj_docs = obj_docs[80:100]
    training_docs = train_subj_docs+train_obj_docs
    testing_docs = test_subj_docs+test_obj_docs
    sentim_analyzer = SentimentAnalyzer()
    all_words_neg = sentim_analyzer.all_words([mark_negation(doc) for doc in training_docs])
    unigram_feats = sentim_analyzer.unigram_word_feats(all_words_neg, min_freq=4)
    print(f"Length of unigram_feats: {len(unigram_feats)}")
    sentim_analyzer.add_feat_extractor(extract_unigram_feats, unigrams=unigram_feats)
    training_set = sentim_analyzer.apply_features(training_docs)
    test_set = sentim_analyzer.apply_features(testing_docs)
    trainer = NaiveBayesClassifier.train
    classifier = sentim_analyzer.train(trainer, training_set)
    for key,value in sorted(sentim_analyzer.evaluate(test_set).items()):
        print('{0}: {1}'.format(key, value))
    '''
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
