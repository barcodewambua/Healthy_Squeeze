// Healthy Squeeze - Main JavaScript File

document.addEventListener('DOMContentLoaded', function() {
    // Initialize tooltips
    initializeTooltips();
    
    // Initialize product image lazy loading
    initializeLazyLoading();
    
    // Initialize cart functionality
    initializeCart();
    
    // Initialize form validation
    initializeFormValidation();
    
    // Initialize geolocation features
    initializeGeolocation();
    
    // Add smooth scrolling
    initializeSmoothScrolling();
    
    // Initialize animation on scroll
    initializeScrollAnimations();
});

// Initialize Bootstrap tooltips
function initializeTooltips() {
    const tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'));
    const tooltipList = tooltipTriggerList.map(function (tooltipTriggerEl) {
        return new bootstrap.Tooltip(tooltipTriggerEl);
    });
}

// Initialize lazy loading for product images
function initializeLazyLoading() {
    const images = document.querySelectorAll('img[data-src]');
    
    const imageObserver = new IntersectionObserver((entries, observer) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                const img = entry.target;
                img.src = img.dataset.src;
                img.classList.remove('lazy');
                imageObserver.unobserve(img);
            }
        });
    });
    
    images.forEach(img => imageObserver.observe(img));
}

// Cart functionality
function initializeCart() {
    // Update cart count in real-time
    updateCartDisplay();
    
    // Add event listeners for cart actions
    const addToCartButtons = document.querySelectorAll('.add-to-cart');
    addToCartButtons.forEach(button => {
        button.addEventListener('click', function(e) {
            e.preventDefault();
            const productId = this.dataset.productId;
            addToCart(productId);
        });
    });
    
    // Quantity update buttons
    const quantityButtons = document.querySelectorAll('.quantity-btn');
    quantityButtons.forEach(button => {
        button.addEventListener('click', function() {
            const input = this.parentNode.querySelector('input[type="number"]');
            const action = this.dataset.action;
            let currentValue = parseInt(input.value);
            
            if (action === 'increase') {
                input.value = currentValue + 1;
            } else if (action === 'decrease' && currentValue > 1) {
                input.value = currentValue - 1;
            }
            
            // Automatically submit the form after a delay
            clearTimeout(window.quantityUpdateTimeout);
            window.quantityUpdateTimeout = setTimeout(() => {
                input.closest('form').submit();
            }, 1000);
        });
    });
}

// Update cart display
function updateCartDisplay() {
    const cartCount = document.querySelector('.cart-count');
    if (cartCount) {
        // Get cart count from session (this would typically be done server-side)
        fetch('/api/cart/count')
            .then(response => response.json())
            .then(data => {
                cartCount.textContent = data.count;
                if (data.count > 0) {
                    cartCount.style.display = 'inline';
                } else {
                    cartCount.style.display = 'none';
                }
            })
            .catch(error => {
                console.log('Cart count update failed:', error);
            });
    }
}

// Add to cart function
function addToCart(productId) {
    // Show loading state
    const button = document.querySelector(`[data-product-id="${productId}"]`);
    const originalText = button.innerHTML;
    button.innerHTML = '<span class="loading"></span> Adding...';
    button.disabled = true;
    
    // Simulate API call (in real implementation, this would be an AJAX call)
    setTimeout(() => {
        button.innerHTML = '<i class="fas fa-check"></i> Added!';
        button.classList.remove('btn-success');
        button.classList.add('btn-outline-success');
        
        // Show success message
        showNotification('Product added to cart!', 'success');
        
        // Reset button after 2 seconds
        setTimeout(() => {
            button.innerHTML = originalText;
            button.classList.remove('btn-outline-success');
            button.classList.add('btn-success');
            button.disabled = false;
        }, 2000);
        
        // Update cart count
        updateCartDisplay();
    }, 1000);
}

// Form validation
function initializeFormValidation() {
    const forms = document.querySelectorAll('.needs-validation');
    
    forms.forEach(form => {
        form.addEventListener('submit', function(event) {
            if (!form.checkValidity()) {
                event.preventDefault();
                event.stopPropagation();
                
                // Focus on first invalid field
                const firstInvalidField = form.querySelector(':invalid');
                if (firstInvalidField) {
                    firstInvalidField.focus();
                }
            }
            
            form.classList.add('was-validated');
        });
    });
    
    // Real-time validation
    const inputs = document.querySelectorAll('input, textarea, select');
    inputs.forEach(input => {
        input.addEventListener('blur', function() {
            if (this.checkValidity()) {
                this.classList.remove('is-invalid');
                this.classList.add('is-valid');
            } else {
                this.classList.remove('is-valid');
                this.classList.add('is-invalid');
            }
        });
    });
}

// Geolocation functionality
function initializeGeolocation() {
    const getLocationButtons = document.querySelectorAll('.get-location');
    
    getLocationButtons.forEach(button => {
        button.addEventListener('click', function() {
            if (navigator.geolocation) {
                button.innerHTML = '<span class="loading"></span> Getting location...';
                button.disabled = true;
                
                navigator.geolocation.getCurrentPosition(
                    function(position) {
                        const lat = position.coords.latitude;
                        const lng = position.coords.longitude;
                        
                        // You can use these coordinates to show directions or distance
                        showNotification(`Location found: ${lat.toFixed(4)}, ${lng.toFixed(4)}`, 'success');
                        
                        button.innerHTML = '<i class="fas fa-map-marker-alt"></i> Location Found';
                        button.disabled = false;
                    },
                    function(error) {
                        showNotification('Unable to get your location. Please enable location services.', 'warning');
                        button.innerHTML = '<i class="fas fa-exclamation-triangle"></i> Location Error';
                        button.disabled = false;
                    }
                );
            } else {
                showNotification('Geolocation is not supported by this browser.', 'error');
            }
        });
    });
}

