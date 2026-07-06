from pathlib import Path
from label_map import ID_TO_LABEL
import pandas as pd


catalog = Path("data/normalized/ntu60_catalog.csv")
pgfa_desc = Path("data/raw/pgfa/descriptions/ntu60_des.txt")
smie_desc = Path("data/raw/smie/descriptions/ntu60_des.txt")
sa_dvae_desc = Path("data/raw/sa_dvae/class_lists/ntu60_llm.txt")

print("Catalog exists :", catalog.exists())
print("PGFA exists    :", pgfa_desc.exists())
print("SMIE exists    :", smie_desc.exists())
# Read description files
pgfa_lines = pgfa_desc.read_text(encoding="utf-8", errors="replace").splitlines()
smie_lines = smie_desc.read_text(encoding="utf-8", errors="replace").splitlines()
sa_dvae_lines = sa_dvae_desc.read_text(
    encoding="utf-8",
    errors="replace"
).splitlines()

print("PGFA lines :", len(pgfa_lines))
print("SMIE lines :", len(smie_lines))

print("\nFirst PGFA description:")
print(pgfa_lines[0])

print("\nFirst SMIE description:")
print(smie_lines[0])
# Read NTU label map
label_map = Path("data/raw/pgfa/descriptions/ntu_labelmap.txt")

labels = label_map.read_text(encoding="utf-8", errors="replace").splitlines()

print("Total labels:", len(labels))
print("First label:", labels[0])
print("60th label:", labels[59])
import pandas as pd

# Build fresh NTU-60 catalog
catalog_df = pd.DataFrame({
 
    "class_id": list(range(1, 61)),
    "canonical_name": [ID_TO_LABEL[i] for i in range(1, 61)],
    "pgfa_description": pgfa_lines,
    "smie_description": smie_lines,
   "sa_dvae_description": sa_dvae_lines,
    "star_description": ["MISSING"] * 60,
})
# Character length and token count
for source in [
    "pgfa_description",
    "smie_description",
    "sa_dvae_description",
    "star_description",
]:
    catalog_df[source + "_chars"] = catalog_df[source].astype(str).str.len()

    catalog_df[source + "_tokens"] = (
        catalog_df[source]
        .astype(str)
        .str.split()
        .str.len()
    )

output_dir = Path("data/processed")
output_dir.mkdir(parents=True, exist_ok=True)

csv_path = output_dir / "ntu60_descriptions.csv"
parquet_path = output_dir / "ntu60_descriptions.parquet"

catalog_df.to_csv(csv_path, index=False)
catalog_df.to_parquet(parquet_path, index=False)

print("\nFiles written successfully.")
print("CSV      :", csv_path)
print("Parquet  :", parquet_path)
print("Rows     :", len(catalog_df))
print("Columns  :", list(catalog_df.columns))
report_dir = Path("reports")
report_dir.mkdir(exist_ok=True)

report_path = report_dir / "phase1_catalog.md"

sources = [
    "pgfa_description",
    "smie_description",
    "sa_dvae_description",
    "star_description",
]

with open(report_path, "w", encoding="utf-8") as f:
    f.write("# Phase 1 Catalog Report\n\n")

    for source in sources:
        coverage = (catalog_df[source] != "MISSING").sum()
        total = len(catalog_df)

        mean_chars = catalog_df[source + "_chars"].mean()
        median_chars = catalog_df[source + "_chars"].median()

        mean_tokens = catalog_df[source + "_tokens"].mean()
        median_tokens = catalog_df[source + "_tokens"].median()

        f.write(f"## {source}\n")
        f.write(f"- Coverage: {coverage}/{total}\n")
        f.write(f"- Mean characters: {mean_chars:.2f}\n")
        f.write(f"- Median characters: {median_chars:.2f}\n")
        f.write(f"- Mean tokens: {mean_tokens:.2f}\n")
        f.write(f"- Median tokens: {median_tokens:.2f}\n\n")

    # Summary (outside the loop)
    f.write("## Summary\n\n")
    f.write("- PGFA, SMIE and SA-DVAE contain identical NTU-60 descriptions in the downloaded repositories.\n")
    f.write("- STAR global NTU-60 description file was not present in the downloaded repository; therefore all STAR entries are explicitly marked as MISSING.\n")

print("Report written:", report_path)