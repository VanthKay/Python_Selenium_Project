from time import sleep
import subprocess
import os
from python_training.project_pageobject.Tests.ebay_seleniumbase import SeleniumBase

# This test compares between the two lowest numbers and prints out the lowest one from the two

# Run the price analyze for PS5
subprocess.run(["python", "results_ps5.py"])
# Run the price analyze for XBOX
subprocess.run(["python", "results_xbox.py"])
with open("cheapest_price_ps5.txt", "r") as file:
    cheapest_price_ps5 = float(file.read().strip())
sleep(3)
with open("cheapest_price_xbox.txt", "r") as file:
    cheapest_price_xbox = float(file.read().strip())
compared_price = min(cheapest_price_ps5, cheapest_price_xbox)
print(f"The lowest price is {compared_price} Shekels")
print("The test has been completed.")
# Replace 'file_path_ps5/xbox_price' with the path to the file you want to delete
file_path_ps5_price = "C:/Users/anton/PycharmProjects/training/python_training/project_pageobject/Tests/cheapest_price_ps5.txt"
file_path_xbox_price = "C:/Users/anton/PycharmProjects/training/python_training/project_pageobject/Tests/cheapest_price_xbox.txt"
os.remove(file_path_ps5_price)
os.remove(file_path_xbox_price)
