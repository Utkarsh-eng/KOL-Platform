from bs4 import BeautifulSoup


def extract_pubmed(file_path):

    with open(
        file_path,
        "r",
        encoding="utf-8"
    ) as f:

        html = f.read()

    soup = BeautifulSoup(
        html,
        "html.parser"
    )

    # Paper Title
    title = soup.find("h1")

    title = (
        title.text.strip()
        if title
        else ""
    )

    # Abstract
    abstract_div = soup.find(
        "div",
        class_="abstract-content"
    )

    abstract = (
        abstract_div.text.strip()
        if abstract_div
        else ""
    )

    # Authors
    authors = soup.find_all(
        "a",
        class_="full-name"
    )

    authors = [
        author.text.strip()
        for author in authors
    ]

    pubmed_data = {
        "paper_title": title,
        "abstract": abstract,
        "authors": authors
    }

    return pubmed_data