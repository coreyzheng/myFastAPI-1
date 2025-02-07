from typing import Annotated

from fastapi import FastAPI, Header, HTTPException

from rank_bm25 import BM25Okapi

app = FastAPI()

#initialize the corpus of documents
corpus = [
  "Hello there good man!",
  "It is quite windy in London",
  "How is the weather today?"
]

def TokenizedCorpus():
    tmp_tokenized_corpus = []
    for doc in corpus:
       doc_tokens = doc.split()
       # print (doc_tokens)
       tmp_tokenized_corpus.append(doc_tokens)
    return tmp_tokenized_corpus

@app.post("/add-doc/")
def add_doc(i_doc):
    corpus.append(i_doc)
    return {"corpus added": corpus}

@app.get("/query/")
def get_query(i_query):
    tokenized_corpus = TokenizedCorpus()

    # Create a BM25 index from the tokenized document corpus  
    bm25 = BM25Okapi(tokenized_corpus)

    # Query the BM25 index
    tokenized_query = i_query.split(" ")

    doc_scores = bm25.get_scores(tokenized_query)

    output = bm25.get_top_n(tokenized_query, corpus, n=1)

    return {"bm25 query result": output}

@app.get("/vectors/")
def get_vectors():   
    tokenized_corpus = TokenizedCorpus()

    # Create a BM25 index from the tokenized document corpus  
    bm25 = BM25Okapi(tokenized_corpus)    
    return {"bm25 vectors:": bm25}
