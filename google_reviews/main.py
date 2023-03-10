from webdriver_manager.microsoft import EdgeChromiumDriverManager 
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains, ScrollOrigin
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from time import sleep
from datedealer import datedealer
import sqlite3
import re

def optionsetter(opt): # faster and cleaner without GUI/interface.

    opt.add_argument("--headless")
    opt.add_argument("--incognito")
    opt.add_argument('blink-settings=imagesEnabled=false')
    #opt.add_argument('')
    prefs = {'profile.default_content_setting_values': { 'notifications' : 2}} # no pop up. working?
    opt.add_experimental_option('prefs', prefs)
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

def crawler():

    driver.get("https://www.google.com/search?q=google+reviews+on+xiao+oberhausen&client=opera&hs=91f&sxsrf=AJOqlzXvGMJw8ErgacEa5RtF9uj6G2COYw%3A1675512109159&ei=LUneY7ylCZ-F9u8P26a8iAI&oq=google+reviews+on+xiao+oberhau&gs_lcp=Cgxnd3Mtd2l6LXNlcnAQAxgAMgUIIRCgAToKCAAQRxDWBBCwAzoHCCEQoAEQCkoECEEYAEoECEYYAFDRA1j_DmC6GmgBcAF4AIABcYgBxQWSAQM3LjGYAQCgAQHIAQLAAQE&sclient=gws-wiz-serp#lrd=0x47b8eb101bfd30d3:0xfbd545815d95cbaa,1,,,,")
    sleep(2)
    accept = driver.find_element(By.ID, "L2AGLb")
    WebDriverWait(driver, 10, 0.5).until(EC.element_to_be_clickable(accept))
    accept.click()
# default: relevance.    


    return True

def parser(keyword, rounds): # 10 reviews checked / round.

    blocks = ["#reviewSort > div:nth-child(1) > div.gws-localreviews__general-reviews-block > div:nth-child({}) > div.jxjCjc"]

    for i in range(0, rounds): # check 10 reviews / round
#        if i == 0: # expand the first 10 once. Necessary?
#            WebDriverWait(driver, 10, 0.5).until(EC.visibility_of_any_elements_located((By.CLASS_NAME, "review-more-link")))
#            exps = driver.find_elements(By.CLASS_NAME, "review-more-link")

#            for exp in exps: # <= n of 10 reviews. 0-2 exps in each review.
#                WebDriverWait(driver, 10, 0.5).until(EC.element_to_be_clickable(exp))
#                driver.execute_script('arguments[0].scrollIntoView(false);', exp) # did move.
#                exp.click()
#                sleep(1)       
        sleep(2)
        print(i, "round:")
        _parser(keyword, blocks)        

def _parser(keyword, blocks): # > 10 must scroll down.
    #driver.execute_script("""document.addEventListener('DOMContentLoaded', () => {
    #const ms = document.querySelector(".review-more-link");
    #for (let i = 0; i < 10; i++) { ms[i].setAttribute("aria-expanded", "true");}
    #})""") not working.
    # The way to expand is to modify?
    for i in range(1, 11): # > 10 requires reloading.

        base = blocks[len(blocks)-1].format(i)

        person_css = base + " > div:nth-child(1) > div > a"
        WebDriverWait(driver, 10, 0.5).until(EC.visibility_of_element_located((By.CSS_SELECTOR, person_css)))
        person = driver.find_element(By.CSS_SELECTOR, person_css).get_attribute("href")

        time_css = base + " > div:nth-child(4) > div.PuaHbe > span.dehysf.lTi8oc"
        WebDriverWait(driver, 10, 0.5).until(EC.visibility_of_element_located((By.CSS_SELECTOR, time_css)))
        _date = driver.find_element(By.CSS_SELECTOR, time_css).text   

        star_css = base + " > div:nth-child(4) > div.PuaHbe > g-review-stars > span"
        WebDriverWait(driver, 10, 0.5).until(EC.visibility_of_element_located((By.CSS_SELECTOR, star_css)))
        star = driver.find_element(By.CSS_SELECTOR, star_css).get_attribute("aria-label")
        stars = int(re.sub(r"\(.+\)|[\D0\.]", "", star))

        exp_css = base + " > div:nth-child(4) > div.Jtu6Td > span > span > a"
        try: 
            exp = driver.find_element(By.CSS_SELECTOR, exp_css)
            WebDriverWait(driver, 10, 0.5).until(EC.element_to_be_clickable(exp))
            exp.click()
            sleep(1)
        except: pass

        txt_css = base + " > div:nth-child(4) > div.Jtu6Td > span > span > span:nth-child(1) > span"
        try: # if none, then pass.
            WebDriverWait(driver, 10, 0.5).until(EC.visibility_of_element_located((By.CSS_SELECTOR, txt_css)))
            text = driver.find_element(By.CSS_SELECTOR, txt_css).text # no text if no exp or simply no text at all.
            if keyword in text: 
                print(_date, datedealer(_date), stars)
                save(keyword, _date, stars, text, person)
        except: pass

    _scrolldown(blocks)

