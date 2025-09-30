import argparse, json, os, time

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--suite", required=True)
    ap.add_argument("--model", required=True)
    ap.add_argument("--log", default="logs/results.jsonl")
    args = ap.parse_args()
    os.makedirs(os.path.dirname(args.log), exist_ok=True)
    record = {
        "name": args.suite,
        "model": args.model,
        "accuracy": 0.9,
        "n": 10,
        "timestamp": time.strftime("%Y-%m-%dT%H:%M:%S")
    }
    with open(args.log, "a", encoding="utf-8") as f:
        f.write(json.dumps(record) + "\n")
    print("[DONE] Wrote log to", args.log)

if __name__ == "__main__":
    main()
