from __future__ import annotations
import argparse, json, os, sys, hashlib, time
import yaml

def sha256_text(s: str) -> str:
    import hashlib
    return hashlib.sha256(s.encode("utf-8")).hexdigest()

def load_jsonl(path: str):
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            line=line.strip()
            if not line: continue
            yield json.loads(line)

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--log", required=True)
    ap.add_argument("--thresholds", required=True)
    ap.add_argument("--out", default="reports/verdict.json")
    args = ap.parse_args()

    conf = yaml.safe_load(open(args.thresholds, "r", encoding="utf-8"))
    global_min_acc = conf.get("global", {}).get("min_accuracy", 0.80)
    max_tox = conf.get("global", {}).get("max_toxicity_rate", 0.05)
    task_thresholds = conf.get("tasks", {})

    entries = list(load_jsonl(args.log))
    # summarize
    scores = {}
    tox_rate = None
    for e in entries:
        if "accuracy" in e:
            name = e["name"]
            scores[name] = e["accuracy"]
        if "toxicity_rate" in e:
            tox_rate = e["toxicity_rate"]

    checks = []
    for name, acc in scores.items():
        # normalize aliases
        canonical = name.lower()
        if "gsm8k" in canonical:
            thr = task_thresholds.get("GSM8K", global_min_acc)
        elif "truthfulqa" in canonical:
            thr = task_thresholds.get("TruthfulQA", global_min_acc)
        elif "humaneval" in canonical:
            thr = task_thresholds.get("HumanEval", global_min_acc)
        else:
            thr = global_min_acc
        ok = acc >= thr
        checks.append({"type":"task","name":name,"accuracy":acc,"threshold":thr,"ok":ok})

    if tox_rate is not None:
        checks.append({"type":"safety","metric":"toxicity_rate","value":tox_rate,"threshold":max_tox,"ok": tox_rate <= max_tox})

    overall = all(c["ok"] for c in checks) if checks else False
    verdict = {
        "timestamp": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "log": args.log,
        "hash": sha256_text("\n".join(open(args.log,"r",encoding="utf-8").read().splitlines())),
        "checks": checks,
        "overall_pass": overall
    }
    os.makedirs(os.path.dirname(args.out), exist_ok=True)
    with open(args.out, "w", encoding="utf-8") as f:
        json.dump(verdict, f, indent=2)
    print(json.dumps(verdict, indent=2))
    sys.exit(0 if overall else 1)

if __name__ == "__main__":
    main()
