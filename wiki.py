import requests

class WikiSearch():

    def __init__(self, title):

        self.URL = "https://fr.wikipedia.org/w/api.php"
        self.S = requests.Session()
        self.title = title

    def get_title(self):

        PARAMS = {
            'action': "query",
            'list': "search",
            'srsearch': self.title,
            'format': "json",
            'srlimit': 1
        }

        R = self.S.get(url=self.URL, params=PARAMS)
        DATA = R.json()

        return DATA["query"]["search"][0]["title"]

    def extract_info(self):

        title = self.get_title()

        PARAMS = {
            'action': 'query',
            'format': 'json',
            'prop': 'extracts',
            'titles': title,
            'explaintext': True,
            "exlimit": 1,
            'exchars': 175
        }

        R = self.S.get(url=self.URL, params=PARAMS)
        DATA2 = R.json()

        for elt in DATA2["query"]["pages"].values():
            return elt["extract"]