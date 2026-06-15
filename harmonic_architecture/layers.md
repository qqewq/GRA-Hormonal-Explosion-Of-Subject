# System Layers

| Layer | Component | Responsibility |
|-------|-----------|----------------|
| **Data** | `datasets/` | Raw corpora (movies, theories, cultural artifacts) |
| **Semantic** | `semantic_pipeline/` | Embeddings, similarity, foam metrics |
| **GRA Foam** | `gra_integration/gra_adapter.py` | Compute global Φ, call GRA‑step |
| **Rank‑N** | `gra_integration/rankN_hooks.py` | Higher‑order derivatives of aesthetic function |
| **Orchestra** | `orchestra/` | Role‑based multi‑agent nullification |
| **Output** | `output/` | Generated playlists, scenarios, meta‑structures |

## Data flow

1. Load corpus → `ingest.py`
2. Compute embeddings → `embedding.py`
3. Calculate foam matrices → `foam_metric.py`
4. Initialize GRA adapter → run nullification loop:
   - Evaluate global foam Φ
   - If Φ > threshold → propose structural changes (via orchestra)
   - Apply GRA step → reduce Φ
5. When Φ stabilizes near zero (global foam nullified) and H is maximal → export masterpiece.
