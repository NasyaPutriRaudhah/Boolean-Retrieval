import os
import subprocess

# Path input dan output
input_path = "corpus"
index_path = "indexes/my_index"

# Command pyserini indexing
command = [
    "python", "-m", "pyserini.index.lucene",
    "--collection", "JsonCollection",
    "--input", input_path,
    "--index", index_path,
    "--generator", "DefaultLuceneDocumentGenerator",
    "--threads", "1",
    "--storePositions",
    "--storeDocvectors",
    "--storeRaw"
]

print("🚀 Menjalankan indexing...")
subprocess.run(command, shell=True)
print(f"✅ Indexing selesai! Index tersimpan di: {index_path}")
