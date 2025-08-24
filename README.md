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
```
2. **Aktifkan Virtual Environment**
```bash
venv\Scripts\activate
```
3. **Install Dependencies**
```bash
pip install pyserini
```

4. **Jalankan Preprocessing**
```bash
python preprocess.py
```
5. **Bangun Indeks**
```bash
python index.py
```
6. **Boolean Search**
```bash
python boolean_search.py
```




