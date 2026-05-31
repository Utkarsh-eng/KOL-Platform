import re


def clean_text(text):

    text = text.lower()

    text = text.replace(
        "\n",
        " "
    )

    text = re.sub(
        r"[^a-zA-Z0-9 ]",
        "",
        text
    )

    text = re.sub(
        r"\s+",
        " ",
        text
    )

    return text.strip()


def build_profile_text(profile):

    text = f"""
    {profile.get('name', '')}

    {profile.get('affiliation', '')}

    {' '.join(
        profile.get(
            'research_interests',
            []
        )
    )}

    {' '.join(
        profile.get(
            'publications',
            []
        )
    )}

    {profile.get('paper_title', '')}

    {profile.get('abstract', '')}
    """

    return clean_text(text)