import argparse, json, os

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--log")
    ap.add_argument("--out")
    a = ap.parse_args()

    # 👇 ensure parent directory exists
    os.makedirs(os.path.dirname(a.out), exist_ok=True)

    rows = [json.loads(l) for l in open(a.log)]
    with open(a.out, "w", encoding="utf-8") as f:
        f.write("<html><body><h1>Report</h1><pre>%s</pre></body></html>" % json.dumps(rows, indent=2))

if __name__ == "__main__":
    main()
