from pathlib import Path

base = Path("data/raw")

print("=" * 50)
print("SOURCE AUDIT")
print("=" * 50)

# SA-DVAE
sa = base / "sa_dvae" / "class_lists"

if (sa / "ntu60.csv").exists():
    lines = open(sa / "ntu60.csv", encoding="utf-8").readlines()
    print(f"SA-DVAE ntu60.csv rows: {len(lines)-1}")

if (sa / "ntu60_llm.txt").exists():
    lines = open(sa / "ntu60_llm.txt", encoding="utf-8").readlines()
    print(f"SA-DVAE ntu60_llm.txt entries: {len(lines)}")

# SMIE
smie = base / "smie" / "descriptions"

if (smie / "ntu60_des.txt").exists():
    lines = open(smie / "ntu60_des.txt", encoding="utf-8").readlines()
    print(f"SMIE ntu60_des.txt entries: {len(lines)}")

# PGFA
pgfa = base / "pgfa" / "descriptions"

if (pgfa / "ntu60_des.txt").exists():
    lines = open(pgfa / "ntu60_des.txt", encoding="utf-8").readlines()
    print(f"PGFA ntu60_des.txt entries: {len(lines)}")

print("=" * 50)
print("DONE")