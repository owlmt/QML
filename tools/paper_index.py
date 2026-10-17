"""Build a feasibility index of every manifest paper from its PDF text.

Usage: python tools/paper_index.py --cache <dir outside repo> --out <csv path>

For each manifest row the PDF text is extracted once (cached as <cache>/<QC-ID>.txt) and
scanned for dataset names, frameworks, model families and reported-metric phrases, so that
papers can be prioritised for reproduction without opening each PDF.
"""
import argparse
import csv
import re
import sys
from pathlib import Path

from pypdf import PdfReader

REPO = Path(__file__).resolve().parents[1]
MANIFEST = REPO / "manifest.csv"

DATASETS = {
    "NSL-KDD": r"NSL[- ]?KDD", "KDD99": r"KDD[- ]?(Cup[- ]?)?(99|1999)", "UNSW-NB15": r"UNSW[- ]?NB15",
    "CIC-IDS2017": r"CIC[- ]?IDS[- ]?2017|CICIDS2017", "CSE-CIC-IDS2018": r"IDS[- ]?2018",
    "CICDDoS2019": r"CIC[- ]?DDoS[- ]?2019", "CICIoT2023": r"CIC[- ]?IoT[- ]?2023", "Bot-IoT": r"Bot[- ]?IoT",
    "TON_IoT": r"TON[_ -]?IoT", "N-BaIoT": r"N[- ]?BaIoT", "Edge-IIoTset": r"Edge[- ]?IIoT", "IoT-23": r"IoT[- ]?23",
    "MQTT-IoT-IDS": r"MQTT", "X-IIoTID": r"X[- ]?IIoTID", "WUSTL": r"WUSTL", "CIC-MalMem": r"MalMem",
    "Drebin": r"Drebin", "CICAndMal": r"CIC[- ]?AndMal|CICMalDroid|MalDroid", "AndroZoo": r"AndroZoo",
    "EMBER": r"\bEMBER\b", "BODMAS": r"BODMAS", "Microsoft Malware (BIG)": r"Microsoft Malware|BIG[- ]?2015",
    "SOREL": r"SOREL", "PhiUSIIL": r"PhiUSIIL", "UCI phishing": r"Phishing Websites|UCI.{0,40}phish",
    "PhishTank": r"PhishTank", "ISCX-URL": r"ISCX[- ]?URL", "Malicious URLs (Kaggle)": r"malicious[_ ]?urls|Malicious URL",
    "Spambase": r"Spambase", "Enron": r"Enron", "CEAS": r"CEAS", "TrustPilot/SMS spam": r"SMS Spam",
    "Car-Hacking (HCRL)": r"Car[- ]?Hacking|HCRL", "ROAD": r"\bROAD\b", "CAN-intrusion": r"CAN[- ]?intrusion",
    "Mississippi power/ICS": r"Morris|Mississippi State|power system dataset", "SWaT": r"SWaT", "WADI": r"WADI",
    "HAI": r"\bHAI\b", "Gas pipeline": r"gas pipeline", "IEEE bus (smart grid)": r"IEEE[- ]?(14|30|39|57|118)[- ]?bus",
    "Ethereum/Etherscan": r"Etherscan|Ethereum", "Elliptic (Bitcoin)": r"Elliptic", "BitcoinHeist": r"BitcoinHeist",
    "CTU-13": r"CTU[- ]?13", "ISCX botnet": r"ISCX.{0,10}[Bb]otnet", "DGA": r"\bDGA\b", "CIRA-CIC-DoHBrw": r"DoHBrw",
    "USTC-TFC": r"USTC", "VPN-nonVPN": r"ISCX[- ]?VPN", "FaceForensics": r"FaceForensics", "ASVspoof": r"ASVspoof",
    "Celeb-DF": r"Celeb[- ]?DF", "MNIST": r"\bMNIST\b", "Fashion-MNIST": r"Fashion[- ]?MNIST", "CIFAR": r"CIFAR",
    "Iris": r"\bIris\b", "Breast cancer (Wisconsin)": r"Wisconsin|breast cancer", "Credit card fraud": r"credit[- ]?card",
    "Kaggle": r"Kaggle", "Hugging Face": r"Hugging ?Face", "UCI": r"UCI (Machine Learning|ML) Repository|archive\.ics\.uci",
    "synthetic data": r"synthetic(ally generated)? (data|dataset)", "make_moons/blobs": r"make_(moons|circles|blobs)",
    "ad hoc dataset": r"ad[- ]?hoc (data|dataset)",
}
FRAMEWORKS = {
    "Qiskit": r"Qiskit", "PennyLane": r"PennyLane", "TensorFlow Quantum": r"TensorFlow[- ]?Quantum|\bTFQ\b",
    "Cirq": r"\bCirq\b", "torchquantum": r"torchquantum|TorchQuantum", "D-Wave": r"D[- ]?Wave", "Braket": r"Braket",
    "IBM hardware": r"ibm[qm]?_[a-z]+|IBM Quantum (device|hardware|computer|processor)", "Classiq": r"Classiq",
    "PyTorch": r"PyTorch", "TensorFlow": r"TensorFlow", "scikit-learn": r"scikit[- ]?learn|sklearn",
}
MODELS = {
    "QSVM/quantum kernel": r"QSVM|quantum kernel|QSVC|kernel[- ]?based quantum", "VQC": r"\bVQC\b|variational quantum classifier",
    "QNN": r"\bQNN\b|quantum neural network", "QCNN": r"\bQCNN\b|quantum convolutional", "QLSTM": r"QLSTM|quantum LSTM",
    "QGAN": r"QGAN|quantum GAN|quantum generative adversarial", "Quantum autoencoder": r"quantum auto[- ]?encoder|\bQAE\b",
    "QAOA/annealing": r"QAOA|quantum annealing|QUBO", "Quantum federated": r"quantum federated|QFL",
    "QBM": r"quantum Boltzmann", "QRL": r"quantum reinforcement", "Quantum transfer learning": r"quantum transfer learning",
    "Quanvolutional": r"quanvolution", "Hybrid QNN layer": r"hybrid quantum[- ]?classical|hybrid quantum neural",
    "Adversarial attack (FGSM/PGD)": r"FGSM|\bPGD\b|adversarial (example|perturbation)", "Poisoning": r"poison",
    "Backdoor/Trojan": r"backdoor|trojan", "Model extraction": r"model (extraction|stealing|theft)",
    "Membership inference": r"membership inference", "Side channel": r"side[- ]?channel|crosstalk", "Survey": r"\bsurvey\b|systematic review|literature review",
}
METRIC_RE = re.compile(r"(accuracy|F1|precision|recall|AUC|detection rate)[^.\n]{0,60}?(\d{1,3}(?:\.\d+)?\s?%)", re.I)
CODE_RE = re.compile(r"github\.com/[\w.-]+/[\w.-]+", re.I)
QUBIT_RE = re.compile(r"(\d{1,3})[- ]qubits?", re.I)


