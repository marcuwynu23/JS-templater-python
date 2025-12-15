"""
Basic Example: Simple JS-templater usage with Flask

This example demonstrates the most basic usage of JS-templater.
"""

from flask import Flask
from jstemplater import JSTemplate

app = Flask(__name__)
js_template = JSTemplate(static_root='/static')

@app.route('/')
def index():
    """Render a simple index page with JavaScript template."""
    return js_template.render('index')

if __name__ == '__main__':
    app.run(debug=True)

