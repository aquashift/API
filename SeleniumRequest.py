from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import requests
import time

chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--window-size=1920,1080")

# Update path to your ChromeDriver executable
chrome_service = Service(r"C:/Users/ckirb/ZAP/webdriver/windows/32/chromedriver.exe")
driver = webdriver.Chrome(service=chrome_service, options=chrome_options)

# 1️⃣ Go to login page
login_url = "https://paradot.ai/login"
driver.get(login_url)

# 2️⃣ Click "Continue with Google"
google_btn = driver.find_element(By.CSS_SELECTOR, ".login-btn-google-content")
google_btn.click()

# 3️⃣ Switch to popup and pick your account
time.sleep(5)
if len(driver.window_handles) > 1:
    driver.switch_to.window(driver.window_handles[-1])
    account_btn = driver.find_element(By.CSS_SELECTOR, "div[data-email='ckirby1@gmail.com']")
    account_btn.click()
    driver.switch_to.window(driver.window_handles[0])

# 4️⃣ Switch back to main site
time.sleep(3)
driver.switch_to.window(driver.window_handles[0])

# 5️⃣ Grab cookies
selenium_cookies = driver.get_cookies()
cookies = {c['name']: c['value'] for c in selenium_cookies}
for c in cookies.items():   # code success test/sanity test
    print(c)
driver.quit()




# 6️⃣ Use cookies with requests
session = requests.Session()
session.cookies.update(cookies)
session.headers.update({
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/114.0",
})

# 7️⃣ Hit API endpoint
api_url = "https://sentry.vsa.ai/api/9/envelope"
resp = session.get(api_url)
print(resp.status_code)
print(resp.text)
