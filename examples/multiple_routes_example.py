"""
Example: Multiple routes with different JavaScript templates

This example demonstrates using JS-templater across multiple routes.
"""

from flask import Flask
from jstemplater import JSTemplate

app = Flask(__name__)
js_template = JSTemplate(static_root='/static')

@app.route('/')
def index():
    """Main landing page."""
    return js_template.render('index', context={
        'page_title': 'Home',
        'description': 'Welcome to our application'
    })

@app.route('/about')
def about():
    """About page."""
    return js_template.render('about', context={
        'page_title': 'About Us',
        'team': [
            {'name': 'Alice', 'role': 'Developer'},
            {'name': 'Bob', 'role': 'Designer'},
            {'name': 'Charlie', 'role': 'Manager'}
        ]
    })

@app.route('/contact')
def contact():
    """Contact page."""
    return js_template.render('contact', context={
        'page_title': 'Contact',
        'email': 'contact@example.com',
        'phone': '+1-234-567-8900'
    })

@app.route('/products')
def products():
    """Products listing page."""
    context = {
        'page_title': 'Products',
        'products': [
            {'id': 1, 'name': 'Product A', 'price': 29.99},
            {'id': 2, 'name': 'Product B', 'price': 39.99},
            {'id': 3, 'name': 'Product C', 'price': 49.99}
        ]
    }
    return js_template.render('products', context=context)

if __name__ == '__main__':
    app.run(debug=True)

