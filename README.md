# 🌍 TruthAI-Universal

**Mission:** Solve all critical AI & Computer Science challenges as of 2025 in one unified repo.

## Quickstart (Nitro V15)
```bash
pip install -r requirements.txt
export OPENAI_API_KEY="sk-..."
python orchestrator.py --suite core --model openai_default --log logs/core.jsonl
python tools/report.py --log logs/core.jsonl --out reports/core.html
python tools/whitepaper.py --log logs/core.jsonl --out reports/core.pdf
streamlit run tools/dashboard.py
```
Created on 2025-09-30 for Nitro V15 compatibility.
