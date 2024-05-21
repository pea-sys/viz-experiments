import requests

# 現在はユーザー登録をした上でAPIキーをセットする必要がある
REST_EU_ROOT_URL = "http://restcountries.eu/rest/v1"


def REST_country_request(field="all", name="", params=None):
    headers = {"User-Agent": "Mozilla/5.0"}

    if params is None:
        params = {}

    if field == "all":
        return requests.get(REST_EU_ROOT_URL + "/all")

    url = "%s/%s/%s" % (REST_EU_ROOT_URL, field, name)
    print("Requesting URL: " + url)
    response = requests.get(url, params=params, headers=headers)

    if not response.status_code == 200:
        raise Exception("Request failed with status code " + str(response.status_code))

    return response


response = REST_country_request("currency", "usd")
print(response.json)
