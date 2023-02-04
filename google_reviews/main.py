from webdriver_manager.microsoft import EdgeChromiumDriverManager 
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
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

    #opt.add_argument("--headless")
    opt.add_argument("--incognito")
    opt.add_argument('blink-settings=imagesEnabled=false')
    #opt.add_argument('')
    #prefs = {'profile.default_content_setting_values': { 'notifications' : 2}} # no pop up.
    #opt.add_experimental_option('prefs', prefs)
    return opt

try: 
    opt = webdriver.ChromeOptions()
    opt = optionsetter(opt)
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver = webdriver.Chrome(options = opt)

except:
    opt = webdriver.EdgeOptions()
    opt = optionsetter(opt)
    driver = webdriver.Edge(EdgeChromiumDriverManager().install())
    driver = webdriver.Edge(options = opt)

AC = ActionChains(driver)    

def crawler(keyword):
# directly consent?
    #driver.get("https://consent.google.com/m?continue=https://www.google.com/search%3Fclient%3Dopera%26q%3Dxiao%26sourceid%3Dopera%26ie%3DUTF-8%26oe%3DUTF-8%26hs%3DV6v%26tbs%3Dlrf:!1m4!1u3!2m2!3m1!1e1!1m4!1u2!2m2!2m1!1e1!2m1!1e2!2m1!1e3!2m4!1e17!4m2!17m1!1e2!3sIAE,lf:1,lf_ui:9%26tbm%3Dlcl%26sxsrf%3DAJOqlzVfFo1XkC9A5f09hJB14j-JsY1ZJg:1675415002432%26rflfq%3D1%26num%3D10%26rldimm%3D18146486695482477482%26lqi%3DCgR4aWFvSIeE2onTrYCACFoKEAAYACIEeGlhb5IBEWJ1ZmZldF9yZXN0YXVyYW50mgEkQ2hkRFNVaE5NRzluUzBWSlEwRm5TVVIxTTI4eU5UTkJSUkFCqgEMEAEqCCIEeGlhbyhF%26phdesc%3DFAU8_Opu34w%26ved%3D2ahUKEwiZ1sig__j8AhVggv0HHQQKAPkQvS56BAgLEAE%26sa%3DX%26rlst%3Df&gl=DE&m=0&pc=srp&uxe=none&hl=zh-TW&src=1#rlfi=hd:;si:18146486695482477482,l,CgR4aWFvSIeE2onTrYCACFoKEAAYACIEeGlhb5IBEWJ1ZmZldF9yZXN0YXVyYW50mgEkQ2hkRFNVaE5NRzluUzBWSlEwRm5TVVIxTTI4eU5UTkJSUkFCqgEMEAEqCCIEeGlhbyhF,y,FAU8_Opu34w;mv:[[51.99692691642221,7.6851771800781155],[51.02606091560833,4.7298549144531155],null,[51.51408037099575,6.2075160472656155],9];tbs:lrf:!1m4!1u3!2m2!3m1!1e1!1m4!1u2!2m2!2m1!1e1!2m1!1e2!2m1!1e3!2m4!1e17!4m2!17m1!1e2!3sIAE,lf:1,lf_ui:9")
    driver.get("https://www.google.com/search?q=google+reviews+on+xiao+oberhausen&client=opera&hs=91f&sxsrf=AJOqlzXvGMJw8ErgacEa5RtF9uj6G2COYw%3A1675512109159&ei=LUneY7ylCZ-F9u8P26a8iAI&oq=google+reviews+on+xiao+oberhau&gs_lcp=Cgxnd3Mtd2l6LXNlcnAQAxgAMgUIIRCgAToKCAAQRxDWBBCwAzoHCCEQoAEQCkoECEEYAEoECEYYAFDRA1j_DmC6GmgBcAF4AIABcYgBxQWSAQM3LjGYAQCgAQHIAQLAAQE&sclient=gws-wiz-serp#lrd=0x47b8eb101bfd30d3:0xfbd545815d95cbaa,1,,,,")
               #https://www.google.com/search?q=google+reviews+on+xiao+oberhausen&client=opera&hs=91f&sxsrf=AJOqlzXvGMJw8ErgacEa5RtF9uj6G2COYw%3A1675512109159&ei=LUneY7ylCZ-F9u8P26a8iAI&oq=google+reviews+on+xiao+oberhau&gs_lcp=Cgxnd3Mtd2l6LXNlcnAQAxgAMgUIIRCgAToKCAAQRxDWBBCwAzoHCCEQoAEQCkoECEEYAEoECEYYAFDRA1j_DmC6GmgBcAF4AIABcYgBxQWSAQM3LjGYAQCgAQHIAQLAAQE&sclient=gws-wiz-serp#lrd=0x47b8eb101bfd30d3:0xfbd545815d95cbaa,1,,,,
    review_css = "#akp_tsuid_29 > div > div:nth-child(1) > div > g-sticky-content-container > div > block-component > div > div.dG2XIf.knowledge-panel.Wnoohf.OJXvsb > div > div > div > div.ifM9O > div > div > div:nth-child(5) > div.AfIYPc > g-sticky-content > div > div.YoOupc.UxY8gd.E0kSRb.xSizI > g-tabs > div > div > a:nth-child(4)"
    WebDriverWait(driver, 10, 0.5).until(EC.presence_of_element_located((By.CSS_SELECTOR, review_css)))
    review = WebDriverWait(driver, 10, 0.5).until(EC.element_to_be_clickable(driver.find_element(By.CSS_SELECTOR, review_css)))                                             
    AC.move_to_element(review).click().scroll_by_amount(0, 2000).perform()
    driver.execute_script("window.scrollBy(0, document.documentElement.scrollHeight)")
    sleep(6)  
    #_recent()
    return True

