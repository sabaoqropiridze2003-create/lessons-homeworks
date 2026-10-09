from dotenv import load_dotenv
load_dotenv() 

from google import genai
from google.genai import types

client = genai.Client()

response = client.models.generate_content()