def find(text, table):
    return "; ".join(k for k, pat in table.items() if re.search(pat, text, re.I))


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--cache", required=True)
    ap.add_argument("--out", required=True)
    ap.add_argument("--limit", type=int, default=0)
    args = ap.parse_args()
    cache = Path(args.cache)
    cache.mkdir(parents=True, exist_ok=True)
    with MANIFEST.open(encoding="utf-8", newline="") as f:
        rows = list(csv.DictReader(f))
    if args.limit:
        rows = rows[: args.limit]
    out_rows = []
    for i, row in enumerate(rows, 1):
        qc = row["QC-ID"]
        folder = row["Assigned cybersecurity topic folder(s)"].split(";")[0].strip()
        pdf = REPO / folder / row["PDF filename"]
        txt_path = cache / f"{qc}.txt"
        pages = ""
        if txt_path.exists():
            text = txt_path.read_text(encoding="utf-8", errors="replace")
        else:
            try:
                reader = PdfReader(str(pdf))
                pages = str(len(reader.pages))
                text = "\n".join((p.extract_text() or "") for p in reader.pages)
            except Exception as e:  # noqa: BLE001
                text = f"EXTRACTION ERROR: {e}"
            text = text.encode("utf-8", errors="replace").decode("utf-8")
            txt_path.write_text(text, encoding="utf-8")
        metrics = "; ".join(f"{m.group(1)} {m.group(2)}" for m in list(METRIC_RE.finditer(text))[:6])
        qubits = sorted({int(m.group(1)) for m in QUBIT_RE.finditer(text) if int(m.group(1)) <= 200})
        out_rows.append({
            "QC-ID": qc, "Year": row["Year"], "Title": row["Full paper title"], "Topic": folder,
            "chars": len(text), "datasets": find(text, DATASETS), "frameworks": find(text, FRAMEWORKS),
            "models": find(text, MODELS), "qubit mentions": ",".join(map(str, qubits[:8])),
            "code links": "; ".join(sorted(set(CODE_RE.findall(text)))[:4]), "metric snippets": metrics,
        })
        if i % 25 == 0:
            print(f"{i}/{len(rows)} done", flush=True)
    with open(args.out, "w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(out_rows[0].keys()))
        w.writeheader()
        w.writerows(out_rows)
    print(f"wrote {args.out} with {len(out_rows)} rows")
    return 0


if __name__ == "__main__":
    sys.exit(main())
