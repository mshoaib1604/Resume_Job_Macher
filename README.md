# AI-Powered Resume Screening & Job Matching System

An NLP-based application that compares a resume with a job description and produces a job-match score, matching skills, missing skills, and recommendations.

## Features

- Resume text upload
- Job description input
- Text preprocessing
- Technical skill extraction
- TF-IDF based text similarity
- Cosine similarity
- Skill coverage calculation
- Combined job match score
- Missing skill detection
- Skill recommendations
- Streamlit user interface

## Tech Stack

- Python
- Scikit-learn
- NLP
- TF-IDF
- Cosine Similarity
- Streamlit
- CSV-based skill dictionary

## How the score works

The application combines:

1. 40% NLP text similarity
2. 60% explicit skill coverage

This is a practical prototype rather than a production recruitment model.

## Run locally

Create and activate a virtual environment, then install dependencies:

```bash
pip install -r requirements.txt
```

Run:

```bash
streamlit run app.py
```

Then upload `sample_data/sample_resume.txt` and paste the content of `sample_data/sample_job.txt`.

## Project Structure

```text
AI-Resume-Job-Matcher/
├── app.py
├── requirements.txt
├── README.md
├── data/
│   └── skills.csv
├── src/
│   ├── text_processor.py
│   ├── skill_extractor.py
│   └── matcher.py
└── sample_data/
    ├── sample_resume.txt
    └── sample_job.txt
```

## Important limitation

The current version uses a curated skill dictionary and TF-IDF/cosine similarity. It does not make hiring decisions and should not be used as an automated employment decision system.

## Future Improvements

- PDF/DOCX resume parsing
- Named Entity Recognition
- Sentence-transformer embeddings
- LLM-based resume feedback
- More robust skill taxonomy
- Experience and education extraction
- Database storage
- Authentication
- Cloud deployment
