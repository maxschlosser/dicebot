import requests
import random

class Jace:
    def __init__(self):
        self.base_url = "https://api.scryfall.com/cards/search"
        self.order = "name"
        self.sort = "desc"
        self.url = ""
        self.__conditions = {
            "equal": "=",
            "more": ">",
            "less": "<",
            "lessequal": "<=",
            "moreequal": ">=",
            "not": "!="
        }

    def __repr__(self):
        return self.url

    def card(self):
        self.url = f"{self.base_url}?order={self.order}&dir={self.sort}&q="
        return self

    def name(self, name):
        self.url = f"{self.url}{name}+"
        return self

    def cmc(self, cmc, condition="equal"):
        self.url = f"{self.url}cmc{self.__conditions[condition]}{cmc}+"
        return self

    def type(self, type):
        self.url = f"{self.url}t:{type}+"
        return self

    def execute(self):
        r = requests.get(self.url)
        return [card  for card in r.json()["data"]]


def main():
    r = Jace().card().type("Jace").type("legendary").cmc(5, "not").execute()
    card = random.choice(r)
    if card["layout"] != 'normal':
        print(card["name"], card["scryfall_uri"])
    else:
        print(card["name"])
        print(card["mana_cost"], card["type_line"])
        print(card["oracle_text"])
        print(card["scryfall_uri"])


if __name__ == '__main__':
    main()
