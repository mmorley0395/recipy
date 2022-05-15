import pandas as pd
import requests
from bs4 import BeautifulSoup


class Recipe:
    def __init__(self, url):
        self.url = url
        self.ing_tags = None
        self.name = None
        self.ingredients = None
        self.time = None  # not in li/ul tags, need to find separately
        self.directions = None

    def process_url(self):
        """uses Beautiful Soup to grab the ingredients list from the URL"""
        page = requests.get(self.url)
        soup = BeautifulSoup(page.text, "html.parser")
        ingredients_container = soup.find_all("ul", class_="wprm-recipe-ingredients")
        ingredients_container = str(ingredients_container[0])
        soup = BeautifulSoup(ingredients_container, "html.parser")
        self.ing_tags = soup.find_all("li")

    def produce_names(self):
        """produces a list of ingredient names"""
        ing_list = []
        for tag in self.ing_tags:
            ing_name = tag.find_all("span", class_="wprm-recipe-ingredient-name")
            ing_name = ing_name[0].get_text()
            ing_list.append(ing_name)
        self.ing_list = ing_list
        print(self.ing_list)

    def produce_amounts(self):
        """produces quantities list for ingredients"""
        amounts_list = []
        for tag in self.ing_tags:
            ing_amount = tag.find_all("span", class_="wprm-recipe-ingredient-amount")
            ing_amount = ing_amount[0].get_text()
            amounts_list.append(ing_amount)
        self.amounts_list = amounts_list
        print(self.amounts_list)

    def produce_units(self):
        """produces a list of units"""
        units_list = []
        for tag in self.ing_tags:
            unit_name = tag.find_all("span", class_="wprm-recipe-ingredient-unit")
            unit_name = unit_name[0].get_text()
            units_list.append(unit_name)
        self.units_list = units_list
        print(self.units_list)


R1 = Recipe("https://minimalistbaker.com/wprm_print/90501")
print(R1.url)
R1.process_url()
R1.produce_names()
R1.produce_amounts()
R1.produce_units()
