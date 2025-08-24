from pyserini.search.lucene import LuceneSearcher

# Path ke index
IDX = "indexes/my_index"
searcher = LuceneSearcher(IDX)

def docs_for_query(query_str: str) -> set[str]:
    """Ambil doc IDs sesuai query Lucene string"""
    hits = searcher.search(query_str, k=1000)
    return {h.docid for h in hits}

def show(q, docs):
    print(f"\n🔍 Query: {q}")
    print("Matching doc IDs:", sorted(docs, key=lambda x: int(x[1:])))

queries = [
    "dog AND cat",
    "dog OR cat",
    "dog AND NOT cat",
    "retrieval AND (bm25 OR (tf AND idf))",
    "retrieval AND (neural or bm25)"
]

for query_str in queries:
    docs = docs_for_query(query_str)
    show(query_str, docs)
