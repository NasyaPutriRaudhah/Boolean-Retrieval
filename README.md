# Boolean-Retrieval 🔍

Implementasi **Boolean Retrieval** untuk pencarian dokumen menggunakan **Pyserini**.  
Proyek ini terdiri dari 3 modul utama: preprocessing, indexing, dan boolean search.

---

## 📂 Struktur File

- `preprocess.py`  
  Melakukan preprocessing dokumen (lowercase, stopword removal, stemming).

- `index.py`  
  Membangun indeks dokumen menggunakan Pyserini.

- `boolean_search.py`  
  Menjalankan pencarian dokumen dengan query boolean (`AND`, `OR`, `NOT`).

---

## ⚡ Cara Menjalankan

1. **Clone repository**
```bash
git clone https://github.com/NasyaPutriRaudhah/Boolean-Retrieval
cd Boolean-Retrieval

2. **Aktifkan virtual environment**
```bash
venv\Scripts\activate

pip install pyserini

python index.py

python boolean_search.py

