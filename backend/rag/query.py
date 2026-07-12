import faiss
import pickle
from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")

index = faiss.read_index("rag_index.faiss")

with open("rag/docs.pkl", "rb") as f:
    docs = pickle.load(f)

def retrieve(query):
    q_emb = model.encode([query])
    D, I = index.search(q_emb, k=2)
    return [docs[i] for i in I[0]]
