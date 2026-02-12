
---

# 🚀 LucidSQL AI — Local Natural Language to SQL Intelligence

> **Enterprise-grade AI database assistant that converts natural language into SQL queries and executes them instantly — powered by a fully local LLM.**

**LucidSQL AI** enables users to interact with databases using plain English. It uses **LangChain + Ollama + Llama 3 + Streamlit** to automatically generate SQL queries and return structured results through a professional dashboard.

⚡ Runs locally
🔒 Privacy-first
🌐 Offline capable
🤖 AI-powered database querying

---

# ✨ Features

## 🧠 AI-Powered SQL Generation

* Converts natural language → SQL automatically
* Schema-aware query generation
* Uses Llama 3 via Ollama

## ⚡ Fully Local AI (No Cloud APIs)

* Runs completely on your machine
* No OpenAI or external API calls
* Privacy-safe architecture
* Offline support after setup

## 📊 Automatic Query Execution

* Executes generated SQL instantly
* Displays results in structured tables

## 🎨 Professional Dashboard UI

* Clean enterprise-grade interface
* Dark theme adaptive styling
* Responsive layout
* Session state management

## 🔐 Secure Query Pipeline

* Uses only database schema
* Prevents invalid queries
* Safe SQL execution

## 🗄️ SQLite Database Integration

* Lightweight local database
* Easy setup
* Fast performance

---

# 🖼️ Application Preview

## 🔹 Overview Dashboard

👉<img width="1906" height="965" alt="image" src="https://github.com/user-attachments/assets/ab84b014-175d-42e6-b045-d96a1015e4f6" />


---

## 🔹 Generated SQL + Results

👉 <img width="1807" height="665" alt="image" src="https://github.com/user-attachments/assets/e960ac17-05cf-483e-81e1-5ed37f94ec01" />


---

# 🧠 How It Works

## Pipeline Flow

```
User Question
      ↓
Prompt Engineering
      ↓
LangChain SQL Generator
      ↓
Local Llama 3 (Ollama)
      ↓
SQL Query Execution
      ↓
Results Displayed in UI
```

### Step-by-Step Process

1. User enters a natural language question.
2. Database schema + question sent to LLM.
3. Llama 3 generates SQL query.
4. SQL executes on SQLite database.
5. Results displayed in Streamlit UI.

---

# 🏗️ Architecture

## Fully Local AI Stack

```
Frontend        → Streamlit
AI Engine       → Ollama + Llama 3 (Local)
LLM Framework   → LangChain
Database        → SQLite
Data Handling   → Pandas
```

### Why this architecture is powerful:

✅ No cloud dependency
✅ Data never leaves your machine
✅ Works offline
✅ Privacy-first design
✅ Low latency inference

---

# 🌐 Offline Capability

LucidSQL AI runs **fully offline** after initial setup.

### Internet required only for:

* Installing dependencies
* Installing Ollama
* First-time model download

### After setup:

✅ No internet required
✅ Local AI inference
✅ Local database execution

---

# 🏗️ Tech Stack

| Technology | Purpose              |
| ---------- | -------------------- |
| Python     | Core development     |
| Streamlit  | UI framework         |
| LangChain  | LLM orchestration    |
| Ollama     | Local LLM runtime    |
| Llama 3    | SQL generation model |
| SQLite     | Database             |
| Pandas     | Data processing      |

---

# 📂 Project Structure

```
LucidSQL-AI/
│
├── app.py
├── project.db
├── requirements.txt
├── README.md
```

---

# ⚡ Installation & Setup

## 1️⃣ Clone Repository

```bash
git clone https://github.com/yourusername/LucidSQL-AI.git
cd LucidSQL-AI
```

---

## 2️⃣ Create Virtual Environment (Recommended)

```bash
python -m venv venv
```

### Activate Environment

**Windows**

```bash
venv\Scripts\activate
```

**Mac/Linux**

```bash
source venv/bin/activate
```

---

## 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

Or manually:

```bash
pip install streamlit pandas langchain langchain-community langchain-ollama
```

---

## 4️⃣ Install Ollama

Download from:

👉 [https://ollama.com](https://ollama.com)

Verify installation:

```bash
ollama --version
```

---

## 5️⃣ Download Llama 3 Model (One-Time Setup)

```bash
ollama run llama3
```

After this step → fully offline usage.

---

## 6️⃣ Run Application

```bash
streamlit run app.py
```

Open in browser:

```
http://localhost:8501
```

---

# 💬 Example Queries

Try asking:

* Show all students with grade A
* Average score by subject
* Top 5 highest scoring students
* Count students per subject
* List students with score above 80

---

# 🎯 Use Cases

* AI-powered data exploration
* Business intelligence dashboards
* SQL learning tools
* Database assistants
* Analytics systems
* Enterprise internal tools

---

# 🔐 Security

* Schema-restricted SQL generation
* Safe result handling
* No direct user SQL execution
* Local data processing

---

# 🚀 Future Improvements

* Chat-style conversational interface
* Automatic data visualization
* Multi-database support (MySQL/PostgreSQL)
* Query explanation feature
* SQL optimization suggestions
* Query history tracking
* Authentication system
* Cloud deployment

---

# 👨‍💻 Developer

**Upayan Chatterjee**
AI & Data Systems Enthusiast • Full Stack Developer

---

# ⭐ Contributing

Contributions are welcome!

1. Fork repository
2. Create feature branch
3. Commit changes
4. Open pull request

---


