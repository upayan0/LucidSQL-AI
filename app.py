import streamlit as st
import pandas as pd
from langchain_community.utilities import SQLDatabase
from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

# --------------------------------------------------
# PAGE CONFIG
# --------------------------------------------------
st.set_page_config(
    page_title="LucidSQL AI",
    page_icon="📊",
    layout="wide"
)

# --------------------------------------------------
# THEME-ADAPTIVE PROFESSIONAL CSS
# --------------------------------------------------
st.markdown("""
<style>

/* Do NOT override background (theme-safe) */
.stApp {
    background: none;
}

/* Hero Title */
.hero-title {
    font-size: 58px;
    font-weight: 800;
    text-align: center;
    letter-spacing: -1px;
    margin-bottom: 10px;
}

/* Gradient Accent */
.hero-title span {
    background: linear-gradient(90deg, #2563EB, #7C3AED);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

/* Subtitle */
.hero-subtitle {
    text-align: center;
    font-size: 18px;
    opacity: 0.8;
    margin-bottom: 40px;
}

/* Theme Adaptive Card */
.theme-card {
    padding: 35px;
    border-radius: 18px;
    border: 1px solid rgba(128,128,128,0.25);
}

/* Result Card */
.result-card {
    padding: 25px;
    border-radius: 16px;
    border: 1px solid rgba(128,128,128,0.25);
}

/* Buttons */
div.stButton > button {
    border-radius: 12px;
    font-weight: 600;
    padding: 10px 18px;
}

/* Primary Button */
div.stButton > button:first-child {
    background-color: #2563EB;
    color: white;
    border: none;
}

div.stButton > button:first-child:hover {
    background-color: #1E40AF;
}

/* Footer */
.footer {
    text-align: center;
    font-size: 13px;
    opacity: 0.6;
    margin-top: 60px;
}

</style>
""", unsafe_allow_html=True)

# --------------------------------------------------
# HERO SECTION
# --------------------------------------------------
st.markdown(
    '<div class="hero-title">Lucid<span>SQL</span> AI</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="hero-subtitle">'
    'Enterprise-Grade Natural Language to SQL Intelligence'
    '</div>',
    unsafe_allow_html=True
)

# --------------------------------------------------
# DATABASE + LLM
# --------------------------------------------------
db = SQLDatabase.from_uri("sqlite:///project.db")
schema = db.get_table_info()

llm = ChatOllama(model="llama3", temperature=0)

prompt = ChatPromptTemplate.from_template("""
You are a senior data analyst and SQL expert.

Given the database schema below, write a correct SQL query that answers the user's question.

Rules:
- Use only the tables and columns in the schema
- Do NOT explain anything
- Return ONLY the SQL query

Schema:
{schema}

Question:
{question}
""")

sql_chain = prompt | llm | StrOutputParser()

# --------------------------------------------------
# SESSION STATE
# --------------------------------------------------
if "question" not in st.session_state:
    st.session_state.question = ""

if "sql_query" not in st.session_state:
    st.session_state.sql_query = None

if "result" not in st.session_state:
    st.session_state.result = None

# --------------------------------------------------
# CENTERED INPUT CARD
# --------------------------------------------------
center = st.columns([1,2,1])[1]

with center:
    st.markdown('<div class="theme-card">', unsafe_allow_html=True)

    st.markdown("### Ask Your Database")

    st.session_state.question = st.text_input(
        "Query",
        value=st.session_state.question,
        placeholder="e.g., Show top 5 students by total marks",
        label_visibility="collapsed"
    )

    col1, col2 = st.columns([3,1])

    submit = col1.button("Generate Query 🚀", use_container_width=True)
    clear = col2.button("Clear", use_container_width=True)

    st.markdown('</div>', unsafe_allow_html=True)

# --------------------------------------------------
# CLEAR BUTTON
# --------------------------------------------------
if clear:
    st.session_state.question = ""
    st.session_state.sql_query = None
    st.session_state.result = None
    st.rerun()

# --------------------------------------------------
# SUBMIT BUTTON
# --------------------------------------------------
if submit and st.session_state.question:
    with st.spinner("Analyzing database..."):
        try:
            sql_query = sql_chain.invoke(
                {"schema": schema, "question": st.session_state.question}
            ).strip()

            result = db.run(sql_query)

            st.session_state.sql_query = sql_query
            st.session_state.result = result

        except Exception as e:
            st.error(f"Error: {e}")

# --------------------------------------------------
# RESULTS SECTION
# --------------------------------------------------
if st.session_state.sql_query:

    st.markdown("<br>", unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        st.markdown('<div class="result-card">', unsafe_allow_html=True)
        st.markdown("### Generated SQL")
        st.code(st.session_state.sql_query, language="sql")
        st.markdown('</div>', unsafe_allow_html=True)

    with col2:
        st.markdown('<div class="result-card">', unsafe_allow_html=True)
        st.markdown("### Results")

        try:
            df = pd.DataFrame(eval(st.session_state.result))
            st.dataframe(df, use_container_width=True)
        except:
            st.write(st.session_state.result)

        st.markdown('</div>', unsafe_allow_html=True)

# --------------------------------------------------
# FOOTER
# --------------------------------------------------
st.markdown(
    '<div class="footer">'
    'Powered by LangChain • Ollama • Streamlit<br>'
    'Developed by Upayan Chatterjee'
    '</div>',
    unsafe_allow_html=True
)
