#!/usr/bin/env python3
"""
Example: Run hormonal explosion on the classic horror movie dataset.
"""
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))

from semantic_pipeline.ingest import ingest_corpus
from semantic_pipeline.embedding import embed_items
from semantic_pipeline.foam_metric import compute_foam_matrix
from orchestra.session import HormonalExplosionSession
import json


def main():
    # Load corpus
    data_path = Path(__file__).parent.parent / "datasets" / "movies" / "classic_horror.csv"
    items = ingest_corpus(data_path)
    print(f"Ingested {len(items)} items")

    # Compute embeddings and foam
    embeddings = embed_items(items)
    foam = compute_foam_matrix(embeddings)
    print(f"Foam matrix shape: {foam.shape}")

    # Run explosion session
    session = HormonalExplosionSession(foam, items)
    final_comp, history = session.run(max_iterations=15)

    # Save result
    output_path = Path(__file__).parent.parent / "output" / "scenarios" / "explosion_result.json"
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with open(output_path, 'w') as f:
        json.dump({
            'final_composition': [item['metadata'] for item in final_comp],
            'phi_history': history['phi'],
            'hormonal_history': history['hormonal_index']
        }, f, indent=2)
    print(f"Saved explosion result to {output_path}")


if __name__ == "__main__":
    main()
