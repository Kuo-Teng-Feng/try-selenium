from webdriver_manager.microsoft import EdgeChromiumDriverManager 
from webdriver_manager.chrome import ChromeDriverManager
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

try:
    driver = webdriver.Chrome(ChromeDriverManager().install())
except:
    driver = webdriver.Edge(EdgeChromiumDriverManager().install())

ac = ActionChains(driver)

def crawler(entry, keyword):
    
    driver.get(entry)

    WebDriverWait(driver,  10, 0.5).until(EC.visibility_of_element_located((By.ID, "gh-ac"))) # search input    
    driver.find_element(By.ID, "gh-ac").send_keys(keyword)
    WebDriverWait(driver,  10, 0.5).until(EC.text_to_be_present_in_element_value((By.ID, "gh-ac"), keyword))
    driver.find_element(By.ID, "gh-btn").submit() # don't wait for the cookie-accept-or-not question.
    
    conditioner()

    sleep(6)

def conditioner():    
    
    WebDriverWait(driver,  10, 0.5).until(EC.visibility_of_element_located((By.CSS_SELECTOR, '#s0-52-12-0-1-2-6 > li.x-refine__main__list--more > span > button')))
    filters = driver.find_element(By.CSS_SELECTOR, '#s0-52-12-0-1-2-6 > li.x-refine__main__list--more > span > button')
# Zustand -> Gebraucht
# Artikelsort -> Deutschland
# Verkäufer -> Verkäuferstyp -> Privat
# Nur Anzeigen -> Verkaufte Artikel

#if_verkauft = '#x-refine__group__9 > ul > li:nth-child(5) > div > a > div > div > div > span.cbx.x-refine__multi-select-cbx'
    #WebDriverWait(driver, 10, 0.5).until(EC.visibility_of_all_elements_located((By.TAG_NAME, "html")))
    



# to catch:    
# class = 's.item__link' href=""
# class = "s-item__price" EUR 199,00
# class = "s-item__shipping s-item__logisticsCost" EUR 18,00 Versand

#def catcher():
    
def all_cookies_accepter():

    WebDriverWait(driver,  10, 0.5).until(EC.visibility_of_all_elements_located((By.TAG_NAME, "html")))
    accept_cookie_button = driver.find_element(By.ID, "gdpr-banner-accept") # cookie accept
    WebDriverWait(driver,  10, 0.5).until(EC.element_to_be_clickable(accept_cookie_button)) # must!
    accept_cookie_button.click()

crawler(infos['entry'][0], infos['keywords'][0])





