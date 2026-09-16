from google import genai

from config.settings import (
    GEMINI_API_KEY,
    GEMINI_MODEL
)


client = genai.Client(
    api_key=GEMINI_API_KEY
)


def generate_outreach(profile, tone, goal):

    with open(
        "config/services/prompts/outreach_prompt.txt",
        "r",
        encoding="utf-8"
    ) as file:

        prompt_template = file.read()

    prompt = prompt_template.format(
        profile=profile,
        tone=tone,
        goal=goal
    )

    response = client.models.generate_content(
        model=GEMINI_MODEL,
        contents=prompt
    )

    return response.text


def parse_response(response):

    subject = ""
    email = ""
    followup = ""

    if "SUBJECT:" in response:

        parts = response.split(
            "SUBJECT:",
            1
        )[1]

        if "EMAIL:" in parts:

            subject_part, parts = parts.split(
                "EMAIL:",
                1
            )

            subject = subject_part.strip()

        if "FOLLOW_UP:" in parts:

            email_part, followup_part = parts.split(
                "FOLLOW_UP:",
                1
            )

            email = email_part.strip()
            followup = followup_part.strip()

        else:

            email = parts.strip()

    return {
        "subject": subject,
        "email": email,
        "followup": followup
    }