import streamlit as st
from src.text_processor import clean_text
from src.skill_extractor import extract_skills
from src.matcher import calculate_match

st.set_page_config(page_title="AI Resume Job Matcher", page_icon="🤖", layout="wide")

st.title("🤖 AI-Powered Resume Screening & Job Matching System")
st.caption("NLP-based resume and job description matching")

resume_file = st.file_uploader("Upload Resume (.txt)", type=["txt"])
job_text = st.text_area("Paste Job Description", height=250)

if st.button("Analyze Match", type="primary"):
    if not resume_file or not job_text.strip():
        st.warning("Please upload a resume and paste a job description.")
    else:
        resume_text = resume_file.read().decode("utf-8", errors="ignore")

        resume_clean = clean_text(resume_text)
        job_clean = clean_text(job_text)

        resume_skills = extract_skills(resume_clean)
        job_skills = extract_skills(job_clean)

        result = calculate_match(resume_clean, job_clean, resume_skills, job_skills)

        st.subheader("📊 Match Result")
        st.metric("Job Match Score", f"{result['score']:.1f}%")

        col1, col2 = st.columns(2)

        with col1:
            st.markdown("### ✅ Matching Skills")
            if result["matching_skills"]:
                for skill in result["matching_skills"]:
                    st.write(f"✓ {skill}")
            else:
                st.write("No matching skills detected.")

        with col2:
            st.markdown("### ❌ Missing Skills")
            if result["missing_skills"]:
                for skill in result["missing_skills"]:
                    st.write(f"✗ {skill}")
            else:
                st.write("No major missing skills detected.")

        st.markdown("### 🎯 Recommendations")
        if result["missing_skills"]:
            st.write(
                "Focus on learning or strengthening: "
                + ", ".join(result["missing_skills"])
                + "."
            )
        else:
            st.write("Your detected skills cover the main skills identified in the job description.")

        with st.expander("Detected Resume Skills"):
            st.write(", ".join(resume_skills) if resume_skills else "None")

        with st.expander("Detected Job Skills"):
            st.write(", ".join(job_skills) if job_skills else "None")
