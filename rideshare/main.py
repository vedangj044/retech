from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager as c

brower = webdriver.Chrome(c().install())

website_URL ="https://www.google.co.in/"
brower.get(website_URL)
