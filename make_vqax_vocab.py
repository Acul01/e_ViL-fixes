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