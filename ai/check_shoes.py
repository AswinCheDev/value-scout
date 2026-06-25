from pymongo import MongoClient

c = MongoClient('mongodb://localhost:27017')
db = c['value_scout']['products']

# Check shoes with embeddings
shoes_with_embeddings = db.count_documents({'category': 'shoes', 'styleEmbedding': {'$exists': True}})
total_shoes = db.count_documents({'category': 'shoes'})
print(f'Shoes with embeddings: {shoes_with_embeddings} / {total_shoes}')

# Check all categories with embedding counts
categories = db.distinct('category')
print('\nEmbedding counts by category:')
for cat in categories:
    with_emb = db.count_documents({'category': cat, 'styleEmbedding': {'$exists': True}})
    total = db.count_documents({'category': cat})
    print(f'  {cat}: {with_emb} / {total}')

# Test a jacket recommendation
print('\n--- Testing jacket recommendations ---')
jacket = db.find_one({'category': 'jacket', 'styleEmbedding': {'$exists': True}})
if jacket:
    print(f"Jacket ID: {jacket['_id']}")
    
    # Find similar products
    import requests
    r = requests.get(f"http://localhost:5000/api/style-builder/{jacket['_id']}")
    if r.status_code == 200:
        data = r.json()
        print(f"Target categories: {data.get('target_categories')}")
        print(f"Total candidates: {data.get('total_candidates')}")
        print(f"Recommendations: {len(data.get('recommendations', []))}")
        
        # Get full product details for recommendations
        for rec in data.get('recommendations', []):
            prod = db.find_one({'_id': rec['id']})
            if prod:
                print(f"  - {prod.get('category')}: {prod.get('productName', 'N/A')[:50]}")
