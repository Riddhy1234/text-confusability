from pathlib import Path

LABEL_MAP_FILE = Path("data/raw/pgfa/descriptions/ntu_labelmap.txt")

CANONICAL_LABELS = LABEL_MAP_FILE.read_text(
    encoding="utf-8",
    errors="replace"
).splitlines()[:60]

ID_TO_LABEL = {
    i: label
    for i, label in enumerate(CANONICAL_LABELS)
}

LABEL_TO_ID = {
    label: i
    for i, label in enumerate(CANONICAL_LABELS)
}

# Verified variants only.
# Empty until an actual mismatch is found.
LABEL_VARIANTS = {}


def canonical_to_id(label: str) -> int:
    label = LABEL_VARIANTS.get(label, label)

    if label not in LABEL_TO_ID:
        raise ValueError(f"Unknown canonical label: {label}")

    return LABEL_TO_ID[label]