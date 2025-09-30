import argparse, json, os

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--log", required=True)
    ap.add_argument("--out", required=True)
    a = ap.parse_args()

    os.makedirs(os.path.dirname(a.out), exist_ok=True)

    rows = [json.loads(l) for l in open(a.log, "r", encoding="utf-8")]
    # simple HTML writer
    accs = [r for r in rows if "accuracy" in r]
    tox = [r for r in rows if "toxicity_rate" in r]
    html = ["<html><body><h1>TruthAI-Universal Report</h1>"]
    html.append("<h2>Benchmarks</h2><ul>")
    for r in accs:
        html.append(f"<li>{r.get('name')}: {round(r.get('accuracy',0)*100,2)}% (n={r.get('n')})</li>")
    html.append("</ul>")
    if tox:
        t = tox[-1]["toxicity_rate"]
        html.append(f"<h2>Safety</h2><p>Toxicity rate: {round(t*100,2)}%</p>")
    html.append("<h2>Raw</h2><pre>"+json.dumps(rows, indent=2)+"</pre>")
    html.append("</body></html>")
    with open(a.out, "w", encoding="utf-8") as f:
        f.write("\n".join(html))

if __name__ == "__main__":
    main()
