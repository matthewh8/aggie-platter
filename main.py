import requests
from bs4 import BeautifulSoup
from which_dc import WhichDC
from input_validation_day import WhatDay
from specific_day import TodayMenu
from input_validation_meal import Meal
from food_items import Items
from nutrition_facts import NutritionFacts
from print_menu import PrintMenu
from calculate import Calculate
from print_nutrition import PrintNutrition

if __name__ == "__main__":
    url = WhichDC()
    html_text = requests.get(url).text
    soup = BeautifulSoup(html_text, "lxml")

    day_index = WhatDay() # gets day of week and assigns index to it
    today_menu = TodayMenu(day_index, soup) # uses day_index and html_text to get menu of the day
    this_meal = Meal(today_menu) # gets breakfast, lunch, or dinner menu
    menu_items = Items(this_meal) # gets every menu item that has nutrient facts
    nutrition_facts = NutritionFacts(menu_items) # organizes menu items in a dictionary
    number_of_items = PrintMenu(nutrition_facts) # prints menu in a user-friendly way and gets number of food items
    total_nut = Calculate(nutrition_facts, number_of_items) # gets total nutritional value of meal
    PrintNutrition(total_nut) # prints user's total nutritional value