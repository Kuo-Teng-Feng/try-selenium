from webdriver_manager.microsoft import EdgeChromiumDriverManager 
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
#from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
#from selenium.webdriver.common.keys import Keys
#from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from time import sleep
from datedealer import datedealer
import sqlite3
import re

def optionsetter(opt): # faster and cleaner without GUI/interface.

    opt.add_argument("--headless")
    opt.add_argument("--incognito")
    opt.add_argument("--disable-gpu")
    opt.add_argument('blink-settings=imagesEnabled=false')
    #opt.add_argument('')

    return opt

try: 
    opt = webdriver.ChromeOptions()
    #opt = optionsetter(opt)
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver = webdriver.Chrome(options = opt)

except:
    opt = webdriver.EdgeOptions()
    #opt = optionsetter(opt)
    driver = webdriver.Edge(EdgeChromiumDriverManager().install())
    driver = webdriver.Edge(options = opt)

def crawler(keyword):

    driver.get("https://www.google.com/search?client=opera&q=xiao&sourceid=opera&ie=UTF-8&oe=UTF-8&hs=V6v&tbs=lrf:!1m4!1u3!2m2!3m1!1e1!1m4!1u2!2m2!2m1!1e1!2m1!1e2!2m1!1e3!2m4!1e17!4m2!17m1!1e2!3sIAE,lf:1,lf_ui:9&tbm=lcl&sxsrf=AJOqlzVfFo1XkC9A5f09hJB14j-JsY1ZJg:1675415002432&rflfq=1&num=10&rldimm=18146486695482477482&lqi=CgR4aWFvSIeE2onTrYCACFoKEAAYACIEeGlhb5IBEWJ1ZmZldF9yZXN0YXVyYW50mgEkQ2hkRFNVaE5NRzluUzBWSlEwRm5TVVIxTTI4eU5UTkJSUkFCqgEMEAEqCCIEeGlhbyhF&phdesc=FAU8_Opu34w&ved=2ahUKEwiZ1sig__j8AhVggv0HHQQKAPkQvS56BAgLEAE&sa=X&rlst=f#rlfi=hd:;si:18146486695482477482,l,CgR4aWFvSIeE2onTrYCACFoKEAAYACIEeGlhb5IBEWJ1ZmZldF9yZXN0YXVyYW50mgEkQ2hkRFNVaE5NRzluUzBWSlEwRm5TVVIxTTI4eU5UTkJSUkFCqgEMEAEqCCIEeGlhbyhF,y,FAU8_Opu34w;mv:[[51.99692691642221,7.6851771800781155],[51.02606091560833,4.7298549144531155],null,[51.51408037099575,6.2075160472656155],9];tbs:lrf:!1m4!1u3!2m2!3m1!1e1!1m4!1u2!2m2!2m1!1e1!2m1!1e2!2m1!1e3!2m4!1e17!4m2!17m1!1e2!3sIAE,lf:1,lf_ui:9")
# Edge cookie accepter is annoying.
#    WebDriverWait(driver, 10, 0.5).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#yDmH0d > c-wiz > div > div > div > div.NIoIEf > div.G4njw > div.AIC7ge > div.CxJub > div.FCY2lb > form:nth-child(1) > div > div > button")))
#    accept = driver.find_element(By.CSS_SELECTOR, "#yDmH0d > c-wiz > div > div > div > div.NIoIEf > div.G4njw > div.AIC7ge > div.CxJub > div.FCY2lb > form:nth-child(1) > div > div > button")
#    WebDriverWait(driver, 10, 0.5).until(EC.element_to_be_clickable(accept))
#    accept.click()

    review = "#akp_tsuid_29 > div > div:nth-child(1) > div > g-sticky-content-container > div > block-component > div > div.dG2XIf.knowledge-panel.Wnoohf.OJXvsb > div > div > div > div.ifM9O > div > div > div:nth-child(5) > div.AfIYPc > g-sticky-content > div > div.YoOupc.UxY8gd.E0kSRb.xSizI > g-tabs > div > div > a:nth-child(4) > div.SVWlSe.t35a5d > span"
    WebDriverWait(driver, 10, 0.5).until(EC.element_to_be_clickable(driver.find_element(By.CSS_SELECTOR, review)))
    review.click()

    recent = "#_VtDcY4TcL7-L9u8PkP2k4AY_8 > div.mR2gOd > div > div:nth-child(2)"
    WebDriverWait(driver, 10, 0.5).until(EC.element_to_be_clickable(driver.find_element(By.CSS_SELECTOR, recent)))
    recent.click()
    
    catcher(keyword)        

    return True

def catcher(keyword):

    con = sqlite3.connect("db.db")
    cur = con.cursor()
    
    for i in range(1, 101): # once for 100 reviews
        
        sq = f"#tsuid_VtDcY4TcL7-L9u8PkP2k4AY_1reviewSort > div > div.gws-localreviews__general-reviews-block > div:nth-child({i}) > div.jxjCjc > div:nth-child(4)"
        timestamp = sq + " > div.PuaHbe > span.dehysf.lTi8oc" # text
        star = sq + " > div.PuaHbe > g-review-stars > span" # aria-label as attribute
        more = sq + " > div.Jtu6Td > span > span > a" # if none, pass.
        txt = sq + " > div.Jtu6Td > span > span > span:nth-child(1) > span" # if none, pass.
        reviewer = f"#tsuid_VtDcY4TcL7-L9u8PkP2k4AY_1reviewSort > div:nth-child(2) > div.gws-localreviews__general-reviews-block > div:nth-child({i}) > div.jxjCjc > div:nth-child(1) > div > a"

        WebDriverWait(driver, 10, 0.5).until(EC.visibility_of_element_located((By.CSS_SELECTOR, timestamp)))
        _date = driver.find_element(By.CSS_SELECTOR, timestamp).text
        WebDriverWait(driver, 10, 0.5).until(EC.visibility_of_element_located((By.CSS_SELECTOR, star)))
        stars = int(re.sub(r"[0\D]", "", driver.find_element(By.CSS_SELECTOR, star).get_attribute('aria-label')))
        WebDriverWait(driver, 10, 0.5).until(EC.visibility_of_element_located((By.CSS_SELECTOR, reviewer)))
        person = driver.find_element(By.CSS_SELECTOR, reviewer).get_attribute('href')
        text = ""        

        try:
            m = driver.find_element(By.CLASS_NAME, more)
            WebDriverWait(driver, 10, 0.5).until(EC.element_to_be_clickable(m))
            m.click()
            WebDriverWait(driver, 10, 0.5).until(EC.visibility_of_element_located((By.CSS_SELECTOR, txt)))
            text += driver.find_element(By.CSS_SELECTOR, txt).text
        
        except: continue

        if keyword not in text: continue
        cur.execute("INSERT INTO reviewXiao(keyword, date, _date, stars, text, person) VALUES(?, ?, ?, ?, ?, ?)", (keyword, datedealer(_date), _date, stars, text, person))
        con.commit()

    cur.close()
    con.close()

if __name__ == "__main__":
    
    keyword = 'sushi'
    try: crawler(keyword)
    except: print(f"{keyword} - error happened, see above for details.")
