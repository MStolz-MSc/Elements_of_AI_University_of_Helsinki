"""
Finding the most similar pair of lines and using the tf-idf representation.
"""

import numpy as np
import math

text = '''Humpty Dumpty sat on a wall
Humpty Dumpty had a great fall
all the king's horses and all the king's men
couldn't put Humpty together again'''

def find_nearest_pair(data):
    data = np.array(data)
    N = len(data)
    dist = np.empty((N, N), dtype=np.float)
    for i in range(N):
        for j in range(N):
            d = 0
            for n in range(len(data[0])):
                d += abs(data[i][n] - data[j][n])
            dist[i][j] = d
            if d == 0:
                dist[i][j] = np.inf
     
    print("The closest pair of lines is:")            
    print(np.unravel_index(np.argmin(dist), dist.shape))


def main(text):
    print("The closest pair of lines of the following text will be identified:\n")
    print(text, "\n")
    # splitting text in lines and words. Listing documents/lines with lists of words
    docs = [line.split() for line in text.splitlines()]
    N = len(docs) # number of documents
    vocabulary = list(set(text.split())) # unique words in text
    
    tf = {} # term frequency {'word':[frequency of doc1, etc.]}
    df = {} # document frequency {'word':[frequency]}
    for word in vocabulary: # tf and df score for every word
        tf[word] = [doc.count(word)/len(doc) for doc in docs] 
        df[word] = sum([word in doc for doc in docs])/N       

    tfidf = []
    for doc_index, doc in enumerate(docs):
        score_list = []
        for word in vocabulary:
            score = tf[word][doc_index] * math.log(1/df[word],10)
            score_list.append(score)
        tfidf.append(score_list)
    #print(tfidf)
    # Calculating the distance between each line (tfidf-score) and selecting closest pair
    find_nearest_pair(tfidf)

main(text)
