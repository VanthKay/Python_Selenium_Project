from python_training.project_pageobject.Tests.results_ps5 import results_ps5

with open("cheapest.txt", "r") as f:
    cheapest_price_ps5 = int(f.read())
    cheapest_price_xbox = int(f.read())


class compare_xbox_ps5_price():
      min(cheapest_price_ps5,cheapest_price_xbox)