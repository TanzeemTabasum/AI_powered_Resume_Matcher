from matcher.skill_matcher import compare_skills
from matcher.score import calculate_match_score

resume_skills = {"python", "SQL", "Git"}

job_skills = {"python", "SQL", "Git", "Docker"}

matched_skills, missing_skills = compare_skills(resume_skills, job_skills)

score = calculate_match_score(len(matched_skills), len(job_skills))

print("AI Resume Job Matcher")
print("-----------------------------")

print("Matched Skills:")
print(matched_skills)

print("\nMissing Skills:")
print(missing_skills)

print("\nMatch Score:")
print(f"{score:.2f}%")