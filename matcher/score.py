def calculate_match_score(matched_skills, total_required_skills):
    if total_required_skills == 0:
        return 0.0
    
    percentage = (matched_skills / total_required_skills) * 100
    return percentage
