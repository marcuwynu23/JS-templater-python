# JS-templater Examples

This directory contains practical examples demonstrating how to use JS-templater in your Flask applications.

## Examples

### 1. Basic Example (`basic_example.py`)

The simplest possible usage of JS-templater. Renders a JavaScript template without any context data.

**Usage:**
```bash
python basic_example.py
```

**JavaScript Template:** `javascript_templates/index.js`

### 2. With Context Example (`with_context_example.py`)

Demonstrates passing data from Python to JavaScript templates using the `context` parameter.

**Routes:**
- `/` - Home page with user information
- `/dashboard` - Dashboard with statistics and activity feed

**JavaScript Templates:**
- `javascript_templates/home.js`
- `javascript_templates/dashboard.js`

### 3. Multiple Routes Example (`multiple_routes_example.py`)

Shows how to use JS-templater across multiple routes, each with its own JavaScript template.

**Routes:**
- `/` - Index page
- `/about` - About page with team information
- `/contact` - Contact page
- `/products` - Products listing page

**JavaScript Templates:**
- `javascript_templates/index.js`
- `javascript_templates/products.js`
- (Create `about.js` and `contact.js` as needed)

## Project Structure

To use these examples, set up your Flask project like this:

```
your-project/
├── app.py (or example file)
├── static/
│   ├── css/
│   │   └── style.css
│   └── javascript/
│       └── src/
│           ├── index.js
│           ├── home.js
│           ├── dashboard.js
│           └── products.js
└── examples/
    └── ...
```

## Running Examples

1. **Install dependencies:**
   ```bash
   pip install flask jstemplater
   ```

2. **Set up static files:**
   - Create `static/css/style.css` for styling
   - Copy JavaScript templates from `javascript_templates/` to `static/javascript/src/`

3. **Run the example:**
   ```bash
   python examples/basic_example.py
   ```

4. **Visit in browser:**
   - Open `http://localhost:5000` in your browser

## JavaScript Templates

All JavaScript templates are ES6 modules and can:
- Access context data via `root.dataset.content`
- Use modern JavaScript features (imports, arrow functions, etc.)
- Interact with the DOM freely
- Make API calls for additional data

## Tips

- Always check if `root.dataset.content` exists before parsing
- Use try-catch when parsing JSON context data
- Keep context data reasonably sized
- For large datasets, consider fetching via API calls from JavaScript

## Next Steps

- Customize the CSS in `static/css/style.css`
- Add more JavaScript templates for different pages
- Integrate with your existing Flask application
- Add API endpoints for dynamic data loading

