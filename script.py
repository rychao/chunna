from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import json
import string
import sys
import datetime

driver = webdriver.Chrome()
driver.get("https://www.ssense.com/en-us/men")
