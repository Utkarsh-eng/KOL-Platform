import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

from src.extract_scholar import extract_google_scholar
from src.extract_pubmed import extract_pubmed
from src.preprocess import build_profile_text
from src.embeddings import generate_embedding
from src.similarity import compute_similarity_matrix
from src.scoring import calculate_influence_scores
from src.clustering import cluster_kols
from src.summarizer import generate_llm_summary


# --------------------------------------------------
# PAGE CONFIG
# --------------------------------------------------

st.set_page_config(
    page_title="KOL AI Analysis System",
    layout="wide"
)

st.title(" KOL AI Analysis System")

st.markdown("""
### Features
- Multi-source researcher extraction
- Semantic similarity analysis
- Influence scoring
- KMeans clustering
- Gemini-powered insights
""")


# --------------------------------------------------
# DATA FILES
# --------------------------------------------------

scholar_files = [
    "data/raw/scholar/_Andrew Ng_ - _Google Scholar_.html",
    "data/raw/scholar/_Li Fei-Fei_ - _Google Scholar_.html",
    "data/raw/scholar/_Yann LeCun_ - _Google Scholar_.html"

]

pubmed_files = [
    "data/raw/pubmed/andrew.html",
    "data/raw/pubmed/Fei-Fei-Li.html",
    "data/raw/pubmed/Yann LeCun.html"
]


# --------------------------------------------------
# EXTRACT DATA
# --------------------------------------------------

scholar_profiles = []

for file in scholar_files:
    scholar_profiles.append(
        extract_google_scholar(file)
    )

pubmed_profiles = []

for file in pubmed_files:
    pubmed_profiles.append(
        extract_pubmed(file)
    )


# --------------------------------------------------
# MERGE DATA
# --------------------------------------------------

combined_profiles = []

for scholar, pubmed in zip(
    scholar_profiles,
    pubmed_profiles
):

    profile = {
        **scholar,
        **pubmed
    }

    combined_profiles.append(profile)


# --------------------------------------------------
# BUILD TEXT
# --------------------------------------------------

texts = []

for profile in combined_profiles:

    text = build_profile_text(
        profile
    )

    texts.append(text)


# --------------------------------------------------
# EMBEDDINGS
# --------------------------------------------------

embeddings = []

for text in texts:

    embedding = generate_embedding(
        text
    )

    embeddings.append(embedding)


# --------------------------------------------------
# SIMILARITY MATRIX
# --------------------------------------------------

names = [
    p["name"]
    for p in combined_profiles
]

similarity_df = compute_similarity_matrix(
    embeddings,
    names
)


# --------------------------------------------------
# INFLUENCE SCORES
# --------------------------------------------------

scores = calculate_influence_scores(
    combined_profiles
)

score_df = pd.DataFrame({
    "Researcher": names,
    "Influence Score": scores
})


# --------------------------------------------------
# CLUSTERING
# --------------------------------------------------

clusters = cluster_kols(
    embeddings
)

cluster_df = pd.DataFrame({
    "Researcher": names,
    "Cluster": clusters
})


# --------------------------------------------------
# DASHBOARD METRICS
# --------------------------------------------------

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "Researchers",
        len(combined_profiles)
    )

with col2:
    st.metric(
        "Data Sources",
        2
    )

with col3:
    st.metric(
        "Embeddings Generated",
        len(embeddings)
    )


# --------------------------------------------------
# RESEARCHER PROFILES
# --------------------------------------------------

st.header(" Researcher Profiles")

for profile in combined_profiles:

    with st.expander(
        profile["name"]
    ):

        st.write(
            f"**Affiliation:** {profile['affiliation']}"
        )

        st.write(
            "**Research Interests:**"
        )

        st.write(
            ", ".join(
                profile["research_interests"]
            )
        )

        st.write(
            f"**Citations:** {profile['citations']}"
        )

        st.write(
            f"**H-Index:** {profile['h_index']}"
        )


# --------------------------------------------------
# SIMILARITY MATRIX
# --------------------------------------------------

st.header(
    " Semantic Similarity Matrix"
)

fig, ax = plt.subplots(
    figsize=(8, 6)
)

sns.heatmap(
    similarity_df,
    annot=True,
    cmap="Blues",
    ax=ax
)

st.pyplot(fig)


# --------------------------------------------------
# INFLUENCE SCORES
# --------------------------------------------------

st.header(
    " Influence Scores"
)

st.dataframe(
    score_df,
    use_container_width=True
)


# --------------------------------------------------
# CLUSTERS
# --------------------------------------------------

st.header(
    " Researcher Clusters"
)

st.dataframe(
    cluster_df,
    use_container_width=True
)


# --------------------------------------------------
# GEMINI SUMMARY
# --------------------------------------------------

st.header(
    " AI Generated Analysis"
)

with st.spinner(
    "Generating insights..."
):

    summary = generate_llm_summary(
        combined_profiles,
        similarity_df
    )

with st.expander(
    "View Detailed Analysis",
    expanded=True
):

    st.markdown(summary)


# --------------------------------------------------
# SAVE SUMMARY
# --------------------------------------------------

if st.button(
    " Save Summary"
):

    with open(
        "outputs/llm_summary.txt",
        "w",
        encoding="utf-8"
    ) as f:

        f.write(summary)

    st.success(
        "Summary saved successfully!"
    )