def _scrolldown(blocks):
    #driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", btm) # not working?
    AC.scroll_from_origin(ScrollOrigin.from_element(driver.find_element(By.ID, "reviewSort")), 0, 3000).perform()
    sleep(1)
    former = blocks[len(blocks)-1]
    next = re.sub(r"\d+", "{}", former.format(1), count=1)
    _from = int(re.search(r"\d+", former).group(0))

    for i in range(_from + 1, 100): # start checking from #reviewSort > div:nth-child(n+1)...

        block_css = next.format(i)
        print(block_css)

        try:
            WebDriverWait(driver, 10, 0.5).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, block_css)))
            blocks.append(block_css.replace("div:nth-child(1) > div.jxjCjc", "div:nth-child({}) > div.jxjCjc"))
            break

        except: pass # if no such review-block. could be <script> ...etc.

    psudocieling = driver.find_element(By.CSS_SELECTOR, blocks[len(blocks)-1].format(1) + " > div:nth-child(1) > div > a") # 1. person of the next block.
    driver.execute_script('arguments[0].scrollIntoView();', psudocieling)

def save(keyword, _date, stars, text, person):

    con = sqlite3.connect("db.db")
    cur = con.cursor()

    res = cur.execute("SELECT keyword, text, person FROM reviewXiao WHERE keyword = ? AND text = ? AND person = ?", (keyword, text, person))
    if len(res.fetchall()) == 0:
        cur.execute("INSERT INTO reviewXiao(keyword, date, _date, stars, text, person) VALUES(?, ?, ?, ?, ?, ?)", (keyword, datedealer(_date), _date, stars, text, person))
        con.commit()

    cur.close()
    con.close()

if __name__ == "__main__":
 
    if crawler(): parser("sushi", 100) # n * 10 reviews to check.

def old_crawler(keyword):
# directly consent?
    driver.get("https://consent.google.com/m?continue=https://www.google.com/search%3Fclient%3Dopera%26q%3Dxiao%26sourceid%3Dopera%26ie%3DUTF-8%26oe%3DUTF-8%26hs%3DV6v%26tbs%3Dlrf:!1m4!1u3!2m2!3m1!1e1!1m4!1u2!2m2!2m1!1e1!2m1!1e2!2m1!1e3!2m4!1e17!4m2!17m1!1e2!3sIAE,lf:1,lf_ui:9%26tbm%3Dlcl%26sxsrf%3DAJOqlzVfFo1XkC9A5f09hJB14j-JsY1ZJg:1675415002432%26rflfq%3D1%26num%3D10%26rldimm%3D18146486695482477482%26lqi%3DCgR4aWFvSIeE2onTrYCACFoKEAAYACIEeGlhb5IBEWJ1ZmZldF9yZXN0YXVyYW50mgEkQ2hkRFNVaE5NRzluUzBWSlEwRm5TVVIxTTI4eU5UTkJSUkFCqgEMEAEqCCIEeGlhbyhF%26phdesc%3DFAU8_Opu34w%26ved%3D2ahUKEwiZ1sig__j8AhVggv0HHQQKAPkQvS56BAgLEAE%26sa%3DX%26rlst%3Df&gl=DE&m=0&pc=srp&uxe=none&hl=zh-TW&src=1#rlfi=hd:;si:18146486695482477482,l,CgR4aWFvSIeE2onTrYCACFoKEAAYACIEeGlhb5IBEWJ1ZmZldF9yZXN0YXVyYW50mgEkQ2hkRFNVaE5NRzluUzBWSlEwRm5TVVIxTTI4eU5UTkJSUkFCqgEMEAEqCCIEeGlhbyhF,y,FAU8_Opu34w;mv:[[51.99692691642221,7.6851771800781155],[51.02606091560833,4.7298549144531155],null,[51.51408037099575,6.2075160472656155],9];tbs:lrf:!1m4!1u3!2m2!3m1!1e1!1m4!1u2!2m2!2m1!1e1!2m1!1e2!2m1!1e3!2m4!1e17!4m2!17m1!1e2!3sIAE,lf:1,lf_ui:9")

    review_css = "#akp_tsuid_29 > div > div:nth-child(1) > div > g-sticky-content-container > div > block-component > div > div.dG2XIf.knowledge-panel.Wnoohf.OJXvsb > div > div > div > div.ifM9O > div > div > div:nth-child(5) > div.AfIYPc > g-sticky-content > div > div.YoOupc.UxY8gd.E0kSRb.xSizI > g-tabs > div > div > a:nth-child(4)"
    WebDriverWait(driver, 10, 0.5).until(EC.presence_of_element_located((By.CSS_SELECTOR, review_css)))
    review = driver.find_element(By.CSS_SELECTOR, review_css)
    WebDriverWait(driver, 10, 0.5).until(EC.element_to_be_clickable(review))                                             
    review.click()
    driver.execute_script("window.scrollBy(0, document.documentElement.scrollHeight)")
    sleep(1)
    #_recent()
    return True

def _recent(): # cannot be found.

    recent_css = "#_lyveY7C9D8T3kwXu1JIQ_6 > div.mR2gOd > div > div:nth-child(2)"
    WebDriverWait(driver, 10, 0.5).until(EC.presence_of_element_located((By.CSS_SELECTOR, recent_css)))
    recent = driver.find_element(By.CSS_SELECTOR, recent_css)
    WebDriverWait(driver, 10, 0.5).until(EC.element_to_be_clickable(recent))
    recent.click()

def old_catcher(keyword): # cannot be found.

    for i in range(1, 4): # once for n reviews
    
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