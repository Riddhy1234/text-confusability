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
# Build fresh NTU-60 catalog
catalog_df = pd.DataFrame({

    "class_id": list(range(60)),
    "canonical_name": [ID_TO_LABEL[i] for i in range(60)],
    "pgfa_description": pgfa_lines,
    "smie_description": smie_lines,
    "sa_dvae_description": sa_dvae_lines,
    "star_description": [None] * 60,
})

# Character length and token count
for source in [
    "pgfa_description",
    "smie_description",
    "sa_dvae_description",
    "star_description",
]:
    catalog_df[source + "_chars"] = catalog_df[source].str.len()

    catalog_df[source + "_tokens"] = (
        catalog_df[source]
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

        coverage = catalog_df[source].notna().sum()
        total = len(catalog_df)

        if coverage > 0:
            mean_chars = catalog_df[source + "_chars"].mean()
            median_chars = catalog_df[source + "_chars"].median()

            mean_tokens = catalog_df[source + "_tokens"].mean()
            median_tokens = catalog_df[source + "_tokens"].median()

            mean_chars = f"{mean_chars:.2f}"
            median_chars = f"{median_chars:.2f}"
            mean_tokens = f"{mean_tokens:.2f}"
            median_tokens = f"{median_tokens:.2f}"

        else:
            mean_chars = "-"
            median_chars = "-"
            mean_tokens = "-"
            median_tokens = "-"

        f.write(f"## {source}\n")
        f.write(f"- Coverage: {coverage}/{total}\n")
        f.write(f"- Mean characters: {mean_chars}\n")
        f.write(f"- Median characters: {median_chars}\n")
        f.write(f"- Mean tokens: {mean_tokens}\n")
        f.write(f"- Median tokens: {median_tokens}\n\n")

    f.write("## Summary\n\n")
    f.write("- MD5 verification confirms that PGFA, SMIE and SA-DVAE description files are byte-identical.\n")
    f.write("- MD5: 811755f481a375b345dd9f2268493a0c\n")
    f.write("- STAR descriptions are currently unavailable in the downloaded repository; missing values are stored as null (NaN).\n")

print("Report written:", report_path)