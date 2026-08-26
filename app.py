from resume_parser.pdf_parser import extract_text_from_pdf
from utils.skill_extractor import extract_skills
from matcher.skill_matcher import compare_skills
from matcher.score import calculate_match_score


# -----------------------------
# Read Resume PDF
# -----------------------------

pdf_path = "resume_parser/resume.pdf"

resume_text = extract_text_from_pdf(pdf_path)


# -----------------------------
# Job Description
# -----------------------------

job_text = """
We are looking for a Python developer with experience
in SQL, Git, Docker, React and JavaScript.
"""


# -----------------------------
# Extract Skills
# -----------------------------

resume_skills = extract_skills(resume_text)

job_skills = extract_skills(job_text)


# -----------------------------
# Compare Skills
# -----------------------------

matched_skills, missing_skills = compare_skills(
    resume_skills,
    job_skills
)


# -----------------------------
# Calculate Score
# -----------------------------

score = calculate_match_score(
    len(matched_skills),
    len(job_skills)
)


# -----------------------------
# Display Results
# -----------------------------

print("\nAI RESUME JOB MATCHER")
print("=====================")

print("\nResume Skills:")
print(resume_skills)

print("\nJob Skills:")
print(job_skills)

print("\nMatched Skills:")
print(matched_skills)

print("\nMissing Skills:")
print(missing_skills)

print("\nMatch Score:")
print(f"{score:.2f}%")