# JS-templater

A Flask library/tool to use pure DOM JavaScript rendering with a view engine. JS-templater allows you to build modern web applications by rendering JavaScript templates on the server side while maintaining a clean separation between your Python backend and JavaScript frontend.

## Features

- 🚀 **Simple Integration**: Easy to integrate with Flask applications
- 🎨 **Pure JavaScript**: Use vanilla JavaScript for rendering, no framework dependencies
- 📦 **Template Engine**: Server-side template generation with context data passing
- 🔧 **Flexible**: Pass JSON context data to your JavaScript templates
- 📝 **Clean HTML**: Generates clean, semantic HTML structure

## Installation

```bash
pip install jstemplater
```

Or install from source:

```bash
git clone https://github.com/yourusername/JS-templater-python.git
cd JS-templater-python
pip install .
```

## Quick Start

### 1. Basic Flask Setup

```python
from flask import Flask
from jstemplater import JSTemplate

app = Flask(__name__)

# Initialize JSTemplate with your static files root
js_template = JSTemplate(static_root='/static')

@app.route('/')
def index():
    # Render a JavaScript template
    return js_template.render('index', context={'title': 'Welcome', 'user': 'John'})
```

### 2. Project Structure

Your Flask application should have the following structure:

```
your-app/
├── app.py
└── static/
    ├── css/
    │   └── style.css
    └── javascript/
        └── src/
            └── index.js
```

### 3. JavaScript Template Example

Create `static/javascript/src/index.js`:

```javascript
// Get the root element
const root = document.getElementById("root");

// Parse context data if provided
let context = {};
if (root.dataset.content) {
  context = JSON.parse(root.dataset.content);
}

// Render your application
root.innerHTML = `
    <h1>${context.title || "Hello World"}</h1>
    <p>Welcome, ${context.user || "Guest"}!</p>
`;
```

## API Reference

### `JSTemplate(static_root)`

Initialize the JSTemplate engine.

**Parameters:**

- `static_root` (str): The root path for static files (e.g., '/static')

**Example:**

```python
js_template = JSTemplate(static_root='/static')
```

### `render(script_name, context='')`

Render a JavaScript template.

**Parameters:**

- `script_name` (str): Name of the JavaScript file (without .js extension)
- `context` (dict, optional): Context data to pass to the template as JSON

**Returns:**

- `str`: Complete HTML document with embedded script

**Example:**

```python
html = js_template.render('dashboard', context={'users': ['Alice', 'Bob']})
```

## Examples

See the [examples](./examples/) directory for more detailed usage examples.

## Requirements

- Python >= 3.6
- Flask (for web framework integration)

## License

See [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## Author

Mark Wayne B. Menorca
