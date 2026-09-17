from pathlib import Path
import hashlib
import json

import numpy as np
import pandas as pd
from sentence_transformers import SentenceTransformer

# Load NTU-60 descriptions
csv_path = Path("data/processed/ntu60_descriptions.csv")
df = pd.read_csv(csv_path)

# Output directory
output_dir = Path("embeddings")
output_dir.mkdir(exist_ok=True)

# Encoder
encoder_name = "all-mpnet-base-v2"
model = SentenceTransformer(encoder_name)

sources = [
    "canonical_name",
    "pgfa_description",
    "smie_description",
    "sa_dvae_description",
    "star_description",
]

for source in sources:
    texts = df[source].fillna("").astype(str).tolist()

    # Generate embeddings
    embeddings = model.encode(
        texts,
        convert_to_numpy=True,
        show_progress_bar=True
    )

    # Save .npy
    npy_file = output_dir / f"{source}_{encoder_name}.npy"
    np.save(npy_file, embeddings)

    # Content hash
    text_blob = "\n".join(texts).encode("utf-8")
    content_hash = hashlib.sha256(text_blob).hexdigest()

    metadata = {
        "encoder": encoder_name,
        "source": source,
        "shape": list(embeddings.shape),
        "dimension": int(embeddings.shape[1]),
        "content_hash": content_hash,
    }

    json_file = output_dir / f"{source}_{encoder_name}.json"

    with open(json_file, "w", encoding="utf-8") as f:
        json.dump(metadata, f, indent=2)

    print(f"✓ Finished {source}")

print("\nAll embeddings generated successfully.")