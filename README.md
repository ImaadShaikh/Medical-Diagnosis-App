Here it is as plain text — select all and copy:

```
# 🏥 Medical Diagnosis App

An AI-powered medical diagnosis assistant that takes a symptom description and returns structured clinical insights — extracted symptoms, potential diagnoses, and relevant PubMed research summaries — all running on a **fully local LLM** with no cloud API costs.

---

## 🏗️ Architecture

```
<img width="1024" height="1024" alt="image" src="https://github.com/user-attachments/assets/0a4b5c99-4afc-4100-a4ac-cbc4f7020dc3" />

```

---

## ✨ Features

- **Symptom Extraction** — Parses free-text descriptions into structured symptom lists
- **AI Diagnosis** — Generates differential diagnoses using LLaMA 3 via Ollama (fully local, no API key needed)
- **PubMed Integration** — Searches and summarizes relevant medical literature in real-time
- **Dual Interface** — Accessible via REST API (FastAPI) and MCP tool protocol
- **Structured Output** — Returns clean JSON with symptoms, diagnoses, and evidence-based summaries
- **Privacy-First** — All LLM inference runs locally; no patient data leaves your machine

---

## 🛠️ Tech Stack

| Layer | Technology |
|-------|------------|
| API Framework | FastAPI |
| MCP Protocol | Custom MCP Server (mcp_tool.py) |
| AI Engine | Ollama + LLaMA 3 (local inference) |
| Medical Literature | PubMed API (NCBI E-utilities) |
| Language | Python 3.10+ |
| Output Format | JSON |

---

## 📁 Project Structure

```
medical-diagnosis-app/
│
├── app.py                        # FastAPI entry point
├── mcp_tool.py                   # MCP Server definition
├── modules/
│   ├── symptom_extractor.py      # Extracts structured symptoms from text
│   ├── diagnosis_module.py       # Generates differential diagnoses via Ollama
│   ├── pubmed_search.py          # Searches PubMed for relevant literature
│   └── summarizer.py             # Summarizes PubMed results
├── requirements.txt
└── README.md
```

---

## 🚀 Getting Started

### Prerequisites

- Python 3.10+
- Ollama installed and running locally — https://ollama.com

### 1. Pull the LLaMA 3 model

```
ollama pull llama3
```

### 2. Clone and install

```
git clone https://github.com/yourusername/medical-diagnosis-app.git
cd medical-diagnosis-app
pip install -r requirements.txt
```

### 3. Environment Variables

Create a .env file:

```
OLLAMA_BASE_URL=http://localhost:11434
OLLAMA_MODEL=llama3
PUBMED_API_KEY=your_pubmed_api_key_here
```

### 4. Run

```
# FastAPI server
uvicorn app:app --reload

# Or via MCP
python mcp_tool.py
```

---

## 📤 Example Request

```
POST /diagnose
{
  "symptoms": "I have a persistent dry cough, mild fever, and fatigue for the past 5 days"
}
```

## 📥 Example Response

```
{
  "extracted_symptoms": ["dry cough", "mild fever", "fatigue"],
  "diagnosis": [
    "Upper respiratory tract infection",
    "Viral bronchitis",
    "COVID-19"
  ],
  "pubmed_summary": "Studies highlight dry cough and low-grade fever as common presentations in viral respiratory infections..."
}
```

---

## ⚠️ Disclaimer

This application is for **educational and research purposes only**. It is not a substitute for professional medical advice, diagnosis, or treatment. Always consult a qualified healthcare provider.

---

## 📄 License

MIT License — feel free to fork and build on this.
```
