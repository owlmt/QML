"""Build the dataset -> notebook usage table for the Cybersecurity Dataset Atlas.

Scans every notebook listed in manifest.csv, detects which atlas datasets its code loads
(pattern table below, keyed by the registry names used in
00_Cybersecurity_Dataset_Atlas/QML_Cybersecurity_Dataset_Atlas.ipynb) and writes
00_Cybersecurity_Dataset_Atlas/atlas_usage.csv with one row per (dataset, notebook):

    dataset, qc_id, topic_folder, notebook_path, paper_title, year, reproduction_status

Run from the repository root with the project venv:
    .venv\\Scripts\\python.exe -X utf8 tools/atlas_usage.py
Re-run after new notebooks are published; the atlas notebook reads the CSV at run time.
"""
import csv
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "00_Cybersecurity_Dataset_Atlas", "atlas_usage.csv")

# (registry name, regex over the notebook's code cells, optional regex over the notebook path)
PATTERNS = [
    ("NSL-KDD", r"NSL_KDD|NSL-KDD|KDDTrain|KDDTest", None),
    ("KDD Cup 1999 (10%)", r"kddcup|fetch_kddcup99|kdd-cup-1999|KDD Cup", None),
    ("CIC-IDS2017", r"CIC-?IDS2017|CICIDS2017|c01dsnap/CIC-IDS2017|StarterArcher|ksay1o", None),
    ("CSE-CIC-IDS2018", r"CIC-?IDS-?2018|CSE-CIC", None),
    ("CIC-DDoS2019", r"CICDDoS2019|CIC-DDoS2019|baalajimaestro", None),
    ("CIC-IoT-2023", r"CIC-?IoT-?2023|lacg030175|CICIoT2023", None),
    ("UNSW-NB15", r"UNSW[-_ ]?NB15|unsw-nb15", None),
    ("CIC-UNSW-NB15", r"bencorn/CIC-UNSW-NB15", None),
    ("TON_IoT (network)", r"codymlewis/TON_IoT|TON_IoT_network|train_test_network|m-hesam-moradian", None),
    ("TON_IoT (IoT telemetry)", r"SilverDragon9|Train_Test_IoT_", None),
    ("NF-ToN-IoT-v2", r"NF-ToN-IoT|NF_ToN", None),
    ("BoT-IoT", r"BoT-IoT|bot-iot|Bot_IoT", None),
    ("IoT-23", r"IoT-?23|IOT23", None),
    ("N-BaIoT", r"N-?BaIoT|n\+baiot|nbaiot", None),
    ("Edge-IIoTset", r"Edge-?IIoT", None),
    ("MQTTset", r"MQTTset|mqttset", None),
    ("Farm-Flow", r"farm-flow|Farm-Flow|10964648", None),
    ("X-IIoTID", r"X-IIoTID", None),
    ("WUSTL-IIoT-2021", r"wustl_iiot|WUSTL-IIoT", None),
    ("WUSTL-EHMS-2020", r"EHMS|ehms", None),
    ("HAI (HIL-based Augmented ICS) 20.07", r"icsdataset/hai|HAI[- ]?2[01]", None),
    ("SWaT", r"SWaT", None),
    ("WADI", r"WADI", None),
    ("BATADAL", r"batadal|BATADAL", None),
    ("Mississippi State / ORNL power system attacks", r"thm0009/icsdatasets|Mississippi|binaryAllNatural|triple\.7z|multiclass\.7z", None),
    ("Ausgrid solar home electricity", r"Ausgrid", None),
    ("OEDI commercial load profiles (Zidi et al. 2022)", r"c3c7329tjj", None),
    ("CIC-MalMem-2022", r"MalMem", None),
    ("ClaMP (Integrated)", r"ClaMP", None),
    ("EMBER 2018", r"EMBER|ember2018", None),
    ("BODMAS", r"BODMAS", None),
    ("Malimg", r"Malimg|MALIMG", None),
    ("Microsoft Malware Classification Challenge (BIG 2015)", r"BIG 2015|malware-classification|BIG2015", None),
    ("Drebin", r"Drebin|drebin", None),
    ("NATICUSdroid", r"naticusdroid|NATICUS", None),
    ("TUANDROMD", r"tuandromd|TUANDROMD", None),
    ("MalwareData (PE features, ml-security-jp)", r"MalwareData\.csv", None),
    ("Ransomware features (ailabteam)", r"ailabteam|ransomware_features", None),
    ("Ransomware detection data set (Chandra)", r"24vv1r1202-Chandra|ransomware-detection-data-set", None),
    ("UCI Phishing Websites", r"phishing\+websites|public/327|id=327", None),
    ("UCI Website Phishing", r"website\+phishing|public/379|id=379", None),
    ("PhiUSIIL Phishing URL", r"PhiUSIIL|phiusiil|public/967|id=967", None),
    ("Web page phishing (Hannousse & Yahiouche)", r"Web_page_Phishing|dataset_phishing\.csv", None),
    ("PhishDataset (ESDAUNG, balanced 20k)", r"ESDAUNG|PhishDataset", None),
    ("PhishStorm URL set (Aalto)", r"urlset\.csv|Vishalya-s", None),
    ("CEAS_08 phishing e-mails", r"CEAS_08|8339691", None),
    ("Ethereum phishing transaction network", r"[Ee]thereum|xblock", r"Ethereum"),
    ("ISCX-URL2016", r"ISCX-?URL|ISCXURL", None),
    ("Malicious and Benign Webpages (Singh 2020)", r"gdx3pkwp47", None),
    ("UCI Spambase", r"spambase|Spambase|public/94\b|id=94\b", None),
    ("Ling-Spam", r"lingspam|Ling-?Spam", None),
    ("SpamFilter corpus (llhyatt98)", r"llhyatt98|SpamFilter", None),
    ("SMS Spam Collection", r"SMSSpam|sms\+spam|smsspamcollection|sms_spam", None),
    ("Enron-Spam", r"enron_spam|Enron-?Spam|ENRON-spam", None),
    ("Botnet DGA Dataset", r"BotnetDgaDataset|dgadata\.blob|Sultanow", None),
    ("CTU-13 (scenario 42)", r"CTU-?13", None),
    ("ISCX-IDS-2012", r"ISCX-?IDS-?2012|ISCX2012|bencorn/ISCX-IDS", None),
    ("CIDDS-001", r"CIDDS", None),
    ("DeCrypto (cryptojacking flows)", r"DeCrypto|7189293", None),
    ("ASVspoof 5", r"12151404|ASVspoof", None),
    ("BETH", r"beth-dataset|BETH", None),
    ("ADFA-LD", r"ADFA", None),
    ("CISA Known Exploited Vulnerabilities", r"known_exploited_vulnerabilities|CISA", None),
    ("Car-Hacking Dataset (HCRL)", r"Car-Hacking|JehadAlyateem", None),
    ("CAN intrusion dataset (OTIDS)", r"ocslab|CAN-intrusion", None),
    ("O-RAN intrusion dataset (reduced)", r"oran_dataset|DiegoAbreuSWB", None),
    ("Kyoto 2006+", r"Kyoto", None),
    ("CIC-Darknet2020", r"Darknet", None),
    ("MNIST", r"(?<![A-Za-z-])MNIST|mnist_784|ylecun/mnist|mnist\.npz|cvdf-datasets/mnist|ossci-datasets/mnist|load_mnist", None),
    ("Fashion-MNIST", r"fashion-mnist|fashion_mnist|Fashion-?MNIST", None),
    ("KMNIST", r"kmnist|KMNIST", None),
    ("EMNIST Letters", r"emnist|EMNIST", None),
    ("GTSRB", r"gtsrb|GTSRB", None),
    ("CIFAR-10", r"cifar|CIFAR", None),
    ("Iris", r"load_iris", None),
    ("Breast Cancer Wisconsin (Diagnostic)", r"load_breast_cancer", None),
    ("Digits (8x8)", r"load_digits", None),
    ("Covertype", r"covtype", None),
    ("Pima Indians Diabetes", r"pima-indians|pima", None),
    ("PennyLane PlusMinus", r"PlusMinus|plus-minus", None),
    ("Synthetic toy sets (make_moons / make_blobs / make_classification)", r"make_moons|make_blobs|make_classification|make_circles", None),
    ("QKD channel simulations", r"QKD|qkd", None),
    ("Gymnasium control states (CartPole, LunarLander)", r"gymnasium|CartPole|LunarLander", None),
]


