from webdriver_manager.microsoft import EdgeChromiumDriverManager 
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
#from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
#from selenium.webdriver.common.keys import Keys
#from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait # Important to wait for the web to run. Or: 
from time import sleep
from data import data
from save import save
import infos

infos = infos.getter() # entry, keywords, login as keys in dict. values: list.

try:
    driver = webdriver.Chrome(ChromeDriverManager().install())
except:
    driver = webdriver.Edge(EdgeChromiumDriverManager().install())

def crawler(keyword): # works only in keyword-form of "str str"

    driver.get(infos['entry'][0]) # unique.
    cu = driver.current_url
# search input -> keyin keyword
    input_id = "gh-ac"
    WebDriverWait(driver, 10, 0.5).until(EC.visibility_of_element_located((By.ID, input_id))) # search input    
    driver.find_element(By.ID, input_id).send_keys(keyword) # chrome can directly proceed without submit command.
    if EC.url_to_be(cu): # if not EC.url_changes(uc) somehow doesn't work. # driver.name "msedge" for Edge browser, which stops here.
        driver.find_element(By.ID, "gh-btn").submit() # submit button. don't wait for the cookie-accept-or-not popup.

# add conditions, if keyword not precise enough to get an accurate result.
    conditioner_gdpv(keyword)
    sleep(2)
    catcher_gdpv(keyword) # only suits specific conditioner.

def conditioner_gdpv(keyword):    
                   
    filters_loc = '#s0-52-12-0-1-2-6 > li.x-refine__main__list--more > span > button'
    filters = driver.find_element(By.CSS_SELECTOR, filters_loc)
    WebDriverWait(driver, 10, 0.5).until(EC.element_to_be_clickable(filters))
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
    # Zustand -> Gebraucht "c3-subPanel-LH_ItemCondition_Gebraucht-0_cbx"
    # Artikelstandort -> Deutschland "c3-subPanel-location_Deutschland-0_rbx"
    # Verkäufer -> Verkäuferstyp -> Privat "c3-subPanel-_x-seller[1]_toggler" "c3-subPanel-_x-seller[1]-4[1]-0_rbx"
    # Nur anzeigen -> Verkaufte Artikel "c3-subPanel-LH_Sold_Verkaufte%20Artikel-0_cbx"                
    steps = {'Zustand': ["c3-subPanel-LH_ItemCondition_Gebraucht-0_cbx"], "Artikelstandort": ["c3-subPanel-location_Deutschland-0_rbx"], "Verkäufer": ["c3-subPanel-_x-seller[1]_toggler", "c3-subPanel-_x-seller[1]-4[1]-0_rbx"], "Nur anzeigen": ["c3-subPanel-LH_Sold_Verkaufte%20Artikel-0_cbx"]}
    for op in l:
        try:
            WebDriverWait(driver, 10, 0.5).until(EC.element_to_be_clickable(op))
        except:
            print(f"{keyword} - no {op.text} there to be clicked.")        
        op.click()

        mark_ids = steps[op.text] # []
        for id in mark_ids:
            try:
                sleep(2)
                mark = driver.find_element(By.ID, id)
            except:
                print(f"{keyword} - lack of required condition(s).")
            #if "ort" in ot: WebDriverWait(driver, 10, 0.5).until(EC.visibility_of_all_elements_located((By.ID, "c3-subPanel")))
            #if "Zu" in ot: WebDriverWait(driver, 10, 0.5).until(EC.element_to_be_clickable(mark))
            #if "Ver" in ot: too much trouble and confusion.
            sleep(2) # Edge needs 2 sec here.
            mark.click()
    
# All options/tags up to serve. Then '#c3-footerId > div.x-overlay-footer__apply > button'
    ok = driver.find_element(By.CSS_SELECTOR, "#c3-footerId > div.x-overlay-footer__apply > button")
    WebDriverWait(driver, 10, 0.5).until(EC.element_to_be_clickable(ok))
    ok.click()

