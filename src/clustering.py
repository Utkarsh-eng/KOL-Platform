from sklearn.cluster import KMeans


def cluster_kols(
    embeddings,
    n_clusters=2
):

    kmeans = KMeans(
        n_clusters=n_clusters,
        random_state=42
    )

    labels = kmeans.fit_predict(
        embeddings
    )

    return labels