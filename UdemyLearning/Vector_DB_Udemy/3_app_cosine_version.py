import chromadb


# This script demonstrates how to use ChromaDB with cosine similarity for document retrieval.

print("Starting ChromaDB with cosine similarity...")


chroma_client = chromadb.Client()

collection = chroma_client.get_or_create_collection(
    name="my_collection",
    metadata={"hnsw:space": "cosine"}  # Use cosine similarity
)

listOfdocuments = [
    "This is a document about pineapple",
    "This is a document about oranges",
    "This is a document about hawaii"
]
listOfIDs = ["id1", "id2", "id3"]

collection.add(
    ids=listOfIDs,
    documents=listOfdocuments,
)

# Query
query = "This is a query document about hawaii"
results = collection.query(
    query_texts=[query],  # Chroma will embed this for you
    n_results=3
)

documents = results['documents'][0]
distances = results['distances'][0]

print(f"\nQuery: {query}")
print("Results ranked by similarity (higher cosine similarity = more similar):\n")

for i, (doc, dist) in enumerate(zip(documents, distances), start=1):
    similarity = 1 - dist  # Convert cosine distance to similarity
    print(f"{i}. Document: {doc}")
    print(f"   Cosine similarity: {similarity:.4f}\n")
print("Query completed successfully. And caluclated cosine similarity scores.\n")

'''
(.venv) E:\UdemyLearning\PyTHON_Learning\Vector_DB_Udemy>python 3_app_cosine_version.py
Starting ChromaDB with cosine similarity...

Query: This is a query document about hawaii
Results ranked by similarity (higher cosine similarity = more similar):

1. Document: This is a document about hawaii
   Cosine similarity: 0.9010

2. Document: This is a document about pineapple
   Cosine similarity: 0.4798

3. Document: This is a document about oranges
   Cosine similarity: 0.3785

Query completed successfully. And caluclated cosine similarity scores.


'''



'''
What happens here?
The collection uses cosine similarity internally.
Returned distances are cosine distance = 1 - cosine similarity.
You convert back to similarity by subtracting from 1.
Results printed with similarity score between 0 (no similarity) and 1 (identical).


=====>>  the more similariy value the more similar the document is to the query.

Steps:
Set metadata={"hnsw:space": "cosine"} when creating/getting the collection to use cosine similarity.

The distances returned will actually be cosine distances (1 - cosine similarity), so you convert them to similarity by:
similarity = 1 - distance

Sort results by similarity (higher is better).
because cosine similarity means angle and cosine distance means how far apart the vectors are in the vector space.

| Term              | Higher value means? | Lower value means? |
| ----------------- | ------------------- | ------------------ |
| Cosine similarity | More similar        | Less similar       |
| Cosine distance   | Less similar        | More similar       |

'''