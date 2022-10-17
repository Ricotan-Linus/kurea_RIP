import time ; import random ; from selenium import webdriver ; import cnfg

while True:
    driver = webdriver.Firefox(executable_path=cnfg.pth)
    url = cnfg.url
    driver.get(url)
    time.sleep(random.randint(25,40))
    driver.quit()
    time.sleep(random.randint(400,900))
