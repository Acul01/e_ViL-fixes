import json
from collections import Counter

# lade Splits
with open("data/train_x.json") as f:
    train = json.load(f)
with open("data/val_x.json") as f:
    val = json.load(f)

# Antworten aus label-Keys extrahieren
answers = []
for ex in (train + val):
    if "label" in ex and isinstance(ex["label"], dict):
        answers.extend(list(ex["label"].keys()))

# häufigste Antworten bestimmen
counter = Counter(answers)
top_answers = [a for a, _ in counter.most_common()]

# Mappings bauen
ans2label = {a: i for i, a in enumerate(top_answers)}
label2ans = {i: a for a, i in ans2label.items()}

# speichern
with open("data/trainval_ans2label.json", "w") as f:
    json.dump(ans2label, f)
with open("data/trainval_label2ans.json", "w") as f:
    json.dump(label2ans, f)
        # Debug-Ausgaben zur Überprüfung der Vokabular-Erstellung
    print(f"[DEBUG] Anzahl eindeutiger Labels: {len(label2ans)}")
    label_keys = list(label2ans.keys())
    if label_keys:
        print(f"[DEBUG] Min Label: {min(map(int, label_keys))}, Max Label: {max(map(int, label_keys))}")
        print(f"[DEBUG] Beispiel Label2Ans: {[(k, label2ans[k]) for k in label_keys[:10]]}")
    ans_keys = list(ans2label.keys())
    if ans_keys:
        print(f"[DEBUG] Beispiel Ans2Label: {[(k, ans2label[k]) for k in ans_keys[:10]]}")