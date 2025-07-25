# Healthy Squeeze - Natural Health E-commerce Platform

## Overview

Healthy Squeeze is a community-based e-commerce platform designed for selling herbal remedies and fresh medicinal juices in Kibera, Nairobi, Kenya. The application focuses on providing natural, affordable, and healthy alternatives to the local community with a colorful, user-friendly interface that reflects natural and organic branding.

## User Preferences

Preferred communication style: Simple, everyday language.

## System Architecture

### Backend Architecture
- **Flask Framework**: Python-based web framework handling routing, session management, and business logic
- **Session-based State Management**: Uses Flask-Session with filesystem storage for shopping cart persistence
- **Template Engine**: Jinja2 for dynamic content rendering and server-side templating
- **In-memory Data Storage**: Product data stored as Python dictionaries in models.py (no database currently implemented)

### Frontend Architecture
- **Bootstrap 5**: Responsive CSS framework for layout and components
- **Vanilla JavaScript**: Client-side interactivity for cart operations, geolocation, and UI enhancements
- **Mobile-first Design**: Responsive layout optimized for mobile devices
- **Component-based Templates**: Modular HTML templates extending a base layout

### Styling and Assets
- **Custom CSS**: Earth-tone color palette with CSS variables for consistent theming
- **Google Fonts**: Poppins font family for modern typography
- **Font Awesome**: Icon library for enhanced user interface
- **External Images**: Pixabay stock photos for product imagery

## Key Components

### Product Management
- **Product Catalog**: Two main categories - Herbal Remedies and Fresh Juices
- **Product Details**: Each product includes ingredients, medicinal benefits, pricing, and stock information
- **Category Filtering**: Dynamic product filtering by category

### Shopping Cart System
- **Session-based Cart**: Shopping cart data stored in Flask sessions
- **Quantity Management**: Add, update, and remove items from cart
- **Cart Persistence**: Cart maintains state across page visits within session

### User Interface Components
- **Navigation**: Bootstrap navbar with dropdown menus for product categories
- **Product Cards**: Grid-based product display with images, descriptions, and benefits
- **Detail Pages**: Individual product pages with ingredient information and health benefits
- **Responsive Design**: Mobile-optimized layout with Bootstrap grid system

### Geolocation Features
- **Store Locator**: HTML5 Geolocation API integration
- **Google Maps**: Embedded map showing store location in Kibera
- **Find Us Page**: Complete store information with address and hours

## Data Flow

### Product Display Flow
1. Route handler retrieves product data from models.py
2. Jinja2 templates render product information
3. Bootstrap components display responsive product grid
4. JavaScript enhances interactivity (lazy loading, animations)

### Shopping Cart Flow
1. User adds product to cart via route handler
2. Flask session stores cart data on server
3. Cart page displays items with quantity controls
4. Update/remove operations modify session data
5. Checkout process collects user information

### Checkout Process
1. Cart validation and total calculation
2. User information collection (name, phone, address)
3. Payment method selection (M-Pesa, Cash on Delivery)
4. Mock order processing and confirmation

## External Dependencies

### Frontend Libraries
- **Bootstrap 5**: CSS framework via CDN
- **Font Awesome 6**: Icon library via CDN
- **Google Fonts**: Poppins font family via CDN

### Backend Dependencies
- **Flask**: Web framework
- **Flask-Session**: Session management

### External Services
- **Google Maps**: Embedded maps for store location
- **Pixabay**: Stock photography for product images

### Development Tools
- **Python 3.x**: Runtime environment
- **Jinja2**: Template engine (included with Flask)

## Deployment Strategy

### Development Setup
- **Local Development**: Flask development server on port 5000
- **Static Files**: Served directly by Flask
- **Session Storage**: Filesystem-based session storage
- **Debug Mode**: Enabled for development with logging

### Production Considerations
- **Database Integration**: Currently using in-memory data storage; ready for database integration (likely PostgreSQL with Drizzle ORM)
- **Static File Serving**: Currently served by Flask; should be moved to CDN or reverse proxy
- **Session Management**: Filesystem sessions suitable for single-server deployment
- **Environment Variables**: Secret key management via environment variables

### Scalability Notes
- **Stateless Design**: Cart data in sessions allows for easy horizontal scaling
- **Database Ready**: Product model structure designed for easy database migration
- **CDN Integration**: External image hosting via Pixabay reduces server load
- **Mobile Optimization**: Responsive design reduces server-side mobile handling needs

The application follows a traditional MVC pattern with Flask handling the controller layer, Jinja2 templates as the view layer, and Python dictionaries serving as the model layer. The architecture is designed to be easily extensible with database integration and additional features while maintaining the community-focused, natural health branding throughout the user experience.