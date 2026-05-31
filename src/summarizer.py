import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()


def generate_llm_summary(
    profiles,
    similarity_df
):
    """
    Generate researcher comparison summary
    using Gemini.
    """

    api_key = os.getenv(
        "GEMINI_API_KEY"
    )

    genai.configure(
        api_key=api_key
    )

    model = genai.GenerativeModel(
        "gemini-2.5-flash"
    )

    prompt = f"""
You are an AI research analyst.

Analyze the following researchers.

Researcher Profiles:
{str(profiles)}

Similarity Matrix:
{similarity_df.to_string()}

Provide:

1. Brief summary of each researcher.
2. Most similar researcher pair.
3. Common research themes.
4. Key differences.
5. Final conclusion.

Keep response under 200 words.
Use professional language.
"""

    try:

        response = model.generate_content(
            prompt
        )

        return response.text

    except Exception as e:

        return f"Error: {str(e)}"