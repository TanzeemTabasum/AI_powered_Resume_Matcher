def compare_skills(resume_skills, job_skills):
    intersect = resume_skills.intersection(job_skills)
    diff = job_skills.difference(resume_skills)
    return intersect, diff



resume_skills = {"python", "SQL", "Git"}
job_skills = {"python", "SQL", "Git", "Docker"}

matching_skills, missing_skills = compare_skills(resume_skills, job_skills)

print("Matching Skills : ", matching_skills)
print("Missing Skills : ", missing_skills)
