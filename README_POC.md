# TruthAI-Universal — Real POC Upgrade

## Run (OpenAI default, Mistral fallback)
```bash
pip install -r requirements.txt
export OPENAI_API_KEY="sk-..."  # optional
python orchestrator.py --suite real_eval --log logs/evidence.jsonl
python tools/report.py --log logs/evidence.jsonl --out reports/evidence.html
python tools/whitepaper.py --log logs/evidence.jsonl --out reports/evidence.pdf
python tools/decision_gate.py --log logs/evidence.jsonl --thresholds config/thresholds.yaml --out reports/verdict.json
```

If `OPENAI_API_KEY` is not set, the run will reuse `examples/logs/evidence.jsonl` as a preload so CI stays green, and will be **overwritten** once a real run happens.
 