def main() -> int:
    os.chdir(ROOT)
    rows = list(csv.DictReader(open("manifest.csv", encoding="utf-8-sig")))
    out_rows = []
    for r in rows:
        p = (r.get("Notebook path") or "").strip()
        if not p or not os.path.exists(p):
            continue
        nb = json.load(open(p, encoding="utf-8"))
        code = "\n".join("".join(c["source"]) for c in nb["cells"] if c["cell_type"] == "code")
        folder = p.split("/")[0]
        for name, pat, path_pat in PATTERNS:
            hit = re.search(pat, code) is not None
            if path_pat and re.search(path_pat, p):
                hit = True
            if hit:
                out_rows.append({
                    "dataset": name, "qc_id": r["QC-ID"], "topic_folder": folder, "notebook_path": p,
                    "paper_title": r["Full paper title"], "year": r["Year"],
                    "reproduction_status": r.get("Reproduction status", ""),
                })
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    with open(OUT, "w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=["dataset", "qc_id", "topic_folder", "notebook_path", "paper_title", "year", "reproduction_status"])
        w.writeheader()
        w.writerows(out_rows)
    n_nb = len({r["notebook_path"] for r in out_rows})
    print(f"wrote {OUT}: {len(out_rows)} dataset-notebook pairs, {n_nb} notebooks, "
          f"{len({r['dataset'] for r in out_rows})} datasets")
    return 0


if __name__ == "__main__":
    sys.exit(main())
