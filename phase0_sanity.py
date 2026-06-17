from sentence_transformers import SentenceTransformer
import numpy as np

print("Loading model...")

model = SentenceTransformer(
    "sentence-transformers/stsb-bert-large",
    device="cpu"
)

sentences = [
    "A person is drinking water.",
    "A person is clapping hands."
]

embeddings = model.encode(sentences)

print("Embedding shape:", embeddings.shape)

assert embeddings.shape == (2, 1024), \
    f"Expected (2,1024), got {embeddings.shape}"

same1 = model.encode(["A person is walking."])
same2 = model.encode(["A person is walking."])

assert np.allclose(same1, same2), \
    "Embeddings are not deterministic"

print("✅ Phase 0 sanity check passed!")
