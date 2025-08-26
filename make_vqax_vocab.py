import json
from collections import Counter
import os

base = "data/vqax"

with open(os.path.join(base, "train_x.json")) as f:
    train = json.load(f)
with open(os.path.join(base, "val_x.json")) as f:
    val = json.load(f)

# alle Antworten sammeln
answers = [ex["answer"] for ex in (train + val)]

# Häufigkeiten zählen
counter = Counter(answers)

# ggf. Top-K, hier: alle
top_answers = [a for a, _ in counter.most_common()]

# Mappings bauen
ans2label = {a: i for i, a in enumerate(top_answers)}
label2ans = {i: a for a, i in ans2label.items()}

# speichern
with open(os.path.join(base, "trainval_ans2label.json"), "w") as f:
    json.dump(ans2label, f)
with open(os.path.join(base, "trainval_label2ans.json"), "w") as f:
    json.dump(label2ans, f)

print(f"Gespeichert: {len(ans2label)} Antworten")