def catcher_gdpv(keyword):
    
    while True:
        _catcher(keyword)
        #save(_catcher(keyword)) # one page.
        try: # one by one.
            _next_page()
            sleep(2)
        except:
            break

def _catcher(keyword): # restricted to one page.
    
    limit = -1
    try: # strict results.                               
        limit = int(driver.find_element(By.CSS_SELECTOR, "#mainContent > div.s-answer-region.s-answer-region-center-top > div > div.clearfix.srp-controls__row-2 > div:nth-child(1) > div.srp-controls__control.srp-controls__count > h1 > span:nth-child(1)").text)
    except: # path could be moderated by website maintainer.
        print(f"{keyword} - no results number found.")

# 1. data:  #srp-river-results > ul > li:nth-child(2) > div > div.s-item__info.clearfix
# 1. _date: #srp-river-results > ul > li:nth-child(2) > div > div.s-item__info.clearfix > div.s-item__title--tag > div > span.POSITIVE
# 1. link:  #srp-river-results > ul > li:nth-child(2) > div > div.s-item__info.clearfix > a
# 1. title: #srp-river-results > ul > li:nth-child(2) > div > div.s-item__info.clearfix > a > div > span
# 1. price: #srp-river-results > ul > li:nth-child(2) > div > div.s-item__info.clearfix > div.s-item__details.clearfix > div:nth-child(1) > span > span
# 1. fee:   #srp-river-results > ul > li:nth-child(2) > div > div.s-item__info.clearfix > div.s-item__details.clearfix > div:nth-child(4) > span    
    if limit > 0: # 0 is also to exclude.
        limit = 2 + limit # 1. data start from li:nth-child(2)
    elif limit == 0: # simply no results.
        return []
    else: # limit = -1. all results in one page. may try excluding system ads or recommendations later.
        sleep(2)
        limit = len(driver.find_elements(By.CSS_SELECTOR, "#srp-river-results > ul > li"))

    l = []
    locs = {}
    
    for n in range(2, limit):    

        unit = f"#srp-river-results > ul > li:nth-child({n}) > div > div.s-item__info.clearfix"
        locs["_date"] = unit + " > div.s-item__title--tag > div > span.POSITIVE"
        locs['title'] = unit + " > a > div > span"
        locs['link'] = unit + " > a"
        locs['price'] = unit + " > div.s-item__details.clearfix > div:nth-child(1) > span > span"
        locs['fee'] = unit + " > div.s-item__details.clearfix > div:nth-child(4) > span"

        for key in locs:
            
            try:
                we = driver.find_element(By.CSS_SELECTOR, locs[key])
                wt = we.text
                if key == "link":
                    locs[key] = we.get_attribute("href")
                elif key == "fee" and "Versand" not in wt: # empty logistic cost
                    locs[key] = ""
                else:    
                    locs[key] = wt        
            except:
                locs[key] = ""
                print(f"{keyword} - no {key} found.")
        
        l.append(data(keyword, locs["_date"], locs['title'], locs['link'], locs['price'], locs['fee']))
        
    return l

# not checked yet.
def _next_page(): 

    next = "#srp-river-results > ul > li.srp-river-answer.srp-river-answer--BASIC_PAGINATION_V2 > div.s-pagination > span > span > nav > a"
    leave = driver.find_element(By.CSS_SELECTOR, next)
    WebDriverWait(driver, 10, 0.5).until(EC.element_to_be_clickable(leave)) # must!
    leave.click()

# not checked yet.
def all_cookies_accepter():

    WebDriverWait(driver, 10, 0.5).until(EC.visibility_of_all_elements_located((By.TAG_NAME, "html")))
    accept_cookie_button = driver.find_element(By.ID, "gdpr-banner-accept") # cookie accept
    WebDriverWait(driver, 10, 0.5).until(EC.element_to_be_clickable(accept_cookie_button)) # must!
    accept_cookie_button.click()

if __name__ == "__main__":
    
    l = infos['keywords']
    
    for keyword in l:
        try:
            crawler(keyword)
        except:
            print(f"{keyword} - error happened, see above for details.")
