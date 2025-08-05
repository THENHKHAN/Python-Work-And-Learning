from sentence_transformers import util
from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")
texts = ["Sample text 1", "Sample text 2"]
embeddings = model.encode(texts)

# print(embeddings[0])
# print(embeddings[1])
print("Embeddings generated successfully.")
# This code snippet uses the SentenceTransformer library to load a pre-trained model



query = "What is AI?"
corpus = ["Artificial intelligence is the simulation of human intelligence.",
          "Pizza is a popular Italian dish."]

query_embedding = model.encode(query)
corpus_embeddings = model.encode(corpus)

similarities = util.cos_sim(query_embedding, corpus_embeddings)
print(similarities)  # Tells which document is more similar to the query

'''
Embeddings generated successfully.
tensor([[0.7198, 0.0766]])
'''