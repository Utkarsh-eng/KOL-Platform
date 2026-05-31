from sklearn.metrics.pairwise import cosine_similarity

import pandas as pd


def compute_similarity_matrix(
    embeddings,
    names
):

    similarity_matrix = cosine_similarity(
        embeddings
    )

    similarity_df = pd.DataFrame(
        similarity_matrix,
        index=names,
        columns=names
    )

    return similarity_df