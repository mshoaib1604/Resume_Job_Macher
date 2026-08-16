import csv
from pathlib import Path

SKILLS_FILE = Path(__file__).resolve().parents[1] / "data" / "skills.csv"

def load_skills():
    skills = []
    with open(SKILLS_FILE, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            skills.append(row["skill"].strip().lower())
    return sorted(set(skills), key=len, reverse=True)

def extract_skills(text: str):
    text = f" {text.lower()} "
    found = []
    for skill in load_skills():
        # Flexible boundary matching for technical skills such as C++ and .NET
        escaped = skill.replace("+", r"\+").replace(".", r"\.")
        import re
        if re.search(r"(?<!\w)" + escaped + r"(?!\w)", text):
            found.append(skill)
    return sorted(set(found))
