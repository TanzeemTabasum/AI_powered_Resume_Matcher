import string

def clean_text(text):
    stop_words = {"the", "is", "and", "with", "a", "an", "of", "for", "to", "in", "on", "at", "but", "or", "he", "she", "it", "they"}
    clean_str = text.lower().translate(text.maketrans("", "", string.punctuation))
    words = [word for word in clean_str.split() if word not in stop_words]
    return words

print(clean_text("Python Developer, with experience in SQL!"))

