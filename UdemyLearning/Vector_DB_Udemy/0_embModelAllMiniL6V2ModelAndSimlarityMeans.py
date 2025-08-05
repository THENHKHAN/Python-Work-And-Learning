from sentence_transformers import SentenceTransformer

# 1. Load a pretrained Sentence Transformer model
model = SentenceTransformer("all-MiniLM-L6-v2")

# The sentences to encode
sentences = [
    "The weather is lovely today.",
    "It's so sunny outside!",
    "He drove to the stadium.",
]

# 2. Calculate embeddings by calling model.encode()
embeddings = model.encode(sentences)
print(embeddings.shape)
# [3, 384]

# 3. Calculate the embedding similarities
similarities = model.similarity(embeddings, embeddings)
print(similarities)
# tensor([[1.0000, 0.6660, 0.1046],
#         [0.6660, 1.0000, 0.1411],
#         [0.1046, 0.1411, 1.0000]])

'''
So yes — embeddings, embeddings means:

“Compare each sentence to every other sentence (including itself)”

It gives a square matrix of all pairwise comparisons.
'''
# COSINE SIMILARITY EXPLANATION
# Cosine similarity measures how similar two vectors are, based on the cosine of the angle between them.
# It ranges from -1 to 1:
# -1 means the vectors are in opposite directions (i.e., they are very dissimilar)
# 1 means the vectors point in the same direction (i.e., they are very similar)
# 0 means the vectors are orthogonal (i.e., they are neither similar nor dissimilar)
# Cosine similarity measures the angle between two vectors, NOT the distance.
'''
When two vectors point in the same direction (angle = 0°), cosine similarity = 1 → very similar.

As the angle between them increases, the cosine value decreases → meaning the vectors are less similar.
When vectors are at 90°, cosine similarity = 0 → they are completely dissimilar (orthogonal).
If vectors point in opposite directions (180°), cosine similarity = -1 → they are maximally dissimilar.
So yes, as the cosine value drops from 1 toward 0 or negative, similarity decreases and dissimilarity increases.

This is why in embeddings:

            Higher cosine similarity → more semantically similar texts.                
            Lower cosine similarity → less related or different texts.

'''

'''
| Measure            | What it measures         | Higher means     | Lower means      |
| ------------------ | ------------------------ | ---------------- | ---------------- |
| Cosine similarity  | Angle between vectors    | More similar (1) | Less similar (0) |
| Euclidean distance | Distance between vectors | Less similar     | More similar     |



'''

'''
Exactly! You got it perfectly:

More cosine similarity value (closer to 1) → more similar
Less angle between vectors → more similar
Cosine similarity = cosine of angle → when angle is small, cosine is close to 1
So yes, a higher cosine similarity means the two things are more alike because their vectors point in nearly the same direction.

'''