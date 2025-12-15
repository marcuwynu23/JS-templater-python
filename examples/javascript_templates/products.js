/**
 * Products Listing Template
 *
 * Example of rendering a product list with data from context.
 */

const root = document.getElementById("root");

// Get context data
let context = {};
if (root.dataset.content) {
  try {
    context = JSON.parse(root.dataset.content);
  } catch (e) {
    console.error("Failed to parse context:", e);
  }
}

const products = context.products || [];

// Render products
root.innerHTML = `
    <div class="products-page">
        <h1>${context.page_title || "Products"}</h1>
        
        <div class="products-grid">
            ${products
              .map(
                (product) => `
                <div class="product-card">
                    <h3>${product.name}</h3>
                    <p class="price">$${product.price.toFixed(2)}</p>
                    <button onclick="addToCart(${
                      product.id
                    })">Add to Cart</button>
                </div>
            `
              )
              .join("")}
        </div>
        
        ${products.length === 0 ? "<p>No products available.</p>" : ""}
    </div>
`;

// Example function (would typically be in a separate module)
function addToCart(productId) {
  console.log(`Adding product ${productId} to cart`);
  // Implement cart logic here
}
