import numpy as np


def calculate_influence_scores(
    profiles
):

    scores = []

    for profile in profiles:

        citations = np.log1p(
            int(profile.get("citations", 0))
        )

        h_index = np.log1p(
            int(profile.get("h_index", 0))
        )

        publication_count = len(
            profile.get("publications", [])
        )

        score = (
            0.6 * citations +
            0.3 * h_index +
            0.1 * publication_count
        )

        scores.append(score)

    # Convert to percentage scale
    max_score = max(scores)

    normalized_scores = [
        (s / max_score) * 100
        for s in scores
    ]

    return normalized_scores