import sys
from pathlib import Path

# Add src folder to Python path
sys.path.append(str(Path(__file__).resolve().parents[1] / "src"))

from label_map import ID_TO_LABEL, LABEL_TO_ID


def test_bijective_mapping():
    # Total labels
    assert len(ID_TO_LABEL) == 60
    assert len(LABEL_TO_ID) == 60

    # Every ID -> Label -> ID should match
    for idx, label in ID_TO_LABEL.items():
        assert LABEL_TO_ID[label] == idx

    print("✓ Label mapping is bijective for all 60 classes.")


if __name__ == "__main__":
    test_bijective_mapping()