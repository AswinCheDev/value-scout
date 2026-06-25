from pymongo import MongoClient

c = MongoClient('mongodb://localhost:27017')
db = c['value_scout']['products']

targets = ['pants', 'jeans', 'shorts', 'shoes', 'tshirt', 'shirt']
count = db.count_documents({'category': {'$in': targets}, 'styleEmbedding': {'$exists': True}})
print(f'Products with embeddings in target categories: {count}')

# Also check what categories exist
categories = db.distinct('category')
print(f'\nAll categories in database: {categories}')
