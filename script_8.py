
# Create assets/style.css
css_code = '''/* Dark Theme Styling for AI Farm Yield Gap Analysis Platform */

:root {
    --bg-primary: #0d1117;
    --bg-secondary: #161b22;
    --bg-tertiary: #1a1f2e;
    --text-primary: #e6edf3;
    --text-secondary: #8b949e;
    --accent-primary: #58a6ff;
    --accent-secondary: #1f6feb;
    --border-color: #30363d;
    --success-color: #3fb950;
    --warning-color: #d29922;
    --danger-color: #f85149;
}

/* Main app styling */
.stApp {
    background-color: var(--bg-primary);
    color: var(--text-primary);
}

/* Sidebar styling */
[data-testid="stSidebar"] {
    background-color: var(--bg-secondary);
    border-right: 1px solid var(--border-color);
}

/* Headers */
h1, h2, h3, h4, h5, h6 {
    color: var(--text-primary) !important;
}

/* Cards and containers */
.css-1r6slb0 {
    background-color: var(--bg-tertiary);
    border: 1px solid var(--border-color);
    border-radius: 8px;
    padding: 1.5rem;
}

/* Metrics */
[data-testid="stMetricValue"] {
    color: var(--accent-primary);
    font-size: 2rem;
    font-weight: 600;
}

/* Buttons */
.stButton > button {
    background-color: var(--accent-secondary);
    color: var(--text-primary);
    border: none;
    border-radius: 6px;
    padding: 0.5rem 1rem;
    font-weight: 500;
    transition: all 0.2s;
}

.stButton > button:hover {
    background-color: var(--accent-primary);
    transform: translateY(-1px);
    box-shadow: 0 4px 12px rgba(88, 166, 255, 0.3);
}

/* Tabs */
.stTabs [data-baseweb="tab-list"] {
    gap: 8px;
    background-color: var(--bg-secondary);
    border-radius: 8px;
    padding: 4px;
}

.stTabs [data-baseweb="tab"] {
    background-color: transparent;
    color: var(--text-secondary);
    border-radius: 6px;
    padding: 8px 16px;
}

.stTabs [aria-selected="true"] {
    background-color: var(--bg-tertiary);
    color: var(--accent-primary);
}

/* Tables */
.dataframe {
    background-color: var(--bg-secondary);
    color: var(--text-primary);
    border: 1px solid var(--border-color);
}

/* Select boxes and inputs */
.stSelectbox, .stTextInput, .stNumberInput {
    background-color: var(--bg-secondary);
    color: var(--text-primary);
    border: 1px solid var(--border-color);
    border-radius: 6px;
}

/* Plotly charts dark theme override */
.js-plotly-plot {
    background-color: var(--bg-tertiary) !important;
}
'''

with open('yield_gap_analysis/assets/style.css', 'w') as f:
    f.write(css_code)

print("✅ Created assets/style.css")
