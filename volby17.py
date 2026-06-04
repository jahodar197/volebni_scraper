# projekt_3.py: třetí projekt
# author: Roman Jahoda
# email: jahodar197@gmail.com

import requests
from bs4 import BeautifulSoup
import csv
import time

def get_html(url):
    headers = {"User-Agent": "Mozilla/5.0"}

    for _ in range(3):
        try:
            print("Načítám stránku:", url)
            r = requests.get(url, headers=headers, timeout=10)
            r.encoding = "utf-8"
            return BeautifulSoup(r.text, "lxml")
        except:
            print("Server neodpověděl, zkouším to znovu…")
            time.sleep(1)

    raise Exception("Server volby.cz odmítá spojení.")

def get_towns(url):
    print("Načítám seznam obcí…")
    soup = get_html(url)
    towns = []
    base = "https://volby.cz/pls/ps2017nss/"

    for row in soup.find_all("tr"):
        cells = row.find_all("td")
        if len(cells) >= 3 and cells[0].find("a"):
            code = cells[0].text.strip()
            name = cells[1].text.strip()
            link = base + cells[0].find("a")["href"]
            towns.append((code, name, link))

    print(f"Nalezeno obcí: {len(towns)}")
    return towns

def get_town_data(town):
    code, name, link = town
    print(f"Zpracovávám obec: {name} ({code})")

    soup = get_html(link)
    tables = soup.find_all("table")

    t0 = tables[0].find_all("td")
    voters = t0[3].text.replace("\xa0", "")
    envelopes = t0[6].text.replace("\xa0", "")
    valid = t0[7].text.replace("\xa0", "")

    parties = {}
    for table in tables[1:]:
        for row in table.find_all("tr")[2:]:
            cells = row.find_all("td")
            if len(cells) >= 3:
                party = cells[1].text.strip()
                votes = cells[2].text.replace("\xa0", "")
                parties[party] = votes

    return {
        "Kód obce": code,
        "Obec": name,
        "Voliči": voters,
        "Obálky": envelopes,
        "Platné hlasy": valid,
        **parties
    }

def scrape_election_data(url, output_file):
    towns = get_towns(url)
    all_data = []
    all_parties = set()

    print("Začínám stahovat data z jednotlivých obcí…")

    for town in towns:
        data = get_town_data(town)
        all_data.append(data)
        all_parties.update(data.keys())
        time.sleep(0.3)

    base_cols = ["Kód obce", "Obec", "Voliči", "Obálky", "Platné hlasy"]
    party_cols = sorted([p for p in all_parties if p not in base_cols])
    header = base_cols + party_cols

    with open(output_file, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=header)
        writer.writeheader()
        writer.writerows(all_data)

    print(f"Hotovo! Výsledky jsou uložené v souboru {output_file}")
scrape_election_data("https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=2&xnumnuts=2101", "benesov_volby17.csv")
