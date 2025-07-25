from flask import render_template, request, redirect, url_for, session, flash, jsonify
from app import app
from models import PRODUCTS, get_products_by_category, get_product, get_categories
import logging

@app.route('/')
def index():
    """Home page with featured products"""
    # Get a few featured products from each category
    herbal_products = list(get_products_by_category('Herbal Remedies').values())[:2]
    juice_products = list(get_products_by_category('Fresh Juices').values())[:3]
    
    return render_template('index.html', 
                         herbal_products=herbal_products,
                         juice_products=juice_products)

@app.route('/products')
@app.route('/products/<category>')
def products(category=None):
    """Product listing page with optional category filter"""
    if category:
        products = get_products_by_category(category)
        page_title = f"{category} Products"
    else:
        products = PRODUCTS
        page_title = "All Products"
    
    categories = get_categories()
    
    return render_template('products.html', 
                         products=products,
                         categories=categories,
                         current_category=category,
                         page_title=page_title)

@app.route('/product/<product_id>')
def product_detail(product_id):
    """Product detail page"""
    product = get_product(product_id)
    if not product:
        flash('Product not found', 'error')
        return redirect(url_for('products'))
    
    return render_template('product_detail.html', product=product)

@app.route('/add_to_cart/<product_id>')
def add_to_cart(product_id):
    """Add product to cart"""
    product = get_product(product_id)
    if not product:
        flash('Product not found', 'error')
        return redirect(url_for('products'))
    
    # Initialize cart if it doesn't exist
    if 'cart' not in session:
        session['cart'] = {}
    
    # Add or increment product in cart
    if product_id in session['cart']:
        session['cart'][product_id] += 1
    else:
        session['cart'][product_id] = 1
    
    session.permanent = True
    flash(f'{product["name"]} added to cart!', 'success')
    
    return redirect(request.referrer or url_for('products'))

@app.route('/cart')
def cart():
    """View shopping cart"""
    cart_items = []
    total = 0
    
    if 'cart' in session:
        for product_id, quantity in session['cart'].items():
            product = get_product(product_id)
            if product:
                item_total = product['price'] * quantity
                cart_items.append({
                    'product': product,
                    'quantity': quantity,
                    'item_total': item_total
                })
                total += item_total
    
    return render_template('cart.html', cart_items=cart_items, total=total)

@app.route('/update_cart/<product_id>', methods=['POST'])
def update_cart(product_id):
    """Update quantity of product in cart"""
    quantity = int(request.form.get('quantity', 0))
    
    if 'cart' not in session:
        session['cart'] = {}
    
    if quantity > 0:
        session['cart'][product_id] = quantity
        flash('Cart updated!', 'success')
    else:
        # Remove item if quantity is 0
        if product_id in session['cart']:
            del session['cart'][product_id]
        flash('Item removed from cart!', 'info')
    
    session.permanent = True
    return redirect(url_for('cart'))

@app.route('/remove_from_cart/<product_id>')
def remove_from_cart(product_id):
    """Remove product from cart"""
    if 'cart' in session and product_id in session['cart']:
        del session['cart'][product_id]
        session.permanent = True
        flash('Item removed from cart!', 'info')
    
    return redirect(url_for('cart'))

@app.route('/checkout')
def checkout():
    """Checkout page"""
    if 'cart' not in session or not session['cart']:
        flash('Your cart is empty!', 'warning')
        return redirect(url_for('products'))
    
    cart_items = []
    total = 0
    
    for product_id, quantity in session['cart'].items():
        product = get_product(product_id)
        if product:
            item_total = product['price'] * quantity
            cart_items.append({
                'product': product,
                'quantity': quantity,
                'item_total': item_total
            })
            total += item_total
    
    return render_template('checkout.html', cart_items=cart_items, total=total)

@app.route('/process_checkout', methods=['POST'])
def process_checkout():
    """Process checkout (mock payment)"""
    if 'cart' not in session or not session['cart']:
        flash('Your cart is empty!', 'warning')
        return redirect(url_for('products'))
    
    # Mock payment processing
    name = request.form.get('name')
    phone = request.form.get('phone')
    address = request.form.get('address')
    payment_method = request.form.get('payment_method')
    
    if not all([name, phone, address, payment_method]):
        flash('Please fill in all required fields!', 'error')
        return redirect(url_for('checkout'))
    
    # Clear cart after successful "payment"
    session['cart'] = {}
    session.permanent = True
    
    flash(f'Thank you {name}! Your order has been received and will be delivered to {address}. We will contact you on {phone} for confirmation.', 'success')
    
    return redirect(url_for('index'))

@app.route('/find_us')
def find_us():
    """Find Us page with location and map"""
    return render_template('find_us.html')

@app.context_processor
def inject_cart_count():
    """Make cart count available in all templates"""
    cart_count = 0
    if 'cart' in session:
        cart_count = sum(session['cart'].values())
    return {'cart_count': cart_count}
