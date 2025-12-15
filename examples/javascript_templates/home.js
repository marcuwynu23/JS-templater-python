/**
 * Home Template with Context Data
 *
 * This template demonstrates how to access and use context data
 * passed from the Python backend.
 */

const root = document.getElementById("root");

// Parse context data if available
let context = {};
if (root.dataset.content) {
  try {
    context = JSON.parse(root.dataset.content);
  } catch (e) {
    console.error("Failed to parse context:", e);
  }
}

// Render using context data
root.innerHTML = `
    <div class="container">
        <h1>${context.title || "Home"}</h1>
        <div class="user-info">
            <h2>Welcome, ${context.user?.name || "Guest"}!</h2>
            <p>Email: ${context.user?.email || "N/A"}</p>
        </div>
        <p class="message">${context.message || ""}</p>
    </div>
`;
