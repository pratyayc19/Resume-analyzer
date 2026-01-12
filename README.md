# AI-Based Resume Analyzer & Job Suitability Scorer

## Problem
Many candidates are rejected by Applicant Tracking Systems (ATS) without understanding the reason.

## Solution
This project analyzes a resume and compares it with a job description to:
- Extract relevant skills
- Identify missing skills
- Calculate a job suitability percentage

## Tech Stack
- Python
- PyPDF2
- Regular Expressions (NLP preprocessing)

## How It Works
1. Extracts text from resume PDF
2. Cleans and preprocesses text
3. Matches skills using keyword extraction
4. Compares resume with job description
5. Computes suitability score

## How to Run
1. Install dependencies  
   `pip install PyPDF2`
2. Place resume PDF in the project folder
3. Update `job_description.txt`
4. Run  
   `python resume_reader.py`

## Future Improvements
- Semantic skill matching using NLP embeddings
- Web interface using Flask
- Resume ranking for multiple candidates
