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

# search input -> keyin keyword
    input_id = "gh-ac"
    WebDriverWait(driver,  10, 0.5).until(EC.visibility_of_element_located((By.ID, input_id))) # search input    
    driver.find_element(By.ID, input_id).send_keys(keyword) # chrome can directly proceed without submit command.
    if 'dge' in driver.name: # "msedge" for Edge browser.
        driver.find_element(By.ID, "gh-btn").submit() # submit button. don't wait for the cookie-accept-or-not popup.

# add conditions, if keyword not precise enough to get an accurate result.    
    conditioner()
    catcher()

def conditioner():    
    
    filters_loc = '#s0-52-12-0-1-2-6 > li.x-refine__main__list--more > span > button'
    filters = driver.find_element(By.CSS_SELECTOR, filters_loc)
    WebDriverWait(driver,  10, 0.5).until(EC.element_to_be_clickable(filters))
    filters.click()
    
    popup_className = "x-overlay__wrapper--left"
    WebDriverWait(driver, 10, 0.5).until(EC.visibility_of_all_elements_located((By.CLASS_NAME, popup_className)))
    options_className = "x-overlay-aspect__label"
    options = driver.find_elements(By.CLASS_NAME, options_className)
    
# find option by text (between open and close tags), not attribute("value"). 'cause it's not like an input in form?
    l = []
    for option in options:
        if option.text in ["Zustand", "Artikelstandort", "Verkäufer", "Nur anzeigen"]:
            l.append(option)
            
    # Zustand -> Gebraucht "c5-subPanel-LH_ItemCondition_Gebraucht"
    # Artikelstandort -> Deutschland "c5-subPanel-location_Deutschland"
    # Verkäufer -> Verkäuferstyp -> Privat "c5-subPanel-_x-seller[1]_toggler" "c5-subPanel-_x-seller[1]-4[1]-0_rbx"
    # Nur anzeigen -> Verkaufte Artikel "c5-subPanel-LH_Sold_Verkaufte%20Artikel"
    
    steps = {'Zustand': ["c3-subPanel-LH_ItemCondition_Gebraucht"], "Artikelstandort": ["c3-subPanel-location_Deutschland-0_rbx"], "Verkäufer": ["c3-subPanel-_x-seller[1]_toggler", "c3-subPanel-_x-seller[1]-4[1]-0_rbx"], "Nur anzeigen": ["c3-subPanel-LH_Sold_Verkaufte%20Artikel"]}
    for op in l:
        WebDriverWait(driver, 10, 0.5).until(EC.element_to_be_clickable(op))
        op.click()
        
        ot = op.text
        mark_ids = steps[ot] # []
        for id in mark_ids:
            sleep(1)
            mark = driver.find_element(By.ID, id)
            #if "ort" in ot: WebDriverWait(driver, 10, 0.5).until(EC.visibility_of_all_elements_located((By.ID, "c3-subPanel")))
            #if "Zu" in ot: WebDriverWait(driver, 10, 0.5).until(EC.element_to_be_clickable(mark))
            #if "Ver" in ot: too much trouble.
            sleep(1) 
            mark.click()
    
# All options/tags up to serve. Then '#c3-footerId > div.x-overlay-footer__apply > button'
    ok = driver.find_element(By.CSS_SELECTOR, "#c3-footerId > div.x-overlay-footer__apply > button")
    WebDriverWait(driver, 10, 0.5).until(EC.element_to_be_clickable(ok))
    ok.click()
   
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

if __name__ == "__main__":

    crawler(infos['entry'][0], infos['keywords'][0])





