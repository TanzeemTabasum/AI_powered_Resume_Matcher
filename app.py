from resume_parser.pdf_parser import extract_text_from_pdf
from utils.skill_extractor import extract_skills
from matcher.skill_matcher import compare_skills
from matcher.score import calculate_match_score
from matcher.recommendation import get_recommendations


# -----------------------------
# Resume PDF
# -----------------------------

pdf_path = "resume_parser/resume.pdf"

resume_text = extract_text_from_pdf(pdf_path)


# -----------------------------
# Job Description
# -----------------------------

print("\nEnter the Job Description:")
print("(Paste the job description below. Type END when finished.)")

job_lines = []

while True:
    line = input()

    if line.strip() == "END":
        break

    job_lines.append(line)

job_text = "\n".join(job_lines)

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
# Calculate Match Score
# -----------------------------

score = calculate_match_score(
    len(matched_skills),
    len(job_skills)
)


# -----------------------------
# Generate Recommendations
# -----------------------------

recommendations = get_recommendations(missing_skills)


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

print("\nRecommendations:")

for recommendation in recommendations:
    print("-", recommendation)