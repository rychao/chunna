from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import json
# import string
# import sys
# import datetime

driver = webdriver.Chrome()
driver.get("https://kith.com/collections/mens-sale?filter.v.availability=1&filter.v.price.gte=&filter.v.price.lte=")
# driver.find_element(By.CLASS_NAME, "sc-gsDKAQ beKdpw").click()
# WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, "filter-Product type-12"))).click()

product = {}
product['name'] = driver.find_element(By.XPATH, "//*[@id='collection-template']/div[2]/ul/li[1]/div/div/a/h1").text
product['color'] = driver.find_element(By.XPATH, "//*[@id='collection-template']/div[2]/ul/li[1]/div/div/a/h2").text
product['original price'] = driver.find_element(By.XPATH, "//*[@id='collection-template']/div[2]/ul/li[1]/div/div/a/span/span[1]").text
product['sale price'] = driver.find_element(By.XPATH, "//*[@id='collection-template']/div[2]/ul/li[1]/div/div/a/span/span[2]").text

print(product['sale price'])



# driver.get("https://kith.com/collections/mens-sale")
# if link doesn't work, click "jeans" button

# RIP SSENSE
# driver.get("https://www.ssense.com/en-us/men")
# driver.find_element(By.ID, "public-sale-checkbox").click()
