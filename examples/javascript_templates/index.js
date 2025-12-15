/**
 * Basic Index Template
 *
 * This is a simple JavaScript template that renders content
 * without requiring context data.
 */

const root = document.getElementById("root");

// Simple rendering without context
root.innerHTML = `
    <div class="container">
        <h1>Welcome to JS-templater</h1>
        <p>This is a basic example without context data.</p>
        <button onclick="alert('Hello!')">Click Me</button>
    </div>
`;
