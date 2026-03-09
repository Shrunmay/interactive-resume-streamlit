import streamlit as st
import pandas as pd
import plotly.express as px

# --- PAGE CONFIG ---
st.set_page_config(
    page_title="Shrunmay Shinde | Interactive Resume",
    page_icon="📊",
    layout="wide"
)

# --- CUSTOM CSS ---
st.markdown("""
<style>
.main-header { font-size: 38px; font-weight: bold; color: #1E3A8A; margin-bottom: 0px; }
.sub-header { 
    font-size: 24px; font-weight: 600; color: #1E40AF; 
    border-bottom: 2px solid #1E40AF; padding-bottom: 5px; margin-top: 25px; margin-bottom: 15px;
}
.sidebar-text { font-size: 14px; }
.highlight { color: #1E3A8A; font-weight: bold; }
</style>
""", unsafe_allow_html=True)

# --- SIDEBAR / CONTACT INFO ---
st.sidebar.image("assets/NewPassPortPhoto.jpg", caption="Shrunmay Shivaji Shinde")
st.sidebar.markdown("## Contact Details")
st.sidebar.write("📍 Toronto, ON")
st.sidebar.markdown("📧 [shrunmay.shinde@rotman.utoronto.ca](mailto:shrunmay.shinde@rotman.utoronto.ca)")
st.sidebar.write("📞 +1 (437) 808-1005")
st.sidebar.markdown("[LinkedIn](https://www.linkedin.com/in/shrunmay-shinde-93882125b/) | [GitHub](https://github.com/shrunmay)")

st.sidebar.markdown("---")
st.sidebar.markdown("### Key Achievements")
st.sidebar.write("🏆 **98.81 Percentile** in JEE Mains (Top 1.2%)")
st.sidebar.write("💰 **CAD 10,000** MMA Entrance Award")

# --- HEADER ---
st.markdown('<p class="main-header">Shrunmay Shivaji Shinde</p>', unsafe_allow_html=True)
st.write("Master of Management Analytics Candidate | Rotman School of Management, University of Toronto")

# --- NAVIGATION ---
section = st.selectbox(
    "Choose a section to explore:",
    ["Summary & Education", "Professional Experience", "Technical Skills", "Projects & Research"]
)

# =========================================================
# SUMMARY & EDUCATION
# =========================================================
if section == "Summary & Education":
    st.markdown('<p class="sub-header">Professional Summary</p>', unsafe_allow_html=True)
    st.write("""
    Advanced Analytics professional and Data Scientist with a B.Tech in Computer Science. 
    Proven track record in engineering enterprise-scale AI engines, NLP pipelines, and 
    logistics optimization models for billion-dollar firms including EllisDon and Patanjali. 
    Expertise in scaling MLOps lifecycles and translating complex operational friction into 
    testable experimental designs.
    """)

    st.markdown('<p class="sub-header">Education</p>', unsafe_allow_html=True)
    edu_data = {
        "Degree": ["Master of Management Analytics", "Bachelor of Technology (CSE)"],
        "Institution": ["Rotman School of Management (UofT)", "IIIT Pune, India"],
        "GPA": ["3.52 / 4.00", "4.00 / 4.00"],
        "Key Highlights": [
            "Entrance Award Recipient (CAD 10,000)", 
            "Secured $13,450 CAD in corporate sponsorships for Entrepreneurship Club"
        ]
    }
    st.table(pd.DataFrame(edu_data))

