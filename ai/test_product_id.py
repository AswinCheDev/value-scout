from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017")
db = client["value_scout"]
products = db["products"]

# Find a product with styleEmbedding
p = products.find_one({"styleEmbedding": {"$exists": True}, "category": "shoes"})

if p:
    print(f"Sample product ID: {p['_id']}")
    print(f"Category: {p.get('category')}")
    print(f"Name: {p.get('productName')}")
    print(f"Has embedding: {'styleEmbedding' in p}")
else:
    print("No products with embeddings found")
