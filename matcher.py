from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def calculate_match(resume_text, job_text, resume_skills, job_skills):
    # NLP similarity
    vectorizer = TfidfVectorizer(stop_words="english", ngram_range=(1, 2))
    matrix = vectorizer.fit_transform([resume_text, job_text])
    similarity = float(cosine_similarity(matrix[0:1], matrix[1:2])[0][0])

    # Skill coverage
    resume_set = set(resume_skills)
    job_set = set(job_skills)
    matching = sorted(resume_set.intersection(job_set))
    missing = sorted(job_set - resume_set)

    if job_set:
        skill_coverage = len(matching) / len(job_set)
    else:
        skill_coverage = 0.0

    # Combined score: semantic/text similarity + explicit skill coverage
    score = (0.40 * similarity + 0.60 * skill_coverage) * 100
    score = min(100.0, max(0.0, score))

    return {
        "score": score,
        "matching_skills": matching,
        "missing_skills": missing,
        "text_similarity": similarity,
        "skill_coverage": skill_coverage,
    }
