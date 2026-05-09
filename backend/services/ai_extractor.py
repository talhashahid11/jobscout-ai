import os
import json

from groq import Groq
from dotenv import load_dotenv

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)


def extract_candidate_data(cv_text):

    try:

        prompt = f"""
        Analyze this CV carefully.

        Extract:
        - name
        - skills
        - experience
        - role
        - education
        - preferred_jobs

        Return ONLY valid JSON.

        Example:

        {{
          "name": "Wahaj",
          "skills": ["React", "Python"],
          "experience": "2 years",
          "role": "Frontend Developer",
          "education": "BSCS",
          "preferred_jobs": ["Frontend Developer"]
        }}

        CV:
        {cv_text}
        """

        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            temperature=0
        )

        text = response.choices[0].message.content

        text = text.replace("```json", "")
        text = text.replace("```", "")
        text = text.strip()

        return json.loads(text)

    except Exception as e:

        print("AI EXTRACTOR ERROR:")
        print(str(e))

        return {
            "name": "Unknown",
            "skills": [],
            "experience": "",
            "role": "Developer",
            "education": "",
            "preferred_jobs": []
        }