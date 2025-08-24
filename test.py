import json, os, re

docs = [
  ("d1",  "The cat chased a small mouse into the garden."),
  ("d2",  "A friendly dog played fetch by the river."),
  ("d3",  "BM25 is a ranking function widely used in search engines."),
  ("d4",  "Boolean retrieval uses logical operators like AND and OR."),
  ("d5",  "TF-IDF weights terms by frequency and rarity."),
  ("d6",  "Neural retrieval uses dense embeddings for semantic search."),
  ("d7",  "The dog and the cat slept on the same couch."),
  ("d8",  "The library hosts a workshop on information retrieval."),
  ("d9",  "Students implemented BM25 and compared it with TF-IDF."),
  ("d10", "The chef roasted chicken with rosemary and garlic."),
  ("d11", "A black cat crossed the old stone bridge at night."),
  ("d12", "Dogs are loyal companions during long hikes."),
  ("d13", "The dataset contains fifteen short sentences for testing."),
  ("d14", "Reranking models reorder BM25 candidates using transformers."),
  ("d15", "The dog sniffed a cat but ignored the mouse.")
]

def light_clean(s: str) -> str:
    s = s.lower()
    s = re.sub(r"[^\w\s\-]", " ", s)   # keep angka & minus (biar BM25 / TF-IDF gak ilang)
    s = re.sub(r"\s+", " ", s).strip()
    return s

os.makedirs("corpus", exist_ok=True)
with open("corpus/docs.jsonl", "w", encoding="utf-8") as f:
    for did, txt in docs:
        f.write(json.dumps({"id": did, "contents": light_clean(txt)}) + "\n")