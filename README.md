# Banking AI Assistant

An AI-powered banking assistant that analyzes bank transaction data, provides financial insights, visualizes spending patterns, and enables users to interact with their bank statements using conversational AI.

Built using Streamlit, Gemini LLM, RAG Architecture, ChromaDB, and HuggingFace Embeddings.

---

## Features

### Bank Statement Upload

* Upload bank transaction data using CSV files.
* Automatically processes and analyzes transactions.

### Financial Dashboard

Provides:

* Total Income
* Total Expense
* Savings
* Expense by Category visualization

### AI Banking Assistant

Users can ask questions about their transactions.

Examples:

* How much did I spend on food?
* What is my highest expense?
* How much did I spend on travel?

The AI generates responses based only on the uploaded bank statement data.

### Transaction Search

Search transactions using descriptions.

Examples:

* Amazon
* Swiggy
* Uber
* Salary

### Financial Insights

Automatically identifies:

* Highest expense
* Spending categories
* Financial observations

### RAG Based Question Answering

This project uses Retrieval Augmented Generation (RAG) to provide accurate answers from bank transaction data.

```
Bank Statement
       |
       ↓
Transaction Documents
       |
       ↓
HuggingFace Embeddings
       |
       ↓
ChromaDB Vector Store
       |
       ↓
Retriever
       |
       ↓
Gemini LLM
       |
       ↓
AI Response
```

---

## Tech Stack

### Frontend

* Streamlit

### Data Processing

* Python
* Pandas

### AI / LLM

* Google Gemini API

### RAG Components

* LangChain
* ChromaDB
* HuggingFace Sentence Transformers

### Visualization

* Matplotlib

---

## Project Structure

```
Banking-AI-Assistant/

│
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── services/
│   ├── csv_reader.py
│   ├── analyzer.py
│   ├── chart.py
│   ├── chatbot.py
│   ├── llm.py
│   ├── embeddings.py
│   └── vector_store.py
│
└── chroma_db/
```

---

## Installation

### Clone Repository

```bash
git clone <https://github.com/HemamaliniSelvaraj4264/Banking-AI-Assistant.git>
```

### Create Virtual Environment

```bash
python -m venv .venv
```

Activate environment:

Windows:

```bash
.venv\Scripts\activate
```

---

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Environment Setup

Create a `.env` file:

```
GOOGLE_API_KEY=your_gemini_api_key
```

---

## Run Application

```bash
streamlit run app.py
```

Application runs at:

```
http://localhost:8501
```

---

## Example Interaction

User:

```
How much did I spend on food?
```

AI Response:

```
You spent ₹830 on food.

Swiggy - ₹350
Milk - ₹60
Zomato - ₹420

Total: ₹830
```

---

## Future Improvements

* PDF bank statement support
* Monthly spending analysis
* AI financial recommendations
* Download financial reports
* User authentication
* Multi-user banking profiles

---

## Author

Hemamalini Selvaraj


