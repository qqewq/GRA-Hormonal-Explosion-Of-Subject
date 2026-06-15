"""
Ingest structured data from various formats.
"""
import json
import csv
import pandas as pd
from pathlib import Path
from typing import List, Dict, Any


def load_movies_from_csv(csv_path: Path) -> List[Dict[str, Any]]:
    df = pd.read_csv(csv_path)
    return df.to_dict(orient='records')


def load_movies_from_json(json_path: Path) -> List[Dict[str, Any]]:
    with open(json_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    return data


def load_theories_from_txt(txt_path: Path) -> List[str]:
    with open(txt_path, 'r', encoding='utf-8') as f:
        lines = [line.strip() for line in f if line.strip()]
    return lines


def ingest_corpus(corpus_path: Path) -> List[Dict[str, Any]]:
    """
    Auto‑detect format and return a unified list of items.
    Each item has at least: {'id', 'text', 'metadata'}
    """
    items = []
    if corpus_path.suffix == '.csv':
        raw = load_movies_from_csv(corpus_path)
        for i, entry in enumerate(raw):
            items.append({
                'id': str(i),
                'text': entry.get('description', entry.get('title', '')),
                'metadata': entry
            })
    elif corpus_path.suffix == '.json':
        raw = load_movies_from_json(corpus_path)
        for i, entry in enumerate(raw):
            items.append({
                'id': str(i),
                'text': entry.get('description', entry.get('title', '')),
                'metadata': entry
            })
    elif corpus_path.suffix == '.txt':
        raw = load_theories_from_txt(corpus_path)
        for i, line in enumerate(raw):
            items.append({
                'id': str(i),
                'text': line,
                'metadata': {'source': str(corpus_path), 'line_num': i}
            })
    else:
        raise ValueError(f"Unsupported file type: {corpus_path.suffix}")
    return items
