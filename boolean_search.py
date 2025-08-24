# boolean_search_strict.py
from pyserini.search.lucene import LuceneSearcher

IDX = "indexes/my_index"
searcher = LuceneSearcher(IDX)

def docs_for(term: str) -> set[str]:
    # Ambil "semua" dokumen yang mengandung term tsb (k >> jumlah dokumen)
    hits = searcher.search(term, k=1000)
    return {h.docid for h in hits}

def show(q, ids):
    print(f"\n🔍 Query: {q}")
    print("Matching doc IDs:", sorted(ids, key=lambda x: int(x[1:])))

# Boolean queries
dog   = docs_for("dog")
cat   = docs_for("cat")
bm25  = docs_for("bm25")
tf    = docs_for("tf")
idf   = docs_for("idf")
retr  = docs_for("retrieval")  # analyzer akan stem ke "retriev"

show("dog AND cat",            dog & cat)
show("dog OR cat",             dog | cat)
show("dog AND NOT cat",        dog - cat)
show("(bm25 OR tf-idf) AND retrieval", (bm25 | (tf & idf)) & retr)
