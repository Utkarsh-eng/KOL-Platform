from bs4 import BeautifulSoup


def extract_google_scholar(file_path):

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

    # Name
    name = soup.find(
        "div",
        id="gsc_prf_in"
    )

    name = name.text if name else ""

    # Affiliation
    affiliation = soup.find(
        "div",
        class_="gsc_prf_il"
    )

    affiliation = (
        affiliation.text
        if affiliation
        else ""
    )

    # Research Interests
    interests = soup.find_all(
        "a",
        class_="gsc_prf_inta"
    )

    interests = [
        i.text for i in interests
    ]

    # Stats
    stats = soup.find_all(
        "td",
        class_="gsc_rsb_std"
    )

    citations = (
        stats[0].text
        if len(stats) > 0
        else "0"
    )

    h_index = (
        stats[2].text
        if len(stats) > 2
        else "0"
    )

    i10_index = (
        stats[4].text
        if len(stats) > 4
        else "0"
    )

    # Publications
    papers = soup.find_all(
        "a",
        class_="gsc_a_at"
    )

    publications = [
        p.text for p in papers[:10]
    ]

    profile = {
        "name": name,
        "affiliation": affiliation,
        "research_interests": interests,
        "publications": publications,
        "citations": citations,
        "h_index": h_index,
        "i10_index": i10_index
    }

    return profile