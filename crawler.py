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

# find search input -> keyin keyword
def crawler(entry, keyword):
    
    driver.get(entry)

    input_id = "gh-ac"
    WebDriverWait(driver,  10, 0.5).until(EC.visibility_of_element_located((By.ID, input_id))) # search input    
    driver.find_element(By.ID, input_id).send_keys(keyword) # chrome can directly proceed without submit command.
    if 'dge' in driver.name: # "msedge" for Edge browser.
        WebDriverWait(driver,  10, 0.5).until(EC.text_to_be_present_in_element_value((By.ID, input_id), keyword))
        driver.find_element(By.ID, "gh-btn").submit() # submit button. don't wait for the cookie-accept-or-not popup.

# add conditions, if keyword not precise enough to get an accurate result.    
    conditioner()
    #sleep(6)

def conditioner():    
    
    filters_loc = '#s0-52-12-0-1-2-6 > li.x-refine__main__list--more > span > button'
    filters = driver.find_element(By.CSS_SELECTOR, filters_loc)
    WebDriverWait(driver,  10, 0.5).until(EC.element_to_be_clickable(filters))
    filters.click()
    
    popup_className = "x-overlay__wrapper--left"
    WebDriverWait(driver, 10, 0.5).until(EC.visibility_of_all_elements_located((By.CLASS_NAME, popup_className)))
    options_className = "x-overlay-aspect__label"
    options = driver.find_elements(By.CLASS_NAME, options_className)
    
    
    
# Zustand -> Gebraucht
# Artikelsort -> Deutschland
# Verkäufer -> Verkäuferstyp -> Privat
# Nur Anzeigen -> Verkaufte Artikel
# Uebernehmen

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





