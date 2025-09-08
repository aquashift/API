from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import requests
import time


API_BASE_URL0 = "https://sentry.vsa.ai/api/9/"
API_BASE_URL1 = "https://sentry.vsa.ai/api/9/envelope"
API_BASE_URL2 = "https://paradot.ai/api/business/ai/chat"
API_BASE_URL3 = "https://paradot.ai/api/business/app/user/lang"
API_BASE_URL4 = "https://paradot.ai/api/business/config/static/files"
API_BASE_URL5 = "https://paradot.ai/api/business/gif/category/search"
API_BASE_URL6 = "https://paradot.ai/api/business/feed/latest/postcode"
API_BASE_URL7 = "https://paradot.ai/api/business/group/chat/records"
API_BASE_URL8 = "https://paradot.ai/api/business/group/chat/memories"
API_BASE_URL9 = "https://paradot.ai/api/business/group/details"
API_BASE_URL10 = "https://paradot.ai/api/business/raw/find/page/v3"
API_BASE_URL11 = "https://paradot.ai/api/business/user/login/logic"
API_BASE_URL12 = "https://paradot.ai/api/user/extend/find"
API_BASE_URL13 = "https://www.youtube.com/api/stats/"

API_BASE_URLS = [API_BASE_URL0, API_BASE_URL1, API_BASE_URL2, API_BASE_URL3, API_BASE_URL4, API_BASE_URL5, API_BASE_URL6, API_BASE_URL7, API_BASE_URL8, API_BASE_URL9,
            API_BASE_URL10, API_BASE_URL11, API_BASE_URL12, API_BASE_URL13]
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--window-size=1920,1080")

# Update path to your ChromeDriver executable
chrome_service = Service(r"C:/Users/ckirb/ZAP/webdriver/windows/32/chromedriver.exe")
driver = webdriver.Chrome(service=chrome_service, options=chrome_options)

try:
    # 1️⃣ Go to login page
    login_url = "https://paradot.ai/login"
    driver.get(login_url)

    # 2️⃣ Click "Continue with Google"
    from selenium.common.exceptions import NoSuchElementException, TimeoutException

    try:
        google_btn = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, ".login-btn-google-content"))
        )
        google_btn.click()
    except (NoSuchElementException, TimeoutException):
        print("Google login button not found or not clickable")
   
    # Wait for the popup window to appear and the Google account button to be present
    WebDriverWait(driver, 10).until(lambda d: len(d.window_handles) > 1)
    driver.switch_to.window(driver.window_handles[-1])
    account_btn = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "div[data-email='ckirby1@gmail.com']"))
        
    )
    account_btn.click()

    
    # 4️⃣ Switch back to main site
    # Wait until a specific element is present on the main page after login
    driver.switch_to.window(driver.window_handles[0])
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".logo-container img"))
    )
    
    # 5️⃣ Grab cookies
    selenium_cookies = driver.get_cookies()
    cookies = {c['name']: c['value'] for c in selenium_cookies}
    for c in cookies.items():   # code success test/sanity test
        print(c)
finally:
    driver.quit()




# 6️⃣ Use cookies with requests
session = requests.Session()
session.cookies.update(cookies)
session.headers.update({
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/114.0",
})

# 6.a  Iterate over API list

for item in API_BASE_URLS:
    try:
        response = session.get(item)
        response.raise_for_status()
        HTTP_Status = response.status_code
        print(f"Success in requesting {item}: {HTTP_Status}") #prints HTTP status code
        response_length = len(response.content)
        print(f"{item} has a response length of {response_length}")
        content_type = response.headers.get('Content-Type')
        # JSON keys preview
        if "application/json" in content_type:
            try:
                json_preview = response.json()
                print(f"JSON preview keys: {list(json_preview.keys())[:5]}")
            except Exception as e:
                print(f"Whoops, error w/ JSON: {e}")
        
        print(f"Header: {content_type}")
        final_URL = response.url
        print(f"After redirects, final URL: {final_URL}")
        stored_cookies = response.cookies.get_dict()
        print(f"Stored cookies: {stored_cookies}\n")
        # Truncating logs of body for preview
        try:
            resp_text = response.text
            body_preview = resp_text[:350] # left boundary defaults to 0,  so [:300] equivalent to slice [0:300]
            print(f"Preview of response body: {body_preview}\n")
        except Exception as e:
            print(f"Whoops, error: {e}")
        
    except requests.exceptions.RequestException as e:
        print(f"Error requesting {item}: {e}\n")



# 7️⃣ (Optional) Hit a specific API endpoint again if needed
# If you want to re-request a specific endpoint for additional processing, uncomment below:
# api_url = "https://sentry.vsa.ai/api/9/envelope"
# resp = session.get(api_url)
# print(resp.status_code)
# print(resp.text)