// Smooth scrolling
function initializeSmoothScrolling() {
    const links = document.querySelectorAll('a[href^="#"]');
    
    links.forEach(link => {
        link.addEventListener('click', function(e) {
            const targetId = this.getAttribute('href');
            if (targetId === '#') return;
            
            const targetElement = document.querySelector(targetId);
            if (targetElement) {
                e.preventDefault();
                targetElement.scrollIntoView({
                    behavior: 'smooth',
                    block: 'start'
                });
            }
        });
    });
}

// Animation on scroll
function initializeScrollAnimations() {
    const animatedElements = document.querySelectorAll('.animate-on-scroll');
    
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('fade-in-up');
                observer.unobserve(entry.target);
            }
        });
    }, {
        threshold: 0.1,
        rootMargin: '0px 0px -50px 0px'
    });
    
    animatedElements.forEach(el => observer.observe(el));
}

// Notification system
function showNotification(message, type = 'info') {
    // Create notification element
    const notification = document.createElement('div');
    notification.className = `alert alert-${type} alert-dismissible fade show position-fixed`;
    notification.style.cssText = `
        top: 20px;
        right: 20px;
        z-index: 9999;
        min-width: 300px;
        max-width: 500px;
    `;
    
    notification.innerHTML = `
        ${message}
        <button type="button" class="btn-close" data-bs-dismiss="alert"></button>
    `;
    
    // Add to page
    document.body.appendChild(notification);
    
    // Auto-remove after 5 seconds
    setTimeout(() => {
        if (notification && notification.parentNode) {
            notification.remove();
        }
    }, 5000);
}

// Search functionality (if search is implemented)
function initializeSearch() {
    const searchInput = document.querySelector('#search-input');
    const searchResults = document.querySelector('#search-results');
    
    if (searchInput && searchResults) {
        let searchTimeout;
        
        searchInput.addEventListener('input', function() {
            const query = this.value.trim();
            
            clearTimeout(searchTimeout);
            
            if (query.length < 2) {
                searchResults.innerHTML = '';
                searchResults.style.display = 'none';
                return;
            }
            
            searchTimeout = setTimeout(() => {
                performSearch(query);
            }, 300);
        });
    }
}

// Perform search (mock function)
function performSearch(query) {
    // This would typically make an AJAX call to search products
    console.log('Searching for:', query);
    
    // Mock search results
    const mockResults = [
        { name: 'Dawapaste', category: 'Herbal Remedies' },
        { name: 'Fresh Passion Juice', category: 'Fresh Juices' }
    ].filter(item => 
        item.name.toLowerCase().includes(query.toLowerCase()) ||
        item.category.toLowerCase().includes(query.toLowerCase())
    );
    
    displaySearchResults(mockResults);
}

// Display search results
function displaySearchResults(results) {
    const searchResults = document.querySelector('#search-results');
    
    if (!searchResults) return;
    
    if (results.length === 0) {
        searchResults.innerHTML = '<div class="p-3 text-muted">No products found</div>';
    } else {
        const resultsHTML = results.map(result => `
            <div class="search-result-item p-2 border-bottom">
                <strong>${result.name}</strong>
                <small class="text-muted d-block">${result.category}</small>
            </div>
        `).join('');
        
        searchResults.innerHTML = resultsHTML;
    }
    
    searchResults.style.display = 'block';
}

// Product comparison (if needed)
function addToComparison(productId) {
    let comparison = JSON.parse(localStorage.getItem('productComparison') || '[]');
    
    if (!comparison.includes(productId)) {
        comparison.push(productId);
        localStorage.setItem('productComparison', JSON.stringify(comparison));
        showNotification('Product added to comparison', 'success');
    } else {
        showNotification('Product already in comparison', 'warning');
    }
    
    updateComparisonCount();
}

// Update comparison count
function updateComparisonCount() {
    const comparison = JSON.parse(localStorage.getItem('productComparison') || '[]');
    const countElement = document.querySelector('.comparison-count');
    
    if (countElement) {
        countElement.textContent = comparison.length;
        countElement.style.display = comparison.length > 0 ? 'inline' : 'none';
    }
}

// Initialize comparison on page load
document.addEventListener('DOMContentLoaded', function() {
    updateComparisonCount();
});

// Utility functions
const Utils = {
    // Format currency
    formatCurrency: function(amount, currency = 'KES') {
        return new Intl.NumberFormat('en-KE', {
            style: 'currency',
            currency: currency
        }).format(amount);
    },
    
    // Format date
    formatDate: function(date) {
        return new Intl.DateTimeFormat('en-KE', {
            year: 'numeric',
            month: 'long',
            day: 'numeric'
        }).format(new Date(date));
    },
    
    // Debounce function
    debounce: function(func, wait) {
        let timeout;
        return function executedFunction(...args) {
            const later = () => {
                clearTimeout(timeout);
                func(...args);
            };
            clearTimeout(timeout);
            timeout = setTimeout(later, wait);
        };
    },
    
    // Throttle function
    throttle: function(func, limit) {
        let inThrottle;
        return function() {
            const args = arguments;
            const context = this;
            if (!inThrottle) {
                func.apply(context, args);
                inThrottle = true;
                setTimeout(() => inThrottle = false, limit);
            }
        };
    }
};

// Export for use in other files if needed
window.HealthySqueeze = {
    showNotification,
    addToCart,
    addToComparison,
    Utils
};
