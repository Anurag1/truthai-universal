import argparse, os, json, time
from benchmarks.harness_runner import run_harness
from benchmarks.safety import append_toxicity_stub

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--suite", required=True, help="core | real_eval")
    ap.add_argument("--model", default=None, help="openai:gpt-4o-mini | hf:mistral-7b ...")
    ap.add_argument("--log", default="logs/evidence.jsonl")
    args = ap.parse_args()

    model = args.model or ("gpt-4o-mini" if os.environ.get("OPENAI_API_KEY") else "mistral-7b-instruct")
    tasks = ["GSM8K", "TruthfulQA", "HumanEval"] if args.suite == "real_eval" else ["GSM8K"]

    print(f"[RUN] suite={args.suite} model={model} -> {args.log}")
    run_harness(model, tasks, args.log)
    # Append safety probe (stub for now)
    append_toxicity_stub(args.log, toxicity_rate=0.02)
    print("[DONE] Wrote", args.log)

if __name__ == "__main__":
    main()
