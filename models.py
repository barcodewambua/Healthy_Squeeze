# Product data structure for Healthy Squeeze e-commerce platform

PRODUCTS = {
    'dawapaste': {
        'id': 'dawapaste',
        'name': 'Dawapaste - Herbal Remedy',
        'category': 'Herbal Remedies',
        'price': 500,  # KES
        'currency': 'KES',
        'image': 'https://pixabay.com/get/g99a1df3a42f2a469bf85fcfaf6b5e8a167755488c62a62d94cf747c73373c67ae9484cf8426dd9db8000716b1dea31aa8a593f34ed05752bfb1512f71c9a0bfb_1280.jpg',
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
        'image': 'https://pixabay.com/get/g02c7f2d85c1b1df99546278c9b9c137370097d5e24f23445f4f4614d99847af1561bb3ec6ff2dd028ee93662987cc2f3fa5c57400295d0ccd5d85bec7170fbf6_1280.jpg',
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
        'image': 'https://pixabay.com/get/ge49a388d1d0b1601f49c6c6bd0228760a40d901f80a904be712ee2930888528acdfe1e501bcdd3f3e7761d1090c2bd1d3eb8f4ad66ff30071127d42a6c7049fb_1280.jpg',
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
        'image': 'https://pixabay.com/get/g752672a9d2e00b1ff89e933c68dfdf27f43c5d05e95cc5237bfc57417e48236c2ddc1abb5ef445ee0630851037e10a23ebceadbe282a71400c4d2c2397a18d04_1280.jpg',
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
        'image': 'https://pixabay.com/get/g7f08252b891fe738f313be223ce27ee51abdbc5061582254bc3cfaa3bf6a06b449fb111dcfbcd0e3099a313469211743e9d715117246c78a2db07edc747118a0_1280.jpg',
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
        'image': 'https://pixabay.com/get/g8a9e6301a5e97775fb6d4410a35bc6df657a8ca62beeba67678641383b86a961b9421cc8ee4f11495dc47ce86d5a5fd5b093377eed9b6742f24d76fa70314127_1280.jpg',
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