def _recent(): # cannot be found for now.

    recent_css = "#_lyveY7C9D8T3kwXu1JIQ_6 > div.mR2gOd > div > div:nth-child(2)"
    WebDriverWait(driver, 10, 0.5).until(EC.presence_of_element_located((By.CSS_SELECTOR, recent_css)))
    recent = driver.find_element(By.CSS_SELECTOR, recent_css)
    WebDriverWait(driver, 10, 0.5).until(EC.element_to_be_clickable(recent))
    recent.click()

def catcher(keyword):

    for i in range(1, 4): # once for 100 reviews
    
        sq = f"#tsuid_lyveY7C9D8T3kwXu1JIQ_1reviewSort > div > div.gws-localreviews__general-reviews-block > div:nth-child({i}) > div.jxjCjc > div:nth-child(4)"
        timestamp = sq + " > div.PuaHbe > span.dehysf.lTi8oc" # text
        star = sq + " > div.PuaHbe > g-review-stars > span" # aria-label as attribute
        more = sq + " > div.Jtu6Td > span > span > a" # if none, pass.
        txt = sq + " > div.Jtu6Td > span > span > span:nth-child(1) > span" # if none, pass.
        reviewer = f"#tsuid_lyveY7C9D8T3kwXu1JIQ_1reviewSort > div > div.gws-localreviews__general-reviews-block > div:nth-child({i}) > div.jxjCjc > div:nth-child(1) > div > a"
            
        WebDriverWait(driver, 10, 0.5).until(EC.visibility_of_element_located((By.CSS_SELECTOR, star)))
        stars = int(re.sub(r"[0\D]", "", driver.find_element(By.CSS_SELECTOR, star).get_attribute('aria-label')))
        WebDriverWait(driver, 10, 0.5).until(EC.visibility_of_element_located((By.CSS_SELECTOR, reviewer)))
        person = driver.find_element(By.CSS_SELECTOR, reviewer).get_attribute('href')       
        WebDriverWait(driver, 10, 0.5).until(EC.presence_of_element_located((By.CSS_SELECTOR, timestamp)))
        _date = driver.find_element(By.CSS_SELECTOR, timestamp).text
        text = ""        

        try:
            m = driver.find_element(By.CLASS_NAME, more)
            WebDriverWait(driver, 10, 0.5).until(EC.element_to_be_clickable(m))
            m.click()
            WebDriverWait(driver, 10, 0.5).until(EC.visibility_of_element_located((By.CSS_SELECTOR, txt)))
            text += driver.find_element(By.CSS_SELECTOR, txt).text
        
        except: continue

        if keyword not in text: continue
        
        con = sqlite3.connect("db.db")
        cur = con.cursor()
        cur.execute("INSERT INTO reviewXiao(keyword, date, _date, stars, text, person) VALUES(?, ?, ?, ?, ?, ?)", (keyword, datedealer(_date), _date, stars, text, person))
        con.commit()
        cur.close()
        con.close()

if __name__ == "__main__":
    
    keyword = 'sushi'
    #try: 
    if crawler(keyword): catcher(keyword)
    #except: print(f"{keyword} - error happened, see above for details.")
