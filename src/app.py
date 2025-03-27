import streamlit as st
import requests

theme = "transparent"

st.set_page_config(
    page_title="GitHub Professional Profile Analyzer", 
    page_icon="👨‍💻", 
    layout="wide"
)

# Custom CSS for enhanced design
st.markdown("""
<style>
    .main-title {
        font-size: 2.5rem;
        color: #2C3E50;
        text-align: center;
        margin-bottom: 20px;
    }
    .subtitle {
        color: #7F8C8D;
        text-align: center;
        margin-bottom: 30px;
    }
    .metric-card {
        background-color: #F4F6F7;
        border-radius: 10px;
        padding: 20px;
        text-align: center;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }
    .stMetric > div {
        display: flex;
        flex-direction: column;
        align-items: center;
    }
</style>
""", unsafe_allow_html=True)

# Advanced title and subtitle
st.markdown('<h1 class="main-title">🚀 GitHub Professional Profile Analyzer</h1>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">Unlock insights for potential employers with a deep dive into your GitHub profile</p>', unsafe_allow_html=True)

# GitHub username input
git_username = st.text_input("🔎 Enter GitHub Username", placeholder="Enter a GitHub username")

def fetch_github_data(username):
    """Fetch comprehensive GitHub user data"""
    base_url = f"https://api.github.com/users/{username}"
    try:
        response = requests.get(base_url)
        return response.json() if response.status_code == 200 else None
    except Exception as e:
        st.error(f"Error fetching GitHub data: {e}")
        return None

if git_username:
    # Fetch GitHub user data
    user_data = fetch_github_data(git_username)
    
    if user_data:
        # Create columns for professional metrics
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            st.markdown('<div class="metric-card">', unsafe_allow_html=True)
            st.metric("📍 Location", user_data.get('location', 'Not Specified'))
            st.markdown('</div>', unsafe_allow_html=True)
        
        with col2:
            st.markdown('<div class="metric-card">', unsafe_allow_html=True)
            st.metric("💼 Followers", user_data.get('followers', 0))
            st.markdown('</div>', unsafe_allow_html=True)
        
        with col3:
            st.markdown('<div class="metric-card">', unsafe_allow_html=True)
            st.metric("🌟 Public Repos", user_data.get('public_repos', 0))
            st.markdown('</div>', unsafe_allow_html=True)
        
        with col4:
            st.markdown('<div class="metric-card">', unsafe_allow_html=True)
            st.metric("💻 Account Created", user_data.get('created_at', 'N/A')[:10])
            st.markdown('</div>', unsafe_allow_html=True)
        
        # Visualization Section
        st.markdown("## ⛭ Professional GitHub Insights")
        
        # Create columns for visualizations
        viz_col1, viz_col2 = st.columns(2)
        
        with viz_col1:
            # Top Languages
            top_lang_url = f"https://github-readme-stats.vercel.app/api/top-langs/?username={git_username}&layout=compact&theme={theme}"
            st.image(top_lang_url, caption=f"🖥️ Top Programming Languages", use_container_width=True)
        
        with viz_col2:
            # Contribution Chart
            contrib_chart = f"https://ghchart.rshah.org/777/{git_username}"
            st.image(contrib_chart, caption="📅 Yearly Contribution Heatmap", use_container_width=True)
        
        # Full-width Profile Details
        st.image(
            f"https://github-profile-summary-cards.vercel.app/api/cards/profile-details?username={git_username}&theme={theme}", 
            caption="🔍 Comprehensive Profile Overview", 
            use_container_width=True
        )
        
        # Professional Bio Section
        st.markdown("## 👤 Professional Bio")
        st.write(user_data.get('bio', 'No bio available'))
        
        # Blog/Website Link
        if user_data.get('blog'):
            st.markdown(f"🌐 Personal Website/Blog: [{user_data['blog']}]({user_data['blog']})")
    
    else:
        st.error("Unable to fetch GitHub profile. Please check the username.")

# Footer with professional touch
st.markdown("---")
st.markdown("""
    💡 **Tips:**
    - Maintain an active GitHub profile
    - Showcase diverse, well-documented projects
    - Contribute to open-source repositories
    - Keep your profile updated and professional
""")

# Add a subtle watermark
st.markdown(
    """
    <div style="position: fixed; bottom: 10px; right: 10px; font-size: 16px; color: #888;">
        Created with ❤️ using Streamlit
    </div>
    """,
    unsafe_allow_html=True
)