from dotenv import load_dotenv
load_dotenv()

from google import genai
from google.genai import types
from pydantic import BaseModel

client = genai.Client()
MODEL = "gemini-3.5-flash-lite"


class JobAnalysis(BaseModel):
  title: str
  required_experience_years: int = 0
  required_skills: list[str]
  nice_to_have_skills: list[str] = []
  work_type: str = "Not specified"
  salary_min: float | None = None
  salary_max: float | None = None
  salary_currency: str | None = None
  english_level: str | None = None
  matching_skills: list[str] = []
  missing_skills: list[str] = []


candidate_skills = ["Python", "FastAPI", "PostgreSQL", "Docker", "Git"]

job_postings = [
    """
    We are looking for a Python Backend Developer.
    The candidate should have at least 2 years of experience with
    Python and Django. Experience with PostgreSQL and Docker is required.
    Nice to have: Redis and Celery.
    The position is remote and the salary is $1500-$2500 per month.
    English B2 or higher is required.
    """,

    """
    Junior Python Developer wanted for our office in Tbilisi.
    Must know Python and FastAPI. Git is a plus.
    Experience required: 1 year.
    """,

    """
    We need someone who knows programming and can help us with backend tasks.
    """,
]

system_instruction = """
You are an expert HR and Recruitment AI assistant. 
Your task is to analyze the provided Job Posting text and compare the requirements with the given Candidate Skills.
Extract the structured fields accurately. If any information (like salary, english level, or experience) is missing in the text, handle it gracefully by setting it to None or 0 as defined in the schema.
"""

for i in range(len(job_postings)):
  job_text = job_postings[i]
  print("=" * 40)
  print(f"Job Posting #{i + 1} Analysis")
  print("=" * 40)

  prompt = f"""
    Candidate skills:
    {", ".join(candidate_skills)}

    Job Posting Text:
    {job_text}
    """

  response = client.models.generate_content(
      model=MODEL,
      contents=prompt,
      config=types.GenerateContentConfig(
          system_instruction=system_instruction,
          response_mime_type="application/json",
          response_schema=JobAnalysis,
          temperature=0.1,
      ),
  )

  result = response.parsed


  print(f"Title: {result.title}")
  print(f"Required Experience: {result.required_experience_years} years")
  print(f"Required Skills: {result.required_skills}")
  print(f"Nice-to-have Skills: {result.nice_to_have_skills}")
  print(f"Work Type: {result.work_type}")
  print(f"Salary: {result.salary_min} - {result.salary_max} {result.salary_currency or ''}")
  print(f"English Level: {result.english_level}")
  print(f"Matching Skills: {result.matching_skills}")
  print(f"Missing Skills: {result.missing_skills}")