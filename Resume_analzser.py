import PyPDF2
import re

# -------- READ RESUME --------
file_path = "Resumetemp.pdf"

with open(file_path, "rb") as file:
    reader = PyPDF2.PdfReader(file)
    text = ""

    for page in reader.pages:
        extracted = page.extract_text()
        if extracted:
            text += extracted + " "

# -------- CLEAN RESUME TEXT --------
text = text.lower()
text = re.sub(r'[^a-z\s]', ' ', text)
text = re.sub(r'\s+', ' ', text)

words = text.split()
resume_text = " ".join(words)

print("Total words:", len(words))

# -------- SKILL LIST --------
skills_list = [
    "python", "java", "c", "c++", "sql",
    "machine learning", "deep learning",
    "data analysis", "numpy", "pandas",
    "scikit learn", "tensorflow", "pytorch",
    "nlp", "linux", "git"
]

# -------- RESUME SKILL MATCHING --------
matched_skills = []
missing_skills = []

for skill in skills_list:
    if skill in resume_text:
        matched_skills.append(skill)
    else:
        missing_skills.append(skill)

# -------- READ JOB DESCRIPTION --------
with open("job_description.txt", "r") as jd:
    jd_text = jd.read().lower()

jd_text = re.sub(r'[^a-z\s]', ' ', jd_text)

# -------- JOB SKILL EXTRACTION --------
job_required_skills = []

for skill in skills_list:
    if skill in jd_text:
        job_required_skills.append(skill)

# -------- MATCH JOB vs RESUME --------
matched_job_skills = []

for skill in job_required_skills:
    if skill in matched_skills:
        matched_job_skills.append(skill)

missing_for_job = []

for skill in job_required_skills:
    if skill not in matched_skills:
        missing_for_job.append(skill)

# -------- SUITABILITY SCORE --------
if job_required_skills:
    suitability_score = (len(matched_job_skills) / len(job_required_skills)) * 100
else:
    suitability_score = 0

# -------- FINAL REPORT --------
print("\n" + "="*50)
print("RESUME ANALYSIS REPORT")
print("="*50)

print("\n✔ Skills Found in Resume:")
for skill in matched_skills:
    print(f"- {skill}")

print("\n✘ Skills Missing from Resume:")
for skill in missing_skills:
    print(f"- {skill}")

print("\n⚠ Skills Required by Job but Missing:")
if missing_for_job:
    for skill in missing_for_job:
        print(f"- {skill}")
else:
    print("None 🎉")

print("\n📊 JOB SUITABILITY SCORE")
print(f"Candidate matches {len(matched_job_skills)} out of {len(job_required_skills)} required skills.")
print(f"Suitability Percentage: {suitability_score:.2f}%")

print("="*50)
