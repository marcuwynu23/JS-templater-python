# JS-templater Documentation

## Overview

JS-templater is a Python library that provides a template engine for Flask applications, allowing you to render JavaScript-based views on the server side. It generates HTML documents with embedded JavaScript modules that can access context data passed from your Python backend.

## Table of Contents

- [Installation](#installation)
- [Getting Started](#getting-started)
- [API Reference](#api-reference)
- [Classes](#classes)
- [Functions](#functions)
- [Usage Patterns](#usage-patterns)
- [Best Practices](#best-practices)

## Installation

```bash
pip install jstemplater
```

## Getting Started

### Basic Setup

1. Import the library in your Flask application:

```python
from flask import Flask
from jstemplater import JSTemplate

app = Flask(__name__)
js_template = JSTemplate(static_root='/static')
```

2. Create your JavaScript template file in `static/javascript/src/your-template.js`

3. Render the template in your route:

```python
@app.route('/')
def home():
    return js_template.render('your-template', context={'key': 'value'})
```

## API Reference

### Classes

#### `Element`

Represents an HTML element with opening and closing tags.

**Constructor:**

```python
Element(name, attrib="")
```

**Parameters:**

- `name` (str): The HTML tag name (e.g., 'div', 'span', 'h1')
- `attrib` (str): Initial attributes string (optional)

**Methods:**

- `add(element)`: Add child element or content
- `add_attrib(key, value)`: Add an attribute to the element
- `set_content(content)`: Set the text content of the element

**Example:**

```python
div = Element("div")
div.add_attrib("class", "container")
div.add_attrib("id", "main")
div.set_content("Hello World")
# Result: <div class='container' id='main'>Hello World</div>
```

#### `EElement`

Represents a self-closing HTML element (void element).

**Constructor:**

```python
EElement(name, attrib="")
```

**Parameters:**

- `name` (str): The HTML tag name (e.g., 'link', 'img', 'input')
- `attrib` (str): Initial attributes string (optional)

**Methods:**

- `add_attrib(key, value)`: Add an attribute to the element

**Example:**

```python
link = EElement("link")
link.add_attrib("rel", "stylesheet")
link.add_attrib("href", "/static/css/style.css")
# Result: <link rel="stylesheet" href="/static/css/style.css"/>
```

#### `JSTemplate`

Main class for rendering JavaScript templates.

**Constructor:**

```python
JSTemplate(static_root)
```

**Parameters:**

- `static_root` (str): The root path for static files (typically '/static' in Flask)

**Methods:**

- `render(script_name, context='')`: Render a JavaScript template

**Example:**

```python
js_template = JSTemplate(static_root='/static')
html = js_template.render('index', context={'title': 'Home'})
```

### Functions

#### `setTemplate(root, div, script)`

Internal function that generates a complete HTML document structure.

**Parameters:**

- `root` (str): Static root path for CSS files
- `div` (Element): The root div element containing the application
- `script` (Element): The script element loading the JavaScript module

**Returns:**

- `str`: Complete HTML document with DOCTYPE, head, and body

**Generated Structure:**

```html
<!DOCTYPE html>
<html>
  <head>
    <title>Web Application</title>
    <link rel="stylesheet" type="text/css" href="{root}/css/style.css" />
  </head>
  <body>
    <div id="root" data-content="{context_json}"></div>
    <script type="module" src="{root}/javascript/src/{script_name}.js"></script>
  </body>
</html>
```

## Usage Patterns

### Passing Context Data

Context data is passed as JSON in the `data-content` attribute of the root div:

```python
context = {
    'user': {'name': 'John', 'email': 'john@example.com'},
    'items': ['item1', 'item2', 'item3']
}
html = js_template.render('dashboard', context=context)
```

In your JavaScript file:

```javascript
const root = document.getElementById("root");
const context = JSON.parse(root.dataset.content);

console.log(context.user.name); // "John"
console.log(context.items); // ["item1", "item2", "item3"]
```

### Without Context Data

If you don't need to pass data, you can omit the context parameter:

```python
html = js_template.render('index')
```

In your JavaScript:

```javascript
const root = document.getElementById("root");
// root.dataset.content will be undefined
```

### Custom HTML Elements

You can create custom HTML structures using the `Element` and `EElement` classes:

```python
from jstemplater import Element, EElement

# Create a custom button
button = Element("button")
button.add_attrib("class", "btn btn-primary")
button.add_attrib("onclick", "handleClick()")
button.set_content("Click Me")

# Create an image
img = EElement("img")
img.add_attrib("src", "/static/images/logo.png")
img.add_attrib("alt", "Logo")
```

## Best Practices

1. **Organize JavaScript Files**: Keep your JavaScript templates organized in the `static/javascript/src/` directory

2. **Error Handling**: Always check if `root.dataset.content` exists before parsing:

```javascript
let context = {};
if (root.dataset.content) {
  try {
    context = JSON.parse(root.dataset.content);
  } catch (e) {
    console.error("Failed to parse context:", e);
  }
}
```

3. **CSS Organization**: Place your CSS files in `static/css/` directory as the template automatically links to `{static_root}/css/style.css`

4. **Module Scripts**: The generated scripts use `type="module"`, so you can use ES6 imports in your JavaScript files

5. **Context Size**: Keep context data reasonably sized. For large datasets, consider fetching via API calls from JavaScript instead

6. **Security**: Be careful with user-generated content in context data. Always sanitize data before passing it to templates

## Project Structure

Recommended project structure:

```
project/
├── app.py
├── static/
│   ├── css/
│   │   └── style.css
│   └── javascript/
│       └── src/
│           ├── index.js
│           ├── dashboard.js
│           └── profile.js
└── templates/  # Optional: for other Flask templates
```

## Troubleshooting

### Script Not Loading

- Verify the script path matches: `{static_root}/javascript/src/{script_name}.js`
- Check that Flask's static file serving is configured correctly
- Ensure the file extension is `.js` (not included in `script_name`)

### Context Data Not Available

- Check that you're passing a dictionary to the `context` parameter
- Verify JSON parsing in JavaScript (check browser console for errors)
- Ensure the root element exists before accessing `dataset.content`

### CSS Not Loading

- Verify CSS file exists at `{static_root}/css/style.css`
- Check Flask static folder configuration
- Inspect browser network tab for 404 errors

## License

See LICENSE file for details.
