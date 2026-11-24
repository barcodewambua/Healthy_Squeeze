# Healthy Squeeze - Natural Health E-commerce Platform

A colorful, user-friendly e-commerce website for **Healthy Squeeze** — selling herbal remedies and fresh medicinal juices in Kibera, Nairobi, Kenya.

## Overview

Healthy Squeeze is a community-based e-commerce platform that provides natural, affordable, and healthy alternatives to the local community in Kibera. Products include traditional herbal remedies and fresh juices made with no preservatives.

## Features

### Product Categories

- **Herbal Remedies** — Traditional pastes like Dawapaste (ginger, tamarind, honey) and Turmeric Healing Paste
- **Fresh Juices** — Natural fruit juices including passion fruit, pineapple, green detox, and moringa superfood juice

### Core Functionality

- Product listing with category filtering
- Detailed product pages with ingredients and medicinal benefits
- Shopping cart with quantity management (add, update, remove)
- Mock checkout with payment options (M-Pesa, Cash on Delivery)
- Store locator with HTML5 Geolocation support for the Kibera location
- Mobile-responsive design

### Highlights

- **Natural & Organic Design** — Earth-tone color palette reflecting natural ingredients
- **Community Focus** — Local, affordable branding tailored for Kibera
- **Health Benefits** — Detailed medicinal properties for every product
- **Geolocation** — "Find Us" page with embedded Google Maps and distance calculation
- **Responsive** — Mobile-first layout using Bootstrap 5

## Tech Stack

### Backend

| Component | Purpose |
|-----------|---------|
| **Flask 3.1** | Web framework — routing, request handling, template rendering |
| **Flask-Session** | Server-side session storage for shopping cart persistence |
| **Flask-SQLAlchemy** | ORM layer (available for future database integration) |
| **Jinja2** | Template engine for dynamic HTML |

### Frontend

| Component | Purpose |
|-----------|---------|
| **HTML5 / CSS3** | Semantic markup, CSS Grid & Flexbox layouts |
| **Bootstrap 5** | Responsive grid, components, and utilities |
| **JavaScript (Vanilla)** | Cart interactions, geolocation, and UI behavior |
| **Font Awesome** | Icon set for navigation and UI elements |
| **Google Fonts (Poppins)** | Modern typography |

### External Services

- **Google Maps Embed API** — Store location map on the "Find Us" page
- **Pixabay** — Stock product imagery

## Project Structure

```
WebForge/
├── app.py                 # Flask app factory & configuration
├── main.py                # Entry point — runs the dev server
├── models.py              # Product data & helper functions
├── routes.py              # All route handlers (pages, cart, checkout)
├── requirements.txt       # Pinned Python dependencies
├── pyproject.toml         # Project metadata
├── templates/
│   ├── base.html          # Base layout (navbar, footer, flash messages)
│   ├── index.html         # Home page with featured products
│   ├── products.html      # Product listing with category filter
│   ├── product_detail.html# Single product view
│   ├── cart.html           # Shopping cart
│   ├── checkout.html       # Checkout form
│   └── find_us.html        # Store locator with map
├── static/
│   ├── css/style.css       # Custom styles
│   ├── js/main.js          # Client-side JavaScript
│   └── images/             # Product and branding images
└── flask_session/          # Server-side session files (auto-generated)
```

## Installation & Setup

### Prerequisites

- Python 3.11 or higher
- pip package manager

### 1. Clone the repository

```bash
git clone https://github.com/<your-username>/healthy-squeeze.git
cd healthy-squeeze
```

### 2. Create a virtual environment (recommended)

```bash
python -m venv venv

# Windows
venv\Scripts\activate

# macOS / Linux
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the application

```bash
python main.py
```

The server starts at **http://localhost:5000**.

### Environment Variables (optional)

| Variable | Default | Description |
|----------|---------|-------------|
| `SESSION_SECRET` | auto-generated | Flask secret key for session signing |

## Routes

| Route | Method | Description |
|-------|--------|-------------|
| `/` | GET | Home page with featured products |
| `/products` | GET | All products listing |
| `/products/<category>` | GET | Products filtered by category |
| `/product/<product_id>` | GET | Product detail page |
| `/add_to_cart/<product_id>` | GET | Add a product to the cart |
| `/cart` | GET | View shopping cart |
| `/update_cart/<product_id>` | POST | Update item quantity in cart |
| `/remove_from_cart/<product_id>` | GET | Remove item from cart |
| `/checkout` | GET | Checkout page |
| `/process_checkout` | POST | Process order (mock payment) |
| `/find_us` | GET | Store locator with map |

## License

This project is provided as-is for educational and community use.
