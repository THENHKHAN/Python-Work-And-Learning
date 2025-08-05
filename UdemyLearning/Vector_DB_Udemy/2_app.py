# By default, ChromaDB uses Euclidean distance to compare vectors.

import chromadb

print("Starting ChromaDB with Euclidean distance...ByDefault, ChromaDB uses Euclidean distance to compare vectors.")

chroma_client = chromadb.Client()
collection = chroma_client.get_or_create_collection(
    name="my_collection",
    metadata={"hnsw:space": "l2"}  # Use Euclidean distance (default)
    # If you want to use cosine similarity, you can specify:
    # metadata={"hnsw:space": "cosine"}  # Use cosine similarity
    
    ) # # Euclidean (default) metadata={"hnsw:space": "l2"}
listOfdocuments = [
    "This is a document about pineapple",
    "This is a document about oranges",
    "This is a document about hawaii"
]
listOfIDs = ["id1", "id2", "id3"]
collection.add(
    ids=listOfIDs, 
    documents= listOfdocuments,
    # embeddings=embeddings,  # If you have precomputed embeddings, you can add them here like all-MiniLM-L6-v2
    # If you don't provide embeddings, Chroma will compute them for you using the default embedding
)
# query 
query = "This is a query document about hawaii"
results = collection.query(
    query_texts=[query], # Chroma will embed this for you
    n_results=3 # how many results to return
)
print(results)

''''
results['documents'][0] 
 is sorted by distance — the first one is the closest (most similar), the last is the farthest (most dissimilar).
'''
documents = results['documents'][0]  # list of matched documents for first query
distances = results['distances'][0]  # list of distances for first query
minDistance = min(distances)  # minimum distance found
maxDistance = max(distances)  # maximum distance found
print(f"\nMinimum distance: {minDistance:.4f}")
print(f"Maximum distance: {maxDistance:.4f}")


print("\nResults ranked by similarity (lowest distance = most similar):\n")
for i, (doc, dist) in enumerate(zip(documents, distances), start=1):
    print(f"{i}. Document: {doc}")
    print(f"   Distance: {dist:.4f}")


# for result in results['documents'][0]:
#     print(result)  # Prints the documents that match the query


print(f"\n Query: {query}")
print("\nTop results:\n")
for doc, dist in zip(documents, distances):
    print(f"Document: {doc}")
    print(f"Distance: {dist:.4f}")
    # print(f"This sentence is similar to the query with a distance of {dist:.4f}\n")


'''

(.venv) E:\UdemyLearning\PyTHON_Learning\Vector_DB_Udemy>python 2_app.py
Starting ChromaDB with Euclidean distance...ByDefault, ChromaDB uses Euclidean distance to compare vectors.
{'ids': [['id3', 'id1', 'id2']], 'embeddings': None, 'documents': [['This is a document about hawaii', 'This is a document about pineapple', 'This is a document about oranges']], 'uris': None, 'included': ['metadatas', 'documents', 'distances'], 'data': None, 'metadatas': [[None, None, None]], 'distances': [[0.1980964094400406, 1.0404009819030762, 1.2430799007415771]]}

Minimum distance: 0.1981
Maximum distance: 1.2431

Results ranked by similarity (lowest distance = most similar):

1. Document: This is a document about hawaii
   Distance: 0.1981
2. Document: This is a document about pineapple
   Distance: 1.0404
3. Document: This is a document about oranges
   Distance: 1.2431


'''























# from sentence_transformers import SentenceTransformer
# import chromadb
# chroma_client = chromadb.Client()
# collection = chroma_client.create_collection(name="my_collection")
# listOfdocuments = [
#     "This is a document about pineapple",
#     "This is a document about oranges",
#     "This is a document about hawaii"
# ]
# listOfIDs = ["id1", "id2", "id3"]
# query = "This is a query document about hawaii"
# model = SentenceTransformer("all-MiniLM-L6-v2")
# embeddings = model.encode(listOfdocuments).tolist()

# collection.add(
#     ids=listOfIDs,
#     documents=listOfdocuments,
#     embeddings=embeddings,
# )


# query_embedding = model.encode([query]).tolist()

# results = collection.query(
#     query_embeddings=query_embedding,
#     n_results=3
# )


# print(results)

# for result in results['documents'][0]:
#     print(result)  # Prints the documents that match the query
