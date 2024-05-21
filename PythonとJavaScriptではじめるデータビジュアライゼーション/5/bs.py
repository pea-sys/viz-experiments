from bs4 import BeautifulSoup
import requests
import requests_cache

requests_cache.install_cache()

BASE_URL = "http://en.wikipedia.org"
HEADERS = {"User-Agent": "Mozilla/5.0"}


def get_Nobel_soup():
    response = requests.get(BASE_URL + "/wiki/List_of_Nobel_laureates", headers=HEADERS)
    return BeautifulSoup(response.content, "lxml")


def get_column_titles(table):
    cols = []
    for th in table.select_one("tr").select("th")[1:]:
        link = th.select_one("a")
        if link:
            cols.append({"name": link.text, "href": link.attrs["href"]})
        else:
            cols.append({"name": th.text, "href": None})
    return cols


def get_Nobel_winners(table):
    cols = get_column_titles(table)
    winners = []
    for row in table.select("tr")[1:-1]:
        year = int(row.select_one("td").text)
        for i, td in enumerate(row.select("td")[1:]):
            for winner in td.select("a"):
                href = winner.attr["href"]
                if not href.startswith("#endnode"):
                    winners.append(
                        {
                            "year": year,
                            "category": cols[i]["name"],
                            "name": winner.text,
                            "link": winner.attrs["href"],
                        }
                    )


def get_winner_nationality(w):
    data = get_url("http://en.wikipedia.org" + w["link"])
    soup = BeautifulSoup(data)
    person_data = {"name": w["name"]}
    attr_rows = soup.select("table.infobox tr")
    for tr in attr_rows:
        try:
            attribute = tr.select_one("th").text
            if attribute == "Nationality":
                person_data[attribute] = tr.select_one("td").text
        except AttributeError:
            pass
    return person_data


soup = get_Nobel_soup()

# print(soup.find("table", {"class": "wikitable sortable"}))
# print(soup.select("table.sortable.wikitable"))
table = soup.select_one("table.sortable.wikitable")
# print(table.select("th"))

# print(get_column_titles(table))

winners = get_Nobel_winners(table)

requests_cache.install_cache("nobel_pages", backend="sqlite", expire_after=7200)

wdata = []
for w in winners[:50]:
    wdata.append(get_winner_nationality(w))

missing_nationality = []
for w in wdata:
    if not w.get("Nationality"):
        missing_nationality.append(w)

print(missing_nationality)
