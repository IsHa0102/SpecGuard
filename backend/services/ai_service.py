import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def generate_test_cases(schema):
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You generate API test cases."},
                {"role": "user", "content": f"""
Given this schema:
{schema}

Generate:
1. Valid test cases
2. Invalid test cases

Return JSON only.
"""}
            ],
            temperature=0.2
        )

        return response.choices[0].message.content

    except Exception as e:
        # 🔥 FALLBACK (THIS IS THE WIN)
        return {
            "note": "AI unavailable, using fallback test cases",
            "valid_cases": [
                {"name": "Test User", "email": "test@example.com", "age": 25}
            ],
            "invalid_cases": [
                {"name": "", "email": "invalid", "age": 10}
            ]
        }