# =========================================================
# WORK EXPERIENCE
# =========================================================
elif section == "Professional Experience":
    st.markdown('<p class="sub-header">Work History</p>', unsafe_allow_html=True)
    
    job = st.radio(
        "Select a role to view detailed impact metrics:",
        ["EllisDon (Data Scientist Co-op)", "Finite 4 (Product & Data Analyst)", "Patanjali Ayurved (AI Intern)"]
    )

    if job == "EllisDon (Data Scientist Co-op)":
        st.write("### EllisDon | Jan 2026 - Present")
        st.write("""
        - **Vector-2 Risk Engine:** Spearheading an enterprise-scale predictive engine on GCP for schedule and budget slippage signals across a **$7.3B portfolio**.
        - **BigQuery Pipelines:** Engineered SQL pipelines processing **319,000+ monthly records** across 15+ relational databases.
        - **Leadership Framework:** Presented a 'Hypothesis vs. Verdict' framework to leadership, using data to invalidate anecdotal biases.
        - **Heuristic Modeling:** Architected a multi-factor model assessing cost variance, safety, and delays to define 'risk' in unlabeled datasets.
        """)
    
    elif job == "Finite 4 (Product & Data Analyst)":
        st.write("### Finite 4 Engineering | Aug 2023 - Aug 2024")
        st.write("""
        - **Corp Eagle Launch:** Deployed an NLP resume engine that automated 50,000+ profiles, reducing **time-to-hire by 40%**.
        - **Data Ingestion:** Reduced manual entry errors by **95%** by building Python pipelines to extract text from variable PDF/DOCX formats.
        - **NLP Matching:** Utilized Named Entity Recognition (NER) and contextual embeddings to boost candidate retrieval precision by **27%**.
        """)

    else:
        st.write("### Patanjali Ayurved | Aug 2022 - Aug 2023")
        st.write("""
        - **Logistics Optimization:** Scaled a dynamic routing solution for milk procurement, reducing transportation costs per liter by **32%**.
        - **ETL Digitization:** Processed over **1.2 million historical records** to resolve data sparsity in decentralized quality logs.
        - **VRP Solver:** Combined HDBSCAN and Google OR-Tools with XGBoost to reduce volume prediction error (MAPE) by **18%**.
        - **Fleet Utilization:** Increased average capacity utilization from **72% to 94%**.
        """)

    # --- EXPERIENCE TIMELINE ---
    st.markdown("### Experience Timeline")
    df_timeline = pd.DataFrame([
        dict(Job="Patanjali", Start="2022-08-01", End="2023-08-01"),
        dict(Job="Finite 4", Start="2023-08-01", End="2024-08-01"),
        dict(Job="EllisDon", Start="2026-01-01", End="2026-04-01")
    ])
    fig = px.timeline(df_timeline, x_start="Start", x_end="End", y="Job", color="Job", template="plotly_white")
    fig.update_yaxes(autorange="reversed")
    st.plotly_chart(fig, use_container_width=True)

# =========================================================
# TECHNICAL SKILLS
# =========================================================
elif section == "Technical Skills":
    st.markdown('<p class="sub-header">Skills Proficiency & Tools</p>', unsafe_allow_html=True)
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.write("**Programming & Cloud:**")
        st.write("Python, SQL (BigQuery), GCP, FastAPI, Docker, K8s, Neo4j [cite: 4]")
        st.write("**Data Science & AI:**")
        st.write("PyTorch, TensorFlow, GNN, NLP, XGBoost, A/B Testing, MLOps [cite: 5]")

    with col2:
        min_score = st.slider("Filter by Proficiency Level:", 0, 100, 80)
    
    skills = {
        "Skill": ["Python", "SQL", "GCP", "NLP", "GNN", "Tableau", "PyTorch", "XGBoost", "FastAPI"],
        "Level": [98, 95, 88, 92, 85, 82, 90, 89, 84]
    }
    df_skills = pd.DataFrame(skills)
    filtered_skills = df_skills[df_skills["Level"] >= min_score]
    
    fig_skills = px.bar(filtered_skills, x="Level", y="Skill", orientation="h", color="Level", color_continuous_scale="Blues")
    st.plotly_chart(fig_skills, use_container_width=True)

# =========================================================
# PROJECTS & RESEARCH
# =========================================================
elif section == "Projects & Research":
    st.markdown('<p class="sub-header">Technical Projects</p>', unsafe_allow_html=True)

    with st.expander("GraphSAGE Anti-Money Laundering (AML) Forensics"):
        st.write("""
        - Engineered a **Graph Neural Network (GNN)** to detect illicit Bitcoin subgraphs (smurfing patterns). [cite: 35]
        - Optimized operational threshold to 5%, boosting **Recall to 84.1%**. [cite: 36]
        - Deployed audit dashboard via FastAPI and Streamlit for sub-200ms inference. [cite: 36]
        """)

    with st.expander("Real-Time Human Activity Recognition"):
        st.write("""
        - Developed a hybrid **CNN-RNN architecture (VGG16+LSTM)** with **92% accuracy** for athletic movements. [cite: 38]
        - Integrated live video inference via Flask and visualized predictions in Tableau. 
        """)

    with st.expander("Identification of Cattle Breeds (Research Paper)"):
        st.write("""
        - Built a non-invasive supply chain traceability system using cattle muzzle images. 
        - Fine-tuned an **Xception (CNN)** model to achieve **95.6% identification accuracy** in real-time. 
        - Currently under review for publication. [cite: 41]
        """)
