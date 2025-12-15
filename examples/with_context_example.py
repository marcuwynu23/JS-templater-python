"""
Example: Using JS-templater with context data

This example shows how to pass data from Python to JavaScript templates.
"""

from flask import Flask
from jstemplater import JSTemplate

app = Flask(__name__)
js_template = JSTemplate(static_root='/static')

@app.route('/')
def home():
    """Home page with user context."""
    context = {
        'title': 'Welcome Home',
        'user': {
            'name': 'John Doe',
            'email': 'john@example.com'
        },
        'message': 'Hello from Python!'
    }
    return js_template.render('home', context=context)

@app.route('/dashboard')
def dashboard():
    """Dashboard with multiple data points."""
    context = {
        'stats': {
            'users': 1250,
            'posts': 5432,
            'comments': 12345
        },
        'recent_activity': [
            {'action': 'User registered', 'time': '2 hours ago'},
            {'action': 'Post created', 'time': '5 hours ago'},
            {'action': 'Comment added', 'time': '1 day ago'}
        ]
    }
    return js_template.render('dashboard', context=context)

if __name__ == '__main__':
    app.run(debug=True)

