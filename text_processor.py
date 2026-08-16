import re

def clean_text(text: str) -> str:
    """Normalize text for NLP processing."""
    text = text.lower()
    text = re.sub(r"[^a-z0-9+#.\- ]", " ", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text
