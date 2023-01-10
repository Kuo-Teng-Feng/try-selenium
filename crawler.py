from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
#from selenium.common.exceptions import WebDriverException as wde
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait # Important to wait for the web to run. Or: 
from time import sleep # only if there's no applicable EC for WebDriverWait.
import infos

infos = infos.getter() # entry, keywords, login as keys in dict. values: list.

driver = None
try:
    driver = webdriver.Chrome()
except:
    driver = webdriver.Edge()

ac = ActionChains(driver)

def crawler(entry, keyword, login):
    
    driver.get(entry)
    
    WebDriverWait(driver,  10, 0.5).until(EC.visibility_of_element_located((By.ID, "gh-ac"))) # search input
    driver.find_element(By.ID, "gh-ac").send_keys(keyword)
    sleep(3)
    WebDriverWait(driver, 10, 0.5).until(EC.visibility_of_all_elements_located((By.TAG_NAME, "html")))
    

# to catch:    
# class = 's.item__link' href=""
# class = "s-item__price" EUR 199,00
# class = "s-item__shipping s-item__logisticsCost" EUR 18,00 Versand

#def catcher():
    
    
  
print(crawler(infos['entry'][0], infos['keywords'][0], infos['login'][0]))





