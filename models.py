# Product data structure for Healthy Squeeze e-commerce platform

PRODUCTS = {
    'dawapaste': {
        'id': 'dawapaste',
        'name': 'Dawapaste - Herbal Remedy',
        'category': 'Herbal Remedies',
        'price': 500,  # KES
        'currency': 'KES',
        'image': '/static/images/dawapaste.jpg',
        'description': 'Traditional herbal paste made from natural ingredients including ginger, tamarind, and honey.',
        'ingredients': {
            'Ginger': 'Antioxidant properties, aids in treating constipation and bloating',
            'Tamarind': 'High in potassium, helps regulate blood pressure and detoxifies the body',
            'Honey': 'Supports respiratory health, helps with cold and asthma symptoms'
        },
        'benefits': [
            'Natural digestive aid',
            'Respiratory health support',
            'Antioxidant and detox properties',
            'Blood pressure regulation'
        ],
        'stock': 50
    },
    'passion-juice': {
        'id': 'passion-juice',
        'name': 'Fresh Passion Fruit Juice',
        'category': 'Fresh Juices',
        'price': 150,  # KES
        'currency': 'KES',
        'image': '/static/images/juice.jpg',
        'description': 'Pure passion fruit juice with no preservatives, rich in Vitamin A and natural antioxidants.',
        'ingredients': {
            'Passion Fruit': 'High in Vitamin A - supports healthy skin, vision, and immune system'
        },
        'benefits': [
            'Vitamin A for healthy skin and vision',
            'Immune system support',
            'Natural antioxidants',
            'No artificial preservatives'
        ],
        'stock': 30
    },
    'pineapple-juice': {
        'id': 'pineapple-juice',
        'name': 'Fresh Pineapple Juice',
        'category': 'Fresh Juices',
        'price': 120,  # KES
        'currency': 'KES',
        'image': '/static/images/pineaple.png',
        'description': 'Fresh pineapple juice high in fiber and natural enzymes to aid digestion.',
        'ingredients': {
            'Pineapple': 'High in fiber and digestive enzymes - aids digestion and supports gut health'
        },
        'benefits': [
            'Digestive health support',
            'High fiber content',
            'Natural digestive enzymes',
            'Gut health promotion'
        ],
        'stock': 25
    },
    'green-juice': {
        'id': 'green-juice',
        'name': 'Green Detox Juice',
        'category': 'Fresh Juices',
        'price': 200,  # KES
        'currency': 'KES',
        'image': '/static/images/greentea.jpg',
        'description': 'Blend of green vegetables and fruits that promotes digestion and supports weight management.',
        'ingredients': {
            'Green Vegetables Mix': 'Promotes healthy digestion and supports natural weight management'
        },
        'benefits': [
            'Digestive health promotion',
            'Weight management support',
            'Natural detoxification',
            'Nutrient-dense green vegetables'
        ],
        'stock': 20
    },
    'turmeric-paste': {
        'id': 'turmeric-paste',
        'name': 'Turmeric Healing Paste',
        'category': 'Herbal Remedies',
        'price': 450,  # KES
        'currency': 'KES',
        'image': '/static/images/gingerpaste.png',
        'description': 'Traditional turmeric-based paste with anti-inflammatory and healing properties.',
        'ingredients': {
            'Turmeric': 'Powerful anti-inflammatory and antioxidant properties',
            'Black Pepper': 'Enhances turmeric absorption and bioavailability',
            'Coconut Oil': 'Natural carrier oil with antimicrobial properties'
        },
        'benefits': [
            'Anti-inflammatory support',
            'Joint health promotion',
            'Antioxidant protection',
            'Natural healing properties'
        ],
        'stock': 35
    },
    'moringa-juice': {
        'id': 'moringa-juice',
        'name': 'Moringa Superfood Juice',
        'category': 'Fresh Juices',
        'price': 180,  # KES
        'currency': 'KES',
        'image': '/static/images/greentea.jpg',
        'description': 'Nutrient-rich moringa leaf juice packed with vitamins, minerals, and antioxidants.',
        'ingredients': {
            'Moringa Leaves': 'Rich in vitamins A, C, and E, iron, calcium, and protein'
        },
        'benefits': [
            'Complete nutrition support',
            'Energy boost',
            'Iron and calcium supplementation',
            'Antioxidant protection'
        ],
        'stock': 15
    }
}


def get_products_by_category(category=None):
    """Get products filtered by category"""
    if category:
        return {k: v for k, v in PRODUCTS.items() if v['category'] == category}
    return PRODUCTS


def get_product(product_id):
    """Get a single product by ID"""
    return PRODUCTS.get(product_id)


def get_categories():
    """Get all unique categories"""
    categories = set()
    for product in PRODUCTS.values():
        categories.add(product['category'])
    return list(categories)
