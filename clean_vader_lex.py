__author__ = 'kennyjoseph'
import glob

all_identity_words = set()

for fil in glob.glob("/Users/kennyjoseph/git/thesis/thesis_work/identity_extraction/python/dictionaries/*/*identities*"):
    all_identity_words |= set([x.strip() for x in open(fil)])


vsent2 = open("vaderSentiment/vader_sentiment_lex_no_identities.txt","w")
for f in open("vaderSentiment/vader_sentiment_lexicon.txt"):
    if f.split("\t")[0] not in all_identity_words:
       vsent2.write(f)

vsent2.close()