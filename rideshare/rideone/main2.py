from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time



def critical():

    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get("https://www.google.com/maps")

    f = open('rideone/find.txt', 'r')
    read = f.read().split()
    print(read)
    elem = driver.find_element_by_xpath('//*[@id="searchbox-directions"]')
    elem.click()
    time.sleep(15)
    elem2 = driver.find_element_by_xpath('//*[@id="omnibox-directions"]/div/div[2]/div/div/div[1]/div[2]/button/div[1]')
    elem2.click()

    j =0
    for i in read:
        j+=1
        if j>2:
            elm7 = driver.find_element_by_xpath('//*[@id="omnibox-directions"]/div/div[3]/button/div[1]/div').click()
        time.sleep(3)
        button = driver.find_element_by_xpath('//*[@id="omnibox-directions"]/div/div[3]/button/div[1]/div')
        elem4 = driver.find_element_by_xpath('//*[@id="sb_ifc5'+str(j)+'"]/input')
        elem4.send_keys(i)
        elem5 = driver.find_element_by_xpath('//*[@id="directions-searchbox-'+str(j-1)+'"]/button[1]').click()


    time.sleep(10)
    elem6 = driver.find_element_by_xpath('//*[@id="section-directions-trip-0"]/div[2]/div[1]/div[1]/div[2]/div')
    l=[]
    print(elem6.text)
    for x in elem6.text.split():

            try:
                if type(int(x)) == int:
                    l.append(x)
                pass
            except Exception as e:
                pass
    distance = ''.join(l)
    return distance
