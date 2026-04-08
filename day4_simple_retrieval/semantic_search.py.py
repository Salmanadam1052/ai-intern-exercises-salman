from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

model = SentenceTransformer('all-MiniLM-L6-v2')
documents = [
    # Machine Learning
    """Machine learning allows computers to learn from data without explicit programming.,
    Deep learning is a subset of machine learning that uses neural networks.""",
    
    # Cooking
    """Cooking requires proper ingredients, timing, and temperature control.,
    Baking cakes needs precise measurements and careful mixing of ingredients.""",
    
    # Space
    """Space exploration helps us understand planets, stars, and galaxies.,
    Astronauts travel to space using rockets and live in space stations.""",
    
    # Programming
    """Programming involves writing code to build software applications.,
    Python is a popular programming language for data science and AI.""",
    
    # Sports
    """Football is one of the most popular sports in the world.,
    Regular exercise and sports improve physical and mental health."""
]
doc_embed = model.encode(documents)
while True:
    print("Type 'exit' to quit the program.")
    query = input("enter your query?").strip()
    if query.lower() == "exit":
        print("Exiting the program.")
        break 

    quer_embed = model.encode([query])
    score=cosine_similarity(quer_embed, doc_embed)[0]
    top_3 = np.argsort(score)[::-1][:3]
    print("Top 3 relevant documents:")
    for id in top_3:
             print(f"Document {id+1} (Score: {score[id]:.4f}):\n{documents[id]}\n")