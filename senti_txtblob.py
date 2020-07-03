# pip install textblob vadersentiment

from textblob import TextBlob

analysis = TextBlob("TextBlob sure looks like it has some interesting features!")   #this converts the statement in a textblob object
# print(dir(analysis))    #what operations can we do with the object
# print(analysis.translate(to='es'))  #translates to spanish or any language code you give
# print(analysis.tags)
print(analysis.sentiment)
"""Polarity - The ratio of negative to postive words
    Subjectivity - it is a degree from zero to one,
    where zero is very objective and one is very subjective"""

pos_count = 0
pos_correct = 0

with open("positive.txt","r") as f:
    for line in f.read().split('\n'):
        analysis = TextBlob(line)

        # if analysis.sentiment.subjectivity < 0.3:
        if analysis.sentiment.subjectivity > 0.8:
            if analysis.sentiment.polarity > 0:
                pos_correct += 1
            pos_count +=1


neg_count = 0
neg_correct = 0

with open("negative.txt","r") as f:
    for line in f.read().split('\n'):
        analysis = TextBlob(line)
        # if analysis.sentiment.subjectivity < 0.3:
        if analysis.sentiment.subjectivity > 0.8:
            if analysis.sentiment.polarity <= 0:
                neg_correct += 1
            neg_count +=1

print("Positive accuracy = {}% via {} samples".format(pos_correct/pos_count*100.0, pos_count))
print("Negative accuracy = {}% via {} samples".format(neg_correct/neg_count*100.0, neg_count))
