import json, os, time

def append_toxicity_stub(log_path: str, toxicity_rate: float = 0.02):
    """Append a synthetic toxicity_rate entry to the log.
    Replace with real toxicity model scoring when desired.
    """
    os.makedirs(os.path.dirname(log_path), exist_ok=True)
    with open(log_path, "a", encoding="utf-8") as f:
        f.write(json.dumps({
            "name": "safety:toxicity",
            "toxicity_rate": toxicity_rate,
            "timestamp": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
        }) + "\n")
