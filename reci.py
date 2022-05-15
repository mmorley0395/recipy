import pandas as pd
import requests
from bs4 import BeautifulSoup


class Recipe:
    def __init__(self, url):
        self.url = url
        # self.ing_tags = None

    def process_url(self):
        """uses Beautiful Soup to grab the ingredients list from the URL"""
        page = requests.get(self.url)
        soup = BeautifulSoup(page.text, "html.parser")
        ingredients_container = soup.find_all("ul", class_="wprm-recipe-ingredients")
        ingredients_container = str(ingredients_container[0])
        soup = BeautifulSoup(ingredients_container, "html.parser")
        self.ing_tags = soup.find_all("li")

    def loop_template(self, list_name, type_name, tag_class: str):
        list_name = []
        for tag in self.ing_tags:
            type_name = tag.find_all("span", class_=f"{tag_class}")
            type_name = type_name[0].get_text()
            list_name.append(type_name)
        self.list_name = list_name
        return self.list_name

    def produce_names(self):
        """produces a list of ingredient names"""
        self.ingredient_list = self.loop_template(
            "ingredient_list", "ing_name", "wprm-recipe-ingredient-name"
        )

    def produce_amounts(self):
        """produces a list of ingredient amounts"""
        self.amounts_list = self.loop_template(
            "amounts_list", "ing_amount", "wprm-recipe-ingredient-amount"
        )

    def produce_units(self):
        """produces a list of ingredient units"""
        self.units_list = self.loop_template(
            "units_list", "unit_name", "wprm-recipe-ingredient-unit"
        )


R1 = Recipe("https://minimalistbaker.com/wprm_print/90501")
print(R1.url)
R1.process_url()
R1.produce_names()
R1.produce_amounts()
R1.produce_units()
