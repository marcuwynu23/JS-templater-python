/**
 * Dashboard Template
 *
 * Example of rendering a dashboard with statistics and activity feed.
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

const stats = context.stats || {};
const activities = context.recent_activity || [];

// Render dashboard
root.innerHTML = `
    <div class="dashboard">
        <h1>Dashboard</h1>
        
        <div class="stats-grid">
            <div class="stat-card">
                <h3>Users</h3>
                <p class="stat-number">${stats.users || 0}</p>
            </div>
            <div class="stat-card">
                <h3>Posts</h3>
                <p class="stat-number">${stats.posts || 0}</p>
            </div>
            <div class="stat-card">
                <h3>Comments</h3>
                <p class="stat-number">${stats.comments || 0}</p>
            </div>
        </div>
        
        <div class="activity-feed">
            <h2>Recent Activity</h2>
            <ul>
                ${activities
                  .map(
                    (activity) => `
                    <li>
                        <strong>${activity.action}</strong>
                        <span class="time">${activity.time}</span>
                    </li>
                `
                  )
                  .join("")}
            </ul>
        </div>
    </div>
`;
