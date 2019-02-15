from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://www.google.com/maps")

elem = driver.find_element_by_xpath('//*[@id="searchbox-directions"]')
elem.click()
