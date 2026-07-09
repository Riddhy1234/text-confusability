import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1] / "src"))

from label_map import ID_TO_LABEL, LABEL_TO_ID


def test_bijective_mapping():
    assert len(ID_TO_LABEL) == 60
    assert len(LABEL_TO_ID) == 60

    for idx, label in ID_TO_LABEL.items():
        assert LABEL_TO_ID[label] == idx


def test_zero_indexing():
    assert ID_TO_LABEL[3] == "Brushing hair"
    assert LABEL_TO_ID["Brushing hair"] == 3

    print("✓ Zero-index mapping verified.")


if __name__ == "__main__":
    test_bijective_mapping()
    test_zero_indexing()
    print("✓ All label map tests passed.")