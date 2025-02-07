
# bm25_demo.py
# import the lib: $ pip install rank_bm25

from rank_bm25 import BM25Okapi

# Create corpus of documents
corpus = [
  "Hello there good man!",
  "It is quite windy in London",
  "How is the weather today?"
]

# Tokenize each document
print ("content in doc_tokens:")
tokenized_corpus = []
for doc in corpus:
  doc_tokens = doc.split()
  print (doc_tokens)
  tokenized_corpus.append(doc_tokens)

print ("\ncontent in tokenized_corpus:")
print(tokenized_corpus)

# Create a BM25 index from the tokenized document corpus  
bm25 = BM25Okapi(tokenized_corpus)
print ("\ncorpus size:")
print(bm25.corpus_size)
print (" doc length:")
print(bm25.doc_len)

# Query the BM25 index
query = "windy London"
print ("\nquery:")
print(query)
tokenized_query = query.split(" ")

doc_scores = bm25.get_scores(tokenized_query)
print ("\ndoc_scores:")
print(doc_scores)

doc = bm25.get_top_n(tokenized_query, corpus, n=1)
print ("\nsimilar content to query:")
print(doc)
