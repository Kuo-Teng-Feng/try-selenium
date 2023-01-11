#only if necessary. implies cookies handler to maintain login status during page changes.

import infos
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

#cookies = driver.get_cookies()
#cookie value = driver.get_cookie(name)
#driver.add_cookie(dict)

info = infos.getter()['login'] # entry, keywords, login as keys in dict. values